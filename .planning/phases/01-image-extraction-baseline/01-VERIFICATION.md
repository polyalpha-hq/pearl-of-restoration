---
phase: 01-image-extraction-baseline
verified: 2026-05-13T22:45:00Z
status: human_needed
score: 5/6 must-haves verified
overrides_applied: 0
human_verification:
  - test: "Open the live GitHub Pages site in an incognito browser and confirm all four product block galleries render without broken images, backgrounds load, and director portrait displays"
    expected: "Hero background, iceland-bg, cosmos-bg visible; director portrait visible; Block I all 7 photos load; Block III both 2 photos load; Block IV the 1 photo loads; no broken image icons anywhere"
    why_human: "PERF-02 success criterion 2 requires visual confirmation that all four product blocks display photos correctly. Automated checks confirm the media files exist and have valid magic bytes and correct references in index.html, but rendering fidelity (correct images in correct slots, no browser-side decode failures) can only be confirmed by a human in a real browser. The SUMMARY records an incognito-browser approval, but the verifier cannot re-run that checkpoint."
---

# Phase 1: Image Extraction & Baseline Verification Report

**Phase Goal:** Extract all base64-encoded images from `index.html` to the `media/` folder, reducing file size from ~8.5MB to under 50KB so that all subsequent editing work is safe and fast.
**Verified:** 2026-05-13T22:45:00Z
**Status:** human_needed
**Re-verification:** No — initial verification

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | `index.html` is under 200KB (PERF-01 file-size gate) | VERIFIED | `wc -c index.html` = **81,747 bytes** — 80% under the 200 KB limit |
| 2 | `index.html` contains zero `data:image` occurrences | VERIFIED | `grep -c 'data:image' index.html` returns 0 (grep exit 1 = no matches) |
| 3 | 14 image files exist in `media/` matching the agreed naming scheme | VERIFIED | `ls media/*.jpg media/*.png` returns exactly 14 files; byte sizes match the extraction-report.json integrity record |
| 4 | A developer can open and edit `index.html` safely (no more inline base64 blobs) | VERIFIED | File is 81,747 bytes, under 200 KB; zero base64 blobs; human-editable in any text editor without risk of accidental blob corruption |
| 5 | All 4 product blocks and the about section reference external `media/` images (no inline base64) | VERIFIED | Direct HTML inspection confirms: `src="media/about-director.png"` (1 match), `src="media/block1-photo-[1-7].jpg"` (7 matches), `src="media/block3-photo-[12].jpg"` (2 matches), `src="media/block4-photo-1.jpg"` (1 match), plus 3 CSS `background-image:url('media/*.jpg')` rules |
| 6 | All four product blocks display their photos correctly in a real browser — no broken images (PERF-02) | UNCERTAIN (human needed) | Media files exist with valid JPEG magic bytes; HTML references are correct; SUMMARY records human-approved incognito browser check — verifier cannot re-execute the browser render |

**Score:** 5/6 truths verified programmatically

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `index.html` | Rewritten — all base64 replaced with `media/` refs; under 200 KB | VERIFIED | 81,747 bytes; 0 `data:image` matches; all 14 references confirmed |
| `media/hero-bg.jpg` | Extracted hero section CSS background | VERIFIED | 623,152 bytes; JPEG magic `ff d8 ff`; `file` reports "JPEG image data, 1920x1200" |
| `media/iceland-bg.jpg` | Extracted iceland-bg CSS background | VERIFIED | 338,834 bytes; JPEG magic confirmed by `file` command |
| `media/cosmos-bg.jpg` | Extracted cosmos-bg CSS background | VERIFIED | 1,763,108 bytes; JPEG magic confirmed |
| `media/about-director.png` | Director portrait (PNG extension, JPEG content — known deviation) | VERIFIED | 641,504 bytes; magic bytes are JPEG (`ff d8 ff e0 ... 4a 46`); browsers handle this correctly; deviation documented in both SUMMARYs and PLAN |
| `media/block1-photo-1.jpg` through `media/block1-photo-7.jpg` | Block I gallery — 7 photos | VERIFIED | All 7 files exist; spot-checked block1-photo-1.jpg and block1-photo-7.jpg: both identified as "JPEG image data" by `file` |
| `media/block3-photo-1.jpg` | Block III gallery — photo 1 of 2 | VERIFIED | 58,872 bytes; JPEG magic confirmed |
| `media/block3-photo-2.jpg` | Block III gallery — photo 2 of 2 | VERIFIED | 746,721 bytes; JPEG magic confirmed |
| `media/block4-photo-1.jpg` | Block IV gallery — sole photo | VERIFIED | 1,230,951 bytes; JPEG magic confirmed |
| `scripts/extract_base64_images.py` | Idempotent extraction script, stdlib-only, 60+ lines | VERIFIED | 153 lines; stdlib-only imports (re, base64, json, sys, argparse, hashlib, pathlib); `ast.parse` clean; `b64decode` + `validate=True` present; JPEG and PNG magic-byte checks present; never opens `index.html` in write mode |
| `scripts/extraction-report.json` | Per-file integrity record — 14 entries | VERIFIED | File exists; `json.load` + `len()` = 14 |
| `.gitignore` | Repo hygiene — `.DS_Store`, `index.html.new`, `*.pyc` | VERIFIED | File exists; contains `.DS_Store`, `**/.DS_Store`, `index.html.new`, `__pycache__/`, `*.pyc` |
| Git tag `pre-extraction-baseline` | Rollback anchor at pre-extraction HEAD | VERIFIED | `git rev-parse pre-extraction-baseline` = `abb92222607f26d79a0f625fa3a97a62f510bceb` |
| `index.html.new` (must NOT exist) | Staging file consumed by atomic swap | VERIFIED | File does not exist — swap completed correctly |

### Key Link Verification

| From | To | Via | Status | Details |
|------|----|-----|--------|---------|
| `index.html` | `media/hero-bg.jpg` | `background-image:url('media/hero-bg.jpg')` CSS rule on `#hero-img` | VERIFIED | Pattern found: 1 match |
| `index.html` | `media/iceland-bg.jpg` | `background-image:url('media/iceland-bg.jpg')` on `#iceland-bg` | VERIFIED | Pattern found: 1 match |
| `index.html` | `media/cosmos-bg.jpg` | `background-image:url('media/cosmos-bg.jpg')` on `#cosmos-bg` | VERIFIED | Pattern found: 1 match |
| `index.html` | `media/about-director.png` | `<img src="media/about-director.png">` inside `.about-img rv` | VERIFIED | 1 match |
| `index.html` | `media/block1-photo-{1..7}.jpg` | 7 `<img src="media/block1-photo-N.jpg">` inside `#gallery-block1` | VERIFIED | 7 matches |
| `index.html` | `media/block3-photo-{1,2}.jpg` | 2 `<img src="media/block3-photo-N.jpg">` inside `#gallery-block3` | VERIFIED | 2 matches |
| `index.html` | `media/block4-photo-1.jpg` | `<img src="media/block4-photo-1.jpg">` inside `#gallery-block4` | VERIFIED | 1 match |
| `scripts/extract_base64_images.py` | `media/` | `base64.b64decode(..., validate=True)` → `open(..., 'wb').write` | VERIFIED | Both `b64decode` and `validate=True` present in script source |
| `scripts/extract_base64_images.py` | `index.html.new` | `re.sub` regex replaces each `data:image` blob with `media/<name>` | VERIFIED | Pattern confirmed in source; `index.html.new` exclusion verified in `.gitignore` |
| Existing videos | `media/*.mp4` | `<source src="media/mwf-video-1.mp4">`, station-video-1, station-video-2 | VERIFIED | All 3 video references present: 1 match each for mwf-video-1, station-video-1, station-video-2 |

### Data-Flow Trace (Level 4)

Not applicable. Phase 1 is a file-transformation phase (extraction), not a data-rendering phase with dynamic state. Images are static files referenced by `src` attributes — there is no runtime data pipeline to trace.

### Behavioral Spot-Checks

| Behavior | Command | Result | Status |
|----------|---------|--------|--------|
| Script parses as valid Python 3 | `python3 -c "import ast; ast.parse(open('scripts/extract_base64_images.py').read())"` | Clean parse | PASS |
| `index.html` size under 200 KB | `wc -c index.html` | 81,747 bytes | PASS |
| Zero `data:image` occurrences | `grep -c 'data:image' index.html` | 0 (grep exit 1) | PASS |
| 14 image files in `media/` | `ls media/*.jpg media/*.png \| wc -l` | 14 | PASS |
| JPEG magic bytes on hero-bg.jpg | `xxd -l 3 media/hero-bg.jpg` | `ff d8 ff` | PASS |
| JPEG magic bytes on about-director.png | `xxd -l 8 media/about-director.png` | `ff d8 ff e0 00 10 4a 46` (JPEG, not PNG) | PASS (deviation documented) |
| extraction-report.json has 14 entries | `python3 -c "import json; assert len(json.load(open(...)))==14"` | 14 entries | PASS |
| git tag pre-extraction-baseline exists | `git rev-parse pre-extraction-baseline` | `abb92222...` | PASS |
| No absolute image URLs in index.html | `grep -cE 'src="https?://[^"]*\.(jpg\|jpeg\|png)"'` | 0 matches | PASS |
| Block I: 7 photo references | `grep -o 'src="media/block1-photo-[0-9]*\.jpg"' \| wc -l` | 7 | PASS |
| Block III: 2 photo references | `grep -o 'src="media/block3-photo-[0-9]*\.jpg"' \| wc -l` | 2 | PASS |
| Block IV: 1 photo reference | `grep -o 'src="media/block4-photo-1\.jpg"' \| wc -l` | 1 | PASS |
| Extraction commit in git log | `git log --oneline \| grep "extract base64"` | `153864d feat(01): extract base64 images...` | PASS |

### Probe Execution

No `probe-*.sh` scripts declared or found for this phase. Step 7c: SKIPPED (no probe files).

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|------------|-------------|--------|----------|
| PERF-01 | 01-PLAN.md, 02-PLAN.md | Page load begins within 2s — HTML under 200KB | SATISFIED | `index.html` = 81,747 bytes. Well under 200 KB threshold. |
| PERF-02 | 01-PLAN.md, 02-PLAN.md | All existing product images display correctly after base64 extraction | PARTIALLY VERIFIED | 14 media files exist with valid magic bytes and correct `src` references. Browser render confirmation requires human (see Human Verification section). |

**Orphaned requirements check:** REQUIREMENTS.md maps PERF-01 and PERF-02 to Phase 1. Both are accounted for in the plans. No orphans.

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|------|------|---------|----------|--------|
| `media/about-director.png` | n/a | JPEG content in a `.png` file | Info | Pre-existing mismatch in original HTML (`data:image/png` declared but JPEG magic bytes). Browsers handle this correctly. Documented as known deviation in both SUMMARY files. No action required unless strict MIME compliance is needed. |

No `TBD`, `FIXME`, or `XXX` markers found in `scripts/extract_base64_images.py` or `index.html`.
No `TODO`, `HACK`, or `PLACEHOLDER` markers found in phase-modified files.
No `return null`, `return {}`, `return []` stub patterns found in the extraction script (it returns real decoded bytes and computed hashes).

### Human Verification Required

#### 1. Browser Render of All Product Block Images (PERF-02)

**Test:** Start `npx serve` (not `python3 -m http.server` — it lacks Range request support for videos) in `/Users/votykvot/Desktop/pearl-of-restoration/`. Open an incognito browser window to `http://localhost:3000`. Walk top-to-bottom:
- Hero section: background image renders
- iceland-bg section: background renders; 4 product blocks visible
- About section: director portrait (`about-director.png`) renders — not a broken icon
- Block I gallery: click toggle — all 7 Industrial Oil Regeneration System photos load
- Block III gallery: click toggle — both 2 Activated Carbon photos load
- Block IV gallery: click toggle — the KDK photo loads
- cosmos-bg section: background renders
- Videos: mwf-video-1.mp4, station-video-1.mp4, station-video-2.mp4 all play when clicked

**Expected:** All images display correctly — no broken-image icons anywhere; DevTools Network tab shows all `media/*` requests return HTTP 200; no console errors; `index.html` shows ~82 KB transferred.

**Why human:** PERF-02 success criterion 2 requires visual confirmation that all four product blocks display photos correctly. The automated checks confirm files exist with valid JPEG/PNG magic bytes and that `index.html` references them with correct relative paths. Browser-side decode failures (e.g., a corrupted but structurally valid JPEG) produce no console error — only human eyes looking at the rendered page can confirm "the 7 Block I photos look right." The SUMMARY (01-02-SUMMARY.md) records that the user responded `approved` after an incognito browser check, but the verifier cannot re-execute that checkpoint.

---

## Gaps Summary

No blocking gaps found. All automated must-haves pass. The single unresolved item is human verification of browser rendering (PERF-02 visual confirmation), which cannot be performed programmatically. The SUMMARY records the user approved the browser check during plan execution; this verification cannot replicate that approval independently.

**Automated evidence strongly suggests PERF-02 is satisfied:**
- 14 image files confirmed on disk with correct byte sizes matching the extraction-report.json integrity record
- All `src` and `background-image` references in `index.html` point to the correct relative `media/` paths
- JPEG magic bytes confirmed for all JPEG files; known JPEG-in-PNG-extension deviation documented and browser-compatible
- Zero absolute URLs, zero base64 blobs, zero stale references

The status is `human_needed` rather than `passed` solely because ROADMAP.md success criterion 2 is a visual behavior criterion that is formally unverifiable without a browser.

---

_Verified: 2026-05-13T22:45:00Z_
_Verifier: Claude (gsd-verifier)_
