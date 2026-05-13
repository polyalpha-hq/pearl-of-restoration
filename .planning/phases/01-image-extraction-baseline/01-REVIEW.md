---
phase: 01-image-extraction-baseline
reviewed: 2026-05-13T00:00:00Z
depth: standard
files_reviewed: 3
files_reviewed_list:
  - scripts/extract_base64_images.py
  - index.html
  - .gitignore
findings:
  critical: 2
  warning: 3
  info: 2
  total: 7
status: issues_found
---

# Phase 1: Code Review Report

**Reviewed:** 2026-05-13
**Depth:** standard
**Files Reviewed:** 3
**Status:** issues_found

## Summary

Three files were reviewed: the base64 extraction script, the rewritten `index.html`, and `.gitignore`. The extraction script is structurally sound — it performs safe file writes, validates magic bytes, reverses replacements in correct order, and never overwrites the source file. The `.gitignore` handles OS artifacts and the temporary `.new` output file correctly.

Two blockers were found in `index.html`: a missing lightbox DOM element causes a guaranteed null-pointer crash on every gallery image click, and a backslash corruption in the footer renders literal `\` characters in the published page. Three warnings cover a missing clipboard error handler, a render-blocking script in `<head>`, and a generated artifact not excluded from version control.

---

## Critical Issues

### CR-01: Lightbox DOM elements missing — null crash on every gallery image click

**File:** `index.html:832-839`
**Issue:** `openLightbox()` and `closeLightbox()` both call `document.getElementById('lightbox')` and immediately access `.style.display` or `.src` on the result. No element with `id="lightbox"` or `id="lightbox-img"` exists anywhere in the HTML. Every click on any gallery image (lines 488–494, 508–509, 514) triggers `openLightbox(this.src)`, which throws `TypeError: Cannot set properties of null (reading 'display')`. The Escape key handler at line 840 also throws on `null`. The gallery image zoom-in cursor hint (`cursor:zoom-in` at line 233) promises a working lightbox to users who receive only a broken experience.

**Fix:** Add a lightbox overlay before the closing `</body>` tag:
```html
<div id="lightbox" style="display:none;position:fixed;inset:0;z-index:99999;background:rgba(0,0,0,0.92);align-items:center;justify-content:center;cursor:zoom-out;" onclick="closeLightbox()">
  <img id="lightbox-img" src="" alt="" style="max-width:92vw;max-height:92vh;object-fit:contain;border:1px solid rgba(201,168,76,0.3);">
</div>
```
And update `openLightbox` to set `display:flex`:
```js
function openLightbox(src){
  var lb=document.getElementById('lightbox');
  document.getElementById('lightbox-img').src=src;
  lb.style.display='flex';
}
```

---

### CR-02: Backslash corruption renders visible in footer legal text

**File:** `index.html:704`
**Issue:** The footer legal line contains literal backslash-escaped HTML entities:
```html
<span data-i18n="ft_legal">WIPO Patented Technology \&nbsp;\&middot;\&nbsp; Closed-Loop Resource Recovery</span>
```
Browsers render `\&nbsp;` as `\` followed by a non-breaking space — the backslash is not an escape character in HTML. The visible output on screen will be `WIPO Patented Technology \ · \ Closed-Loop Resource Recovery` with two stray backslash characters. This is a content defect visible to every visitor in the current deployed state.

**Fix:** Remove the backslashes:
```html
<span data-i18n="ft_legal">WIPO Patented Technology &nbsp;&middot;&nbsp; Closed-Loop Resource Recovery</span>
```

---

## Warnings

### WR-01: `navigator.clipboard.writeText()` failure is silently swallowed

**File:** `index.html:791-795`
**Issue:** The `copyAddr` function calls `navigator.clipboard.writeText(addrs[type]).then(...)` with no `.catch()` handler. On some mobile browsers or when clipboard permission is denied, the returned Promise rejects. With no rejection handler, the user sees no feedback at all — the "Copied" confirmation never appears, and the unhandled rejection may emit a console error. For a page whose primary call to action is donating crypto by copying a wallet address, silent copy failure is a meaningful UX breakage.

**Fix:**
```js
function copyAddr(type){
  navigator.clipboard.writeText(addrs[type]).then(()=>{
    const el=document.getElementById('confirm-'+type);
    el.textContent=((i18n[currentLang]||i18n.en).copied||'✓ Copied to clipboard');
    setTimeout(()=>el.textContent='',2500);
  }).catch(()=>{
    const el=document.getElementById('confirm-'+type);
    el.textContent='Copy failed — please copy manually';
    setTimeout(()=>el.textContent='',3000);
  });
}
```

---

### WR-02: `qrcode.min.js` loaded as render-blocking synchronous script in `<head>`

**File:** `index.html:9`
**Issue:** `<script src="qrcode.min.js"></script>` in `<head>` without `defer` or `async` blocks HTML parsing until the file is downloaded and executed. The QR code library is only used inside modal dialogs that open on user interaction — there is no need for it to be available before the page renders. On a slow connection this delays first contentful paint.

**Fix:**
```html
<script src="qrcode.min.js" defer></script>
```

---

### WR-03: `scripts/extraction-report.json` generated artifact not excluded from version control

**File:** `.gitignore:1-7`
**Issue:** The extraction script writes `scripts/extraction-report.json` (line 146 of the Python script) containing image filenames, byte counts, sha256 hashes, and approximate source line numbers. This file is not listed in `.gitignore` and is already present in the repository (`/scripts/extraction-report.json` exists on disk). Generated artifacts should not be checked in unless they are intentionally versioned; this one will appear as an unexpected diff in every re-run of the script.

**Fix:** Add to `.gitignore`:
```
scripts/extraction-report.json
```

---

## Info

### IN-01: CSS regex pattern in extraction script does not match double-quoted `url()` forms

**File:** `scripts/extract_base64_images.py:40-44`
**Issue:** The CSS branch of `PATTERN` matches only single-quoted `url('data:image/…')` but not double-quoted `url("data:image/…")` or unquoted `url(data:image/…)` forms. The current HTML only uses single-quote form, so this works for this specific input. However, the docstring says the regex covers "both CSS url() and HTML src="" forms" — the claim is slightly overstated. If a future HTML variant uses double-quoted or bare `url()` syntax, the script will silently under-count blobs and refuse to run (`EXPECTED_COUNT` mismatch), making the failure safe but confusing.

**Fix:** If broader resilience is desired, extend the CSS branch:
```python
r"background-image:url\(['\"]?data:image/(jpeg|jpg|png);base64,([A-Za-z0-9+/=]+)['\"]?\)"
```

---

### IN-02: `import json` is used only for side-effect output — `report` list printed twice

**File:** `scripts/extract_base64_images.py:135, 146`
**Issue:** `json.dumps(report, indent=2)` is called at line 135 (always, including dry-run, printed to stdout) and again at line 146 (written to `extraction-report.json` on disk). The JSON printed to stdout is mixed with the per-file `stderr` progress messages, making stdout non-machine-parseable in dry-run mode because stderr and stdout both flow to the terminal. In non-dry-run mode the on-disk report duplicates the stdout output exactly. This is a design inconsistency: either stdout is the machine output (keep it pure, suppress human-readable lines) or the report file is the output (suppress stdout JSON). Not a correctness bug but creates confusion for callers piping the output.

**Fix (minimal):** Separate machine output from human output explicitly in the docstring, or redirect the per-file progress lines to `stdout` with a prefix so callers can distinguish.

---

_Reviewed: 2026-05-13_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
