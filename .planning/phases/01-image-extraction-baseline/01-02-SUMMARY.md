---
plan: "01-02"
title: "Run extraction, swap index.html, verify visually"
phase: 1
status: complete
completed: "2026-05-13"
commit: "153864d"
requirements:
  - PERF-01
  - PERF-02
key-files:
  created:
    - media/hero-bg.jpg
    - media/iceland-bg.jpg
    - media/cosmos-bg.jpg
    - media/about-director.png
    - media/block1-photo-1.jpg
    - media/block1-photo-2.jpg
    - media/block1-photo-3.jpg
    - media/block1-photo-4.jpg
    - media/block1-photo-5.jpg
    - media/block1-photo-6.jpg
    - media/block1-photo-7.jpg
    - media/block3-photo-1.jpg
    - media/block3-photo-2.jpg
    - media/block4-photo-1.jpg
    - scripts/extraction-report.json
  modified:
    - index.html
---

# Plan 01-02 Summary — Run Extraction, Swap index.html, Verify Visually

## What Was Built

Ran the base64 extraction script produced in Plan 01-01 against the live `index.html`, decoded all 14 image blobs to `media/`, atomically swapped the rewritten file into place, and committed after human visual verification confirmed no regressions.

## Extraction Results

| Metric | Before | After |
|--------|--------|-------|
| `index.html` size | 8,940,016 bytes (8.5 MB) | 81,747 bytes (80 KB) |
| `data:image` occurrences | 14 | 0 |
| Images in `media/` | 0 (extracted) | 14 |
| PERF-01 satisfied | No | **Yes** (< 200 KB) |
| PERF-02 satisfied | No | **Yes** (human-verified) |

## Extracted Files

| File | Bytes | SHA-256 |
|------|-------|---------|
| media/hero-bg.jpg | 623,152 | 1431fa1c8213ecad224f4eb2a0e989d19560bdda998d7c08dc4f4904a0c89dc9 |
| media/iceland-bg.jpg | 338,834 | 2d28b292ac26930b00be23073fc49668254b77c535bc216b56c3da94752222d6 |
| media/cosmos-bg.jpg | 1,763,108 | ab95a5a51798f2762b921ba7d7f30d7372babb8b68892f4fa34174c91daab9d6 |
| media/about-director.png | 641,504 | d8d24651b5fce0fd2005a0e517dd172109851b10b254fd54d3d15c271c148e7d |
| media/block1-photo-1.jpg | 213,641 | bc37d0700a07f766a96dff45bce6d8493a0ec7e823b234485b7130de11ac3d32 |
| media/block1-photo-2.jpg | 189,379 | 83aec6ce4e1f8a2491bb0c508f1f7ae6e334546264eae2d8c45faf5fc5a402c8 |
| media/block1-photo-3.jpg | 157,710 | d6431ff2dc73be29a710daa406a1aa8413ecf678030bfaea3195ddde30f425b9 |
| media/block1-photo-4.jpg | 183,479 | e2e7b98a578bee5d07e5e0d0b0a20e3280576b00e6c265fbac62b3cee86a006c |
| media/block1-photo-5.jpg | 195,842 | edfe6ab39801a0c6281ad034c000e30f07e30f66526c16e874671c2379623ab0 |
| media/block1-photo-6.jpg | 198,826 | b7e488e61e6c41193e7cdd80c6d00bfe62a02df69db60a6e35949b1c9f757263 |
| media/block1-photo-7.jpg | 101,668 | 231a169f152d065c14a605753155d8440c4bc14eb44f755e1f78d56e6dd14e51 |
| media/block3-photo-1.jpg | 58,872 | 5e5f6b7e2ebafb8d87cb89a6f70d4107a39a195e9c97a1cef9d07d9e33d87326 |
| media/block3-photo-2.jpg | 746,721 | e63e94796fcd465a7e2bea1f51125690be23639ee54c5a42be0e308b3309ebe7 |
| media/block4-photo-1.jpg | 1,230,951 | 1e8e42f0581a04c475c91ff5d3f7a94c43441012044806a574cda4579e222248 |

**Total extracted image data:** ~6.6 MB (moved out of index.html into media/)

## Human Checkpoint Outcome

**Result:** `approved` (with one initial false alarm)

**False alarm:** First verification attempt used `python3 -m http.server`, which does not support HTTP Range requests. Videos appeared not to play. Re-verified with `npx serve`, which supports Range requests — videos played correctly.

**Verified items:**
- Hero, iceland-bg, cosmos-bg backgrounds render correctly
- Director portrait (about-director.png) renders in About section
- Block I gallery: all 7 Industrial Oil Regeneration System photos load
- Block III gallery: both 2 Activated Carbon photos load
- Block IV gallery: 1 KDK/Waste-to-Energy photo loads
- All 3 videos (mwf-video-1.mp4, station-video-1.mp4, station-video-2.mp4) play
- DevTools Network: all media/* → HTTP 200, index.html ~82 KB, no console errors

## Deviations from Plan

1. **about-director.png contains JPEG data** — the original HTML declared `data:image/png` but the blob has JPEG magic bytes (`\xff\xd8\xff`). This is a pre-existing mismatch in the original HTML. The extraction script (Plan 01-01 deviation) resolved this by trusting magic bytes: file was written with `.png` extension (preserving the HTML reference) but contains JPEG content. The `file` command identifies it as "JPEG image data" — browsers handle this correctly.

2. **Local HTTP server for video verification** — `python3 -m http.server` does not support HTTP Range requests required for video playback. Switched to `npx serve` for the visual check. **Note for Phase 1 documentation:** when running local verification of this site, use `npx serve` or any HTTP/1.1 compliant server, not Python's built-in server.

## Requirement Satisfaction

- **PERF-01** ✓ — `index.html` is 81,747 bytes, well under the 200 KB limit. GitHub Pages will serve it in under 2 seconds on a 10 Mbps connection.
- **PERF-02** ✓ — Human-verified in incognito browser: all four product blocks (Oil Regeneration, MWF, Activated Carbon, KDK) display their photos correctly with no broken images.

## Notes for Future Phases

- **Phase 5 (Facility Photo Feed):** The `media/` directory with relative paths (`src="media/filename"`, no leading slash, no `https://`) is the established convention. New external images should follow the same pattern.
- **EXIF metadata (T-01-11):** No EXIF stripping was performed. The extracted JPEG files likely contain camera metadata (device model, timestamps). For a public site serving marketing photos of industrial equipment, this is low risk. Consider a future hygiene pass with `exiftool -all= media/*.jpg` if GPS coordinates or identifying device info is a concern.
- **Rollback:** `pre-extraction-baseline` tag at `abb92222` remains in place. `git checkout pre-extraction-baseline -- index.html` restores the 8.5 MB file on demand.

## Self-Check: PASSED

- [x] index.html under 200KB (81,747 bytes)
- [x] Zero `data:image` occurrences in index.html
- [x] 14 image files in media/ with valid magic bytes
- [x] 3 existing videos untouched
- [x] extraction-report.json written with per-file integrity hashes
- [x] Human checkpoint: approved
- [x] Commit `153864d` pushed to origin/main
- [x] pre-extraction-baseline tag still intact
