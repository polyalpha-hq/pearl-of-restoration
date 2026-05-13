"""Phase 1 — Image Extraction & Baseline (PERF-01 / PERF-02)
Extracts 14 base64 image blobs from index.html → media/<name> + index.html.new.
NEVER writes to index.html directly. Rollback: git checkout pre-extraction-baseline -- index.html
Usage: python3 scripts/extract_base64_images.py [--dry-run] [input_html]
"""
import re
import base64
import json
import sys
import argparse
import hashlib
from pathlib import Path

# occurrence-index → (filename, declared_fmt); indices 0-13 in file order
BLOB_MAP = [
    (0,  "media/hero-bg.jpg",        "jpeg"),   # line 45  — #hero-img CSS bg
    (1,  "media/iceland-bg.jpg",     "jpeg"),   # line 70  — #iceland-bg CSS bg
    (2,  "media/cosmos-bg.jpg",      "jpeg"),   # line 76  — #cosmos-bg CSS bg
    (3,  "media/about-director.png", "png"),    # line 406 — .about-img rv <img>
    (4,  "media/block1-photo-1.jpg", "jpeg"),   # line 488 — Block I gallery
    (5,  "media/block1-photo-2.jpg", "jpeg"),   # line 489
    (6,  "media/block1-photo-3.jpg", "jpeg"),   # line 490
    (7,  "media/block1-photo-4.jpg", "jpeg"),   # line 491
    (8,  "media/block1-photo-5.jpg", "jpeg"),   # line 492
    (9,  "media/block1-photo-6.jpg", "jpeg"),   # line 493
    (10, "media/block1-photo-7.jpg", "jpeg"),   # line 494
    (11, "media/block3-photo-1.jpg", "jpeg"),   # line 508 — Block III gallery
    (12, "media/block3-photo-2.jpg", "jpeg"),   # line 509
    (13, "media/block4-photo-1.jpg", "jpeg"),   # line 514 — Block IV gallery
]

EXPECTED_COUNT = 14

MAGIC_BYTES = {
    "jpeg": b"\xff\xd8\xff",
    "png":  b"\x89PNG\r\n\x1a\n",
}

# Single-pass regex covering both CSS url() and HTML src="" forms
PATTERN = re.compile(
    r"background-image:url\('data:image/(jpeg|jpg|png);base64,([A-Za-z0-9+/=]+)'\)"
    r"|"
    r'src="data:image/(jpeg|jpg|png);base64,([A-Za-z0-9+/=]+)"'
)


def die(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def find_matches(html_text: str) -> list:
    """Return all regex matches in file order."""
    results = []
    for m in PATTERN.finditer(html_text):
        if m.group(1):  # CSS form
            results.append({"match": m, "kind": "css", "fmt": m.group(1), "payload": m.group(2)})
        else:           # img form
            results.append({"match": m, "kind": "img", "fmt": m.group(3), "payload": m.group(4)})
    return results


def decode_and_verify(idx: int, filename: str, payload: str, html_fmt: str) -> bytes:
    """base64-decode payload, verify magic bytes, warn on MIME mismatch."""
    try:
        raw = base64.b64decode(payload, validate=True)
    except Exception as exc:
        die(f"Occurrence {idx}: base64 decode failed for {filename}: {exc}")
    # Detect actual format from magic bytes (\xff\xd8\xff = JPEG; \x89PNG = PNG)
    if raw.startswith(MAGIC_BYTES["jpeg"]):
        actual = "jpeg"
    elif raw.startswith(MAGIC_BYTES["png"]):
        actual = "png"
    else:
        die(f"Occurrence {idx}: unrecognised magic bytes for {filename} — got {raw[:8]!r}")
    norm = "jpeg" if html_fmt in ("jpeg", "jpg") else html_fmt
    if norm != actual:
        print(f"WARNING: Occurrence {idx}: HTML declares '{html_fmt}' but "
              f"magic bytes show '{actual}' for {filename} — accepting actual content.",
              file=sys.stderr)
    return raw


def build_replacement(kind: str, filename: str) -> str:
    return (f"background-image:url('{filename}')" if kind == "css"
            else f'src="{filename}"')


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract base64 images from index.html")
    parser.add_argument("input", nargs="?", default="./index.html")
    parser.add_argument("--dry-run", action="store_true",
                        help="Validate and report; write nothing to disk")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        die(f"Input file not found: {input_path}")

    output_path = input_path.parent / "index.html.new"  # never the input file

    try:
        html_text = input_path.read_bytes().decode("utf-8")
    except UnicodeDecodeError as exc:
        die(f"Cannot decode {input_path} as UTF-8: {exc}")

    matches = find_matches(html_text)
    if len(matches) != EXPECTED_COUNT:
        die(f"Expected {EXPECTED_COUNT} base64 blobs, found {len(matches)}. Refusing.")

    report = []
    replacements = []

    for idx, m_info in enumerate(matches):
        _, filename, _ = BLOB_MAP[idx]
        raw = decode_and_verify(idx, filename, m_info["payload"], m_info["fmt"])
        sha256 = hashlib.sha256(raw).hexdigest()
        approx_line = html_text[:m_info["match"].start()].count("\n") + 1

        report.append({
            "index": idx,
            "filename": filename,
            "bytes": len(raw),
            "sha256": sha256,
            "source_line_approx": approx_line,
        })
        replacements.append((m_info["match"], build_replacement(m_info["kind"], filename)))

        if not args.dry_run:
            out_file = input_path.parent / filename
            out_file.parent.mkdir(parents=True, exist_ok=True)
            out_file.write_bytes(raw)
            print(f"  wrote {filename} ({len(raw):,} bytes, sha256={sha256[:12]}…)", file=sys.stderr)

    print(json.dumps(report, indent=2))

    if not args.dry_run:
        result = html_text
        for m, repl in reversed(replacements):
            result = result[:m.start()] + repl + result[m.end():]
        output_path.write_text(result, encoding="utf-8")
        print(f"  wrote {output_path}", file=sys.stderr)

        report_path = input_path.parent / "scripts" / "extraction-report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"  wrote {report_path}", file=sys.stderr)

    print(f"\nDone: {EXPECTED_COUNT} blobs processed (dry_run={args.dry_run})", file=sys.stderr)


if __name__ == "__main__":
    main()
