---
id: "01-01"
title: "Build extraction tooling and safety net"
phase: 1
plan: 1
type: execute
wave: 1
depends_on: []
files_modified:
  - .gitignore
  - scripts/extract_base64_images.py
autonomous: true
requirements:
  - PERF-01
  - PERF-02
must_haves:
  truths:
    - "A pre-extraction snapshot of index.html is preserved as a git tag so rollback is one command"
    - ".DS_Store and OS junk files are excluded from git so they cannot be committed to media/ or repo root"
    - "An idempotent Python script exists that, given index.html, produces index.html.new with all base64 blobs replaced by media/<name> references and writes the decoded image bytes to media/"
    - "The script refuses to corrupt input — it reads index.html, never edits in place, and exits non-zero if any blob fails to decode"
    - "The script produces filenames that match the actual page structure (hero bg, iceland-bg, cosmos-bg backgrounds; about director photo; block1 7 photos; block3 2 photos; block4 1 photo)"
  artifacts:
    - path: ".gitignore"
      provides: "Repo hygiene — excludes .DS_Store, OS files, and Python bytecode"
      contains: ".DS_Store"
    - path: "scripts/extract_base64_images.py"
      provides: "Programmatic base64 extraction with byte-level integrity guarantee"
      min_lines: 60
    - path: "Git tag pre-extraction-baseline"
      provides: "Rollback anchor pointing to the 8.5MB pre-extraction index.html"
  key_links:
    - from: "scripts/extract_base64_images.py"
      to: "media/"
      via: "writes decoded bytes via base64.b64decode → open(..., 'wb').write"
      pattern: "b64decode|base64\\.decode"
    - from: "scripts/extract_base64_images.py"
      to: "index.html.new"
      via: "regex replaces each data:image blob with media/<name>"
      pattern: "data:image|re\\.sub"
    - from: ".gitignore"
      to: "git repo"
      via: "first line of repo .gitignore"
      pattern: "\\.DS_Store"
---

<objective>
Build the extraction tooling and safety net so that Plan 02 can run the extraction against the live `index.html` without risk. This plan does NOT touch `index.html` — it only creates the script that will be executed in Plan 02, plus the `.gitignore` and git tag that protect the work.

Purpose: PERF-01 and PERF-02 fail catastrophically if extraction corrupts a base64 blob silently (Pitfall #2). The fix is to never edit the 8.5MB file by hand and never run a one-shot operation without a rollback path. This plan creates both prerequisites.

Output: A reusable Python script, a `.gitignore`, and a pre-extraction git tag.
</objective>

<execution_context>
@$HOME/.claude/get-shit-done/workflows/execute-plan.md
@$HOME/.claude/get-shit-done/templates/summary.md
</execution_context>

<context>
@.planning/STATE.md
@.planning/ROADMAP.md
@.planning/REQUIREMENTS.md
@.planning/research/ARCHITECTURE.md
@.planning/research/PITFALLS.md
@.planning/codebase/STRUCTURE.md
@.planning/codebase/CONCERNS.md
@CLAUDE.md

<facts>
Verified by grep against /Users/votykvot/Desktop/pearl-of-restoration/index.html before this plan was written:
- File size: 8940016 bytes (8.5MB), 1101 lines total
- 14 base64 image occurrences total:
  - 3 CSS `background-image:url('data:image/jpeg;base64,...')` at lines 45, 70, 76 — these belong to selectors #hero-img (line 304), #iceland-bg (line 399), #cosmos-bg (line 595) respectively
  - 1 `<img src="data:image/png;base64,...">` at line 406 — inside a `<div class="about-grid">` / `<div class="about-img rv">` block (the only PNG; director portrait per CLAUDE.md About section)
  - 7 `<img src="data:image/jpeg;base64,...">` at lines 488, 489, 490, 491, 492, 493, 494 — inside `<div id="gallery-block1" class="gallery-panel">` (Block I, Industrial Oil Regeneration System — matches CLAUDE.md "Block I — 7 photos (base64)")
  - 2 `<img src="data:image/jpeg;base64,...">` at lines 508, 509 — inside `<div id="gallery-block3" class="gallery-panel">` (Block III, Activated Carbon — matches CLAUDE.md "Block III — 2 photos (base64)")
  - 1 `<img src="data:image/jpeg;base64,...">` at line 514 — inside `<div id="gallery-block4" class="gallery-panel">` (Block IV, KDK — matches CLAUDE.md "Block IV — 1 photo (base64)")
- Existing media/ folder contents: mwf-video-1.mp4, station-video-1.mp4, station-video-2.mp4 (videos already external — do not touch)
- STRUCTURE.md mentions station-1.jpg and station-7.jpg in media/ but they DO NOT EXIST on disk — STRUCTURE.md is out of date. Do not assume any image files exist in media/.
- No .gitignore exists in repo root. The `.DS_Store` file is present (CONCERNS.md #7).
- Python 3.9.6 is available at /usr/bin/python3.
- Working directory is /Users/votykvot/Desktop/pearl-of-restoration/ — all paths in this plan are relative to that root.
</facts>

<naming_scheme>
Per planning_context, extracted files use descriptive position/context names. Mapping decided in this plan and used by both `scripts/extract_base64_images.py` and Plan 02:

| Line | Source kind | Output filename | Rationale |
|------|-------------|-----------------|-----------|
| 45  | CSS bg-image | media/hero-bg.jpg          | Belongs to #hero-img |
| 70  | CSS bg-image | media/iceland-bg.jpg       | Belongs to #iceland-bg |
| 76  | CSS bg-image | media/cosmos-bg.jpg        | Belongs to #cosmos-bg |
| 406 | <img> PNG    | media/about-director.png   | Inside .about-img rv (director portrait) |
| 488 | <img> JPEG   | media/block1-photo-1.jpg   | Block I gallery, photo 1 of 7 |
| 489 | <img> JPEG   | media/block1-photo-2.jpg   | Block I gallery, photo 2 of 7 |
| 490 | <img> JPEG   | media/block1-photo-3.jpg   | Block I gallery, photo 3 of 7 |
| 491 | <img> JPEG   | media/block1-photo-4.jpg   | Block I gallery, photo 4 of 7 |
| 492 | <img> JPEG   | media/block1-photo-5.jpg   | Block I gallery, photo 5 of 7 |
| 493 | <img> JPEG   | media/block1-photo-6.jpg   | Block I gallery, photo 6 of 7 |
| 494 | <img> JPEG   | media/block1-photo-7.jpg   | Block I gallery, photo 7 of 7 |
| 508 | <img> JPEG   | media/block3-photo-1.jpg   | Block III gallery, photo 1 of 2 |
| 509 | <img> JPEG   | media/block3-photo-2.jpg   | Block III gallery, photo 2 of 2 |
| 514 | <img> JPEG   | media/block4-photo-1.jpg   | Block IV gallery, photo 1 of 1 |

The script encodes this exact mapping (line-number → filename) because the 14 base64 occurrences are at known fixed line numbers and ordering by occurrence index in the file is deterministic.
</naming_scheme>
</context>

<tasks>

<task type="auto">
  <name>Task 1: Tag pre-extraction baseline and add .gitignore</name>
  <files>.gitignore</files>
  <read_first>
    - /Users/votykvot/Desktop/pearl-of-restoration/.planning/codebase/CONCERNS.md (concern #7 — .DS_Store hygiene; concern #8 — backups outside repo should become git tags)
    - /Users/votykvot/Desktop/pearl-of-restoration/.planning/research/PITFALLS.md (Pitfall #2 — monolithic file corruption; Pitfall #17 — .DS_Store on GitHub Pages)
  </read_first>
  <action>
    Create a fresh `.gitignore` at repo root with one entry per line covering, at minimum: `.DS_Store`, `**/.DS_Store`, `Thumbs.db`, `__pycache__/`, `*.pyc`, `index.html.new` (the script's staging output — never committed; the swap commit in Plan 02 will overwrite the real `index.html` from this staging file), `media/.DS_Store`. Use plain LF line endings, no trailing whitespace, file must end with a newline. Do NOT commit the existing `.DS_Store` in the repo root if it is already tracked — first run `git rm --cached .DS_Store media/.DS_Store` (ignore errors if untracked) so the ignore takes effect cleanly.

    Then create the git tag `pre-extraction-baseline` pointing at the current HEAD commit (a3cf59d "docs: create roadmap (6 phases)") with message `Baseline before Phase 1 image extraction (index.html ~8.5MB, 14 base64 blobs)`. This is the rollback anchor per Pitfall #2 prevention guidance.

    Do NOT modify index.html in this task. Do NOT touch media/ or its existing video files.
  </action>
  <verify>
    <automated>test -f .gitignore && grep -q '\.DS_Store' .gitignore && grep -q 'index\.html\.new' .gitignore && git rev-parse pre-extraction-baseline >/dev/null 2>&1 && ! git ls-files --error-unmatch .DS_Store 2>/dev/null</automated>
  </verify>
  <acceptance_criteria>
    - `.gitignore` exists at `/Users/votykvot/Desktop/pearl-of-restoration/.gitignore` and contains the literal strings `.DS_Store` and `index.html.new` (verified by `grep -F`).
    - `git rev-parse pre-extraction-baseline` succeeds (tag exists and resolves to a commit).
    - `git ls-files .DS_Store` produces no output (the root `.DS_Store` is no longer tracked).
    - `git status --porcelain media/mwf-video-1.mp4` shows the file unchanged (existing media untouched).
    - `wc -c index.html` still reports `8940016` (index.html bytes unchanged in this task).
  </acceptance_criteria>
  <done>The repo has a working `.gitignore`, the pre-extraction git tag is in place, and `index.html` is byte-identical to the start of this task.</done>
</task>

<task type="auto">
  <name>Task 2: Write the base64 extraction script</name>
  <files>scripts/extract_base64_images.py</files>
  <read_first>
    - /Users/votykvot/Desktop/pearl-of-restoration/.planning/research/PITFALLS.md (Pitfall #2 — base64 corruption mechanism: text editors break on long lines, manual find-replace cannot be trusted)
    - /Users/votykvot/Desktop/pearl-of-restoration/.planning/research/ARCHITECTURE.md (Step 1 — Image Extraction methodology: grep, decode, replace, then verify with local HTTP server)
    - /Users/votykvot/Desktop/pearl-of-restoration/CLAUDE.md (page structure: blocks I/III/IV photo counts must match the naming scheme exactly)
  </read_first>
  <action>
    Create `scripts/extract_base64_images.py` — a Python 3 script that performs deterministic, byte-safe extraction of all 14 base64 image blobs from `index.html`. The script must be standalone (use only the standard library: `re`, `base64`, `pathlib`, `argparse`, `hashlib`, `sys`) so it runs under the system Python 3.9 with no install step.

    Behavior contract:
    1. Read `index.html` in binary mode (`rb`) from the path passed via CLI (default: `./index.html`). Decode as UTF-8 for regex; emit a hard error if decode fails.
    2. Define the explicit mapping table from `<naming_scheme>` above as a Python list of (occurrence_index, filename, expected_format) tuples — occurrence_index 0..13 in the order they appear in the file. The script asserts the count is exactly 14 at the start; if it finds more or fewer, exit non-zero with a clear message.
    3. Two regex patterns to detect:
       - CSS form: `background-image:url\('data:image/(jpeg|jpg|png);base64,([A-Za-z0-9+/=]+)'\)` — captures format + payload, replaces with `background-image:url('media/<filename>')`
       - HTML img form: `src="data:image/(jpeg|jpg|png);base64,([A-Za-z0-9+/=]+)"` — captures format + payload, replaces with `src="media/<filename>"`
       Use a single combined-pass approach: collect all matches in file order via `re.finditer` across both patterns, assign each its occurrence_index, then perform one rewrite. The expected formats per occurrence must match the mapping (occurrences 0,1,2 are jpeg via CSS; occurrence 3 is png via img; occurrences 4–13 are jpeg via img). If actual format mismatches expected format, exit non-zero.
    4. For each match: `base64.b64decode(payload, validate=True)` — `validate=True` rejects whitespace/garbage inside the blob. Write the decoded bytes to `media/<filename>` in binary mode. Compute and log the SHA-256 of each decoded byte string for the per-file integrity record.
    5. Sanity check each decoded blob's magic bytes BEFORE writing: JPEG must start with `\xff\xd8\xff`; PNG must start with `\x89PNG\r\n\x1a\n`. Mismatch → exit non-zero, do not write.
    6. Write the rewritten HTML to `index.html.new` (NOT `index.html`). The script never overwrites the input. Plan 02 is responsible for the atomic swap.
    7. Emit a JSON report to stdout listing each extracted file: `{index, filename, bytes, sha256, source_line_approx}`. Also write the report to `scripts/extraction-report.json` (created if missing). The line approximation can be derived from the byte offset of the match in the original text.
    8. Support `--dry-run` flag: do everything except writing `media/*` and `index.html.new` — useful for Plan 02's verification step.
    9. Exit 0 on full success, non-zero on any failure with a single descriptive line on stderr.

    Keep the script under 200 lines. Include a top-of-file docstring naming the phase (Phase 1, PERF-01/PERF-02), the rollback tag (`pre-extraction-baseline`), and the prohibited-output-file note (never writes to `index.html` directly).

    Do NOT execute the script in this task. Do NOT create `media/*` image files in this task. Do NOT modify `index.html`. The script is built and committed; running it is Plan 02's job.
  </action>
  <verify>
    <automated>python3 -c "import ast; ast.parse(open('scripts/extract_base64_images.py').read())" && python3 scripts/extract_base64_images.py --dry-run index.html >/tmp/extract_dryrun.json 2>/tmp/extract_dryrun.err && python3 -c "import json,sys; r=json.load(open('/tmp/extract_dryrun.json')); assert len(r)==14, f'expected 14 entries, got {len(r)}'; expected=['media/hero-bg.jpg','media/iceland-bg.jpg','media/cosmos-bg.jpg','media/about-director.png','media/block1-photo-1.jpg','media/block1-photo-2.jpg','media/block1-photo-3.jpg','media/block1-photo-4.jpg','media/block1-photo-5.jpg','media/block1-photo-6.jpg','media/block1-photo-7.jpg','media/block3-photo-1.jpg','media/block3-photo-2.jpg','media/block4-photo-1.jpg']; got=[e['filename'] for e in r]; assert got==expected, f'filename order mismatch:\n  expected: {expected}\n  got:      {got}'; print('OK')" && test ! -e media/hero-bg.jpg && test ! -e index.html.new</automated>
  </verify>
  <acceptance_criteria>
    - `scripts/extract_base64_images.py` exists and parses as valid Python 3 (`ast.parse` succeeds — no syntax errors).
    - The script uses ONLY standard-library imports. `grep -E "^import |^from " scripts/extract_base64_images.py | grep -vE "^(import |from )(re|base64|pathlib|argparse|hashlib|sys|json|os)( |$)"` must produce no output.
    - `python3 scripts/extract_base64_images.py --dry-run index.html` exits 0 and emits a 14-entry JSON array on stdout where the `filename` field for entries 0..13 matches in order: `media/hero-bg.jpg`, `media/iceland-bg.jpg`, `media/cosmos-bg.jpg`, `media/about-director.png`, `media/block1-photo-1.jpg` through `media/block1-photo-7.jpg`, `media/block3-photo-1.jpg`, `media/block3-photo-2.jpg`, `media/block4-photo-1.jpg`.
    - After dry-run, `media/hero-bg.jpg` does NOT exist and `index.html.new` does NOT exist (dry-run wrote nothing).
    - `wc -c index.html` still reports `8940016` after dry-run.
    - The string `b64decode` and the substring `validate=True` both appear in the script source (`grep -F 'b64decode' scripts/extract_base64_images.py && grep -F 'validate=True' scripts/extract_base64_images.py`).
    - The strings `\xff\xd8\xff` (or its raw form `b'\xff\xd8\xff'`) and `\x89PNG` appear in the script — magic-byte checks are present.
    - The script never opens `index.html` in write mode: `grep -E "open\\([^)]*index\\.html[^)]*['\"]w" scripts/extract_base64_images.py` produces no match.
  </acceptance_criteria>
  <done>The extraction script is written, parses cleanly, runs the dry-run path against the real `index.html`, and reports the expected 14 outputs in the exact filename order — without having modified `index.html`, `media/`, or anything else on disk other than the script file and `scripts/extraction-report.json` (if produced by dry-run; the script may skip writing the report on dry-run if implemented that way).</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| disk → script | The script consumes index.html bytes as untrusted input — corrupted base64 or unexpected character ranges could trigger an exception or produce invalid binaries |
| script → media/ | The script writes binary files into a directory that is publicly served by GitHub Pages — every byte must be image data, not arbitrary attacker-controlled content |
| git tag → future commits | The pre-extraction-baseline tag is the only rollback anchor; if it is deleted or moved, the safety net is lost |

## STRIDE Threat Register

| Threat ID | Category | Component | Disposition | Mitigation Plan |
|-----------|----------|-----------|-------------|-----------------|
| T-01-01 | Tampering | scripts/extract_base64_images.py overwriting index.html | mitigate | Script is hard-coded to write only to `index.html.new`, never `index.html`. Acceptance criterion greps for any `open("index.html", "w...")` and fails on match. |
| T-01-02 | Tampering | Corrupted base64 producing junk image files | mitigate | Two-layer check before writing each file: (1) `base64.b64decode(..., validate=True)` rejects non-base64 chars including whitespace; (2) magic-byte verification (JPEG `\xff\xd8\xff`, PNG `\x89PNG\r\n\x1a\n`) catches truncation. Any failure exits non-zero before any disk write. |
| T-01-03 | Denial of Service | Regex catastrophic backtracking on 8.5MB input | mitigate | Patterns use bounded character classes `[A-Za-z0-9+/=]+` with no nested quantifiers and no backreferences. Python's `re` engine handles this in linear time for these patterns. Validated by the script completing dry-run in <5 seconds on the actual 8.5MB file. |
| T-01-04 | Information Disclosure | .DS_Store committed to public GitHub Pages repo leaks developer filesystem metadata | mitigate | `.gitignore` adds `.DS_Store` and `**/.DS_Store` BEFORE the extraction commit; Task 1 also runs `git rm --cached` to untrack any existing instance. Per Pitfall #17. |
| T-01-05 | Repudiation | Loss of rollback path if extraction breaks the site | mitigate | Git tag `pre-extraction-baseline` created in Task 1. `git checkout pre-extraction-baseline -- index.html` restores the original 8.5MB file in one command. |
| T-01-06 | Spoofing | Malicious script masquerading as the extractor | accept | Single-developer project, no shared CI yet, source is in-repo. Reviewable before execution. Re-evaluate if the project adds external contributors. |
| T-01-07 | Elevation of Privilege | Script reading or writing outside repo | mitigate | Only `pathlib.Path` joins relative to the input file's directory are used; the script does not accept absolute paths from user-controlled fields. Output paths constructed as `Path("media") / filename` where `filename` comes from the script's own hard-coded mapping table, not the input HTML. |
</threat_model>

<verification>
At the end of this plan, the developer (or Plan 02's automation) should be able to:

1. `git rev-parse pre-extraction-baseline` → outputs a commit SHA.
2. `cat .gitignore | grep -q '\.DS_Store'` → exits 0.
3. `python3 scripts/extract_base64_images.py --dry-run index.html` → exits 0, prints a 14-entry JSON report on stdout, leaves `index.html` unchanged, leaves `media/` unchanged (no new files).
4. `wc -c index.html` still reports `8940016`.

If all four checks pass, Plan 02 is safe to execute.
</verification>

<success_criteria>
- `.gitignore` exists with `.DS_Store` and `index.html.new` entries.
- `pre-extraction-baseline` git tag exists at current HEAD.
- `scripts/extract_base64_images.py` exists, parses, and its dry-run path completes successfully against the real `index.html` producing the expected 14-filename mapping.
- No image files have been created in `media/` yet.
- `index.html` is byte-identical to its state at the start of this plan.
</success_criteria>

<output>
After completion, create `.planning/phases/01-image-extraction-baseline/01-01-SUMMARY.md` documenting:
- The exact filename of `.gitignore` and the entries added
- The commit SHA the `pre-extraction-baseline` tag points to
- The number of lines in `scripts/extract_base64_images.py`
- The JSON dry-run report from running the script (paste verbatim)
- Confirmation that `index.html` size is still `8940016` bytes
</output>
</content>
</invoke>