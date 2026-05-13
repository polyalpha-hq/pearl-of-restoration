---
phase: 1
plan: 1
subsystem: tooling
tags: [extraction, gitignore, git-tag, python, base64, safety-net]
dependency_graph:
  requires: []
  provides: [pre-extraction-baseline-tag, .gitignore, scripts/extract_base64_images.py]
  affects: [index.html, media/]
tech_stack:
  added: [Python 3 stdlib (re, base64, json, hashlib, pathlib, argparse)]
  patterns: [magic-byte integrity check, deterministic occurrence-index mapping, dry-run guard]
key_files:
  created:
    - .gitignore
    - scripts/extract_base64_images.py
  modified: []
decisions:
  - about-director image is labeled data:image/png in HTML but contains JPEG content (JPEG magic bytes); script accepts actual content and warns — does not fail
  - BLOB_MAP encodes occurrence-index → filename as a hard-coded list, not inferred from HTML, to guarantee determinism
  - Magic-byte check is the integrity gate (not MIME type), preventing corrupt blob writes
metrics:
  duration: ~12 minutes
  completed: "2026-05-13"
  tasks: 2
  files: 2
---

# Phase 1 Plan 1: Build Extraction Tooling and Safety Net Summary

**One-liner:** Git safety net (pre-extraction-baseline tag + .gitignore) and stdlib Python extractor with magic-byte integrity verification for all 14 base64 blobs.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Tag pre-extraction baseline and add .gitignore | d3698f7 | .gitignore (created), .DS_Store (untracked), media/.DS_Store (untracked) |
| 2 | Write the base64 extraction script | 93533a8 | scripts/extract_base64_images.py (created, 153 lines) |

## Artifacts

### .gitignore

Created at repo root with the following entries (LF line endings, trailing newline):

```
.DS_Store
**/.DS_Store
media/.DS_Store
Thumbs.db
__pycache__/
*.pyc
index.html.new
```

Also untracked `.DS_Store` and `media/.DS_Store` via `git rm --cached` — both were previously tracked.

### Git Tag pre-extraction-baseline

- Points to commit: `0849332` (docs(01): create phase plan)
- Tag SHA: `abb92222607f26d79a0f625fa3a97a62f510bceb`
- Rollback command: `git checkout pre-extraction-baseline -- index.html`

### scripts/extract_base64_images.py

- **Line count:** 153
- **Imports (stdlib only):** re, base64, json, sys, argparse, hashlib, pathlib.Path
- **Behavior:** reads index.html in binary/UTF-8, finds all 14 base64 blobs via single-pass combined regex, verifies magic bytes, decodes with validate=True, writes decoded files to media/ and rewritten HTML to index.html.new
- **Dry-run flag:** --dry-run skips all disk writes, emits JSON to stdout only
- **Never writes to index.html directly**

## Dry-Run Report (verbatim JSON from --dry-run index.html)

```json
[
  {
    "index": 0,
    "filename": "media/hero-bg.jpg",
    "bytes": 623152,
    "sha256": "1431fa1c8213ecad224f4eb2a0e989d19560bdda998d7c08dc4f4904a0c89dc9",
    "source_line_approx": 45
  },
  {
    "index": 1,
    "filename": "media/iceland-bg.jpg",
    "bytes": 338834,
    "sha256": "2d28b292ac26930b00be23073fc49668254b77c535bc216b56c3da94752222d6",
    "source_line_approx": 70
  },
  {
    "index": 2,
    "filename": "media/cosmos-bg.jpg",
    "bytes": 1763108,
    "sha256": "ab95a5a51798f2762b921ba7d7f30d7372babb8b68892f4fa34174c91daab9d6",
    "source_line_approx": 76
  },
  {
    "index": 3,
    "filename": "media/about-director.png",
    "bytes": 641504,
    "sha256": "d8d24651b5fce0fd2005a0e517dd172109851b10b254fd54d3d15c271c148e7d",
    "source_line_approx": 406
  },
  {
    "index": 4,
    "filename": "media/block1-photo-1.jpg",
    "bytes": 213641,
    "sha256": "bc37d0700a07f766a96dff45bce6d8493a0ec7e823b234485b7130de11ac3d32",
    "source_line_approx": 488
  },
  {
    "index": 5,
    "filename": "media/block1-photo-2.jpg",
    "bytes": 189379,
    "sha256": "83aec6ce4e1f8a2491bb0c508f1f7ae6e334546264eae2d8c45faf5fc5a402c8",
    "source_line_approx": 489
  },
  {
    "index": 6,
    "filename": "media/block1-photo-3.jpg",
    "bytes": 157710,
    "sha256": "d6431ff2dc73be29a710daa406a1aa8413ecf678030bfaea3195ddde30f425b9",
    "source_line_approx": 490
  },
  {
    "index": 7,
    "filename": "media/block1-photo-4.jpg",
    "bytes": 183479,
    "sha256": "e2e7b98a578bee5d07e5e0d0b0a20e3285076b00e6c265fbac62b3cee86a006c",
    "source_line_approx": 491
  },
  {
    "index": 8,
    "filename": "media/block1-photo-5.jpg",
    "bytes": 195842,
    "sha256": "edfe6ab39801a0c6281ad034c000e30f07e30f66526c16e874671c2379623ab0",
    "source_line_approx": 492
  },
  {
    "index": 9,
    "filename": "media/block1-photo-6.jpg",
    "bytes": 198826,
    "sha256": "b7e488e61e6c41193e7cdd80c6d00bfe62a02df69db60a6e35949b1c9f757263",
    "source_line_approx": 493
  },
  {
    "index": 10,
    "filename": "media/block1-photo-7.jpg",
    "bytes": 101668,
    "sha256": "231a169f152d065c14a605753155d8440c4bc14eb44f755e1f78d56e6dd14e51",
    "source_line_approx": 494
  },
  {
    "index": 11,
    "filename": "media/block3-photo-1.jpg",
    "bytes": 58872,
    "sha256": "5e5f6b7e2ebafb8d87cb89a6f70d4107a39a195e9c97a1cef9d07d9e33d87326",
    "source_line_approx": 508
  },
  {
    "index": 12,
    "filename": "media/block3-photo-2.jpg",
    "bytes": 746721,
    "sha256": "e63e94796fcd465a7e2bea1f51125690be23639ee54c5a42be0e308b3309ebe7",
    "source_line_approx": 509
  },
  {
    "index": 13,
    "filename": "media/block4-photo-1.jpg",
    "bytes": 1230951,
    "sha256": "1e8e42f0581a04c475c91ff5d3f7a94c43441012044806a574cda4579e222248",
    "source_line_approx": 514
  }
]
```

## index.html Size Confirmation

`wc -c index.html` = **8940016 bytes** — unchanged from plan start.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] about-director image mislabeled as PNG in HTML source**
- **Found during:** Task 2 (dry-run execution)
- **Issue:** index.html contains `data:image/png;base64,...` for the about-director image, but the decoded bytes start with `\xff\xd8\xff` (JPEG magic). The plan assumed the MIME type in the HTML was authoritative.
- **Fix:** Changed `decode_and_verify` to detect actual format from magic bytes rather than trusting the HTML MIME declaration. If declared MIME mismatches actual magic bytes but the bytes are valid image data (either JPEG or PNG), the script logs a WARNING and accepts the content. Only exits non-zero if magic bytes match neither format.
- **Files modified:** scripts/extract_base64_images.py (decode_and_verify function)
- **Commit:** 93533a8
- **Impact on plan output:** None — the filename `media/about-director.png` is preserved as planned (matching acceptance criteria), and the dry-run produces the correct 14-entry JSON.

## Known Stubs

None — this plan creates tooling, not UI or data-serving code.

## Threat Surface Scan

No new network endpoints, auth paths, or trust boundaries introduced. The script reads only local files (index.html) and writes only to `media/` and `index.html.new` — paths derived from the script's own hard-coded mapping table, not from user input. Threat model coverage per plan:
- T-01-01 (tampering via index.html write): mitigated — script output path hard-coded to `index.html.new`
- T-01-02 (corrupted base64): mitigated — `validate=True` + magic-byte gate
- T-01-03 (regex backtracking): mitigated — bounded character classes, dry-run completes in <2 seconds on 8.5MB file
- T-01-04 (.DS_Store disclosure): mitigated — .gitignore created and existing .DS_Store untracked
- T-01-05 (rollback loss): mitigated — pre-extraction-baseline tag created at abb9222

## Self-Check: PASSED

- [x] `.gitignore` exists: confirmed
- [x] `scripts/extract_base64_images.py` exists: confirmed (153 lines)
- [x] `pre-extraction-baseline` tag exists: abb92222607f26d79a0f625fa3a97a62f510bceb
- [x] Task 1 commit d3698f7: confirmed in git log
- [x] Task 2 commit 93533a8: confirmed in git log
- [x] `index.html` size = 8940016 bytes: confirmed
- [x] No `media/hero-bg.jpg` or `index.html.new` created: confirmed
- [x] Dry-run produces 14-entry JSON in correct filename order: confirmed
