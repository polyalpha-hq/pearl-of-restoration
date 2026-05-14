---
phase: 02-hindi-locale
reviewed: 2026-05-14T00:00:00Z
depth: standard
files_reviewed: 1
files_reviewed_list:
  - index.html
findings:
  critical: 1
  warning: 3
  info: 2
  total: 6
status: issues_found
---

# Phase 02: Code Review Report

**Reviewed:** 2026-05-14
**Depth:** standard
**Files Reviewed:** 1
**Status:** issues_found

## Summary

The Phase 2 edit added a `hi:{}` locale object (122 keys) to `const i18n` and a HI language button to the nav `.lang-sw` div. The JS object parses without error, key counts match `en` exactly, and the nav button markup is structurally correct (`onclick`, `data-lang`, `class` all present).

However, four problems were found: one content policy violation that is a BLOCKER (the Hindi locale directly translates and exposes "molasses" and "sugar factories" in the expanded Block III panel — prohibited by CLAUDE.md), two warnings (the `<html lang>` attribute is never updated on language switch, causing accessibility and SEO failures for Hindi users; and the `hero_manifesto` Hindi text contains a mistranslation that inverts the intended meaning), and one additional warning about `impact_kg` omitting the localized connector word. Two informational items are also noted.

---

## Critical Issues

### CR-01: Content Policy Violation — Molasses and Sugar Factories Named in Hindi locale

**File:** `index.html:1117`
**Issue:** CLAUDE.md states explicitly: *"Never mention molasses, sugar plants, or specific feedstock sources."* The `hi.rm_block3_inner` value — set via `innerHTML` when Hindi is selected and the "Activated Carbon" read-more panel is expanded — contains the Hindi text `क्षीण शीरा` (depleted molasses) and `चीनी कारखाने` (sugar factories). This is a faithful translation of the English `rm_block3_inner` (line 889), which already violates the policy. Phase 2 introduces this violation into Hindi, expanding its exposure to a new audience.

The same violation already exists in `es` (line 965, "melaza agotada" / "fábricas azucareras") and `pt` (line 1041, "melaço esgotado" / "fábricas de açúcar"), so this is a systemic issue that Phase 2 perpetuated rather than originated — but each new locale is a fresh instance of the violation.

**Fix:** Replace the feedstock-specific language with the approved abstraction "organic industrial byproduct" across all four locales. For `hi`:

```javascript
// Current (line 1117):
rm_block3_inner:'...<br><br>कच्चा माल: क्षीण शीरा — एक औद्योगिक उप-उत्पाद जिसे चीनी कारखाने फेंकने के लिए भुगतान करते हैं।...'

// Fixed:
rm_block3_inner:'...<br><br>कच्चा माल: जैविक औद्योगिक उप-उत्पाद — जिसे प्रसंस्करण सुविधाएं फेंकने के लिए भुगतान करती हैं।...'
```

Apply corresponding changes to `en` (line 889), `es` (line 965), and `pt` (line 1041).

---

## Warnings

### WR-01: `<html lang>` Attribute Never Updated on Language Switch

**File:** `index.html:2` and `index.html:1152`
**Issue:** The `<html lang="en">` attribute is hardcoded and never updated by `setLang()`. When a user selects Hindi, the document language declaration remains `"en"`, which causes:
1. Screen readers to pronounce Hindi Devanagari text with English phonology — a significant accessibility failure.
2. Search engines to index Hindi content as English.
3. Browser auto-translation to offer to translate what is already translated.

This was not introduced by Phase 2 but Phase 2 makes it meaningfully worse: Hindi (script: Devanagari, direction: LTR) is especially impacted because it is phonologically and orthographically remote from English, and Devanagari requires correct `lang` declaration for proper font shaping and text-to-speech.

**Fix:** Add one line to `setLang()`:

```javascript
function setLang(lang){
  currentLang=lang;
  localStorage.setItem('pearl_lang',lang);
  document.documentElement.lang=lang; // ADD THIS LINE
  var t=i18n[lang]||i18n.en;
  // ... rest of function
```

### WR-02: `hero_manifesto` Hindi Mistranslation Inverts Meaning

**File:** `index.html:1075`
**Issue:** The English source reads:
> *"Closed-loop technology — not an idea. A working reality."*

The Hindi translation is:
> `बंद-लूप प्रौद्योगिकी — कोई विचार नहीं। एक कार्यशील वास्तविकता।`

`कोई विचार नहीं` literally means "no idea/thought at all" — as in "I have no idea" — rather than "not merely an idea." A Hindi reader will parse this as "Closed-loop technology — no idea. A working reality," which is incoherent or reads as self-deprecating ("we have no idea"). The intended meaning is that the technology is not a theoretical concept but a proven reality.

**Fix:**

```javascript
// Current:
'बंद-लूप प्रौद्योगिकी — कोई विचार नहीं। एक कार्यशील वास्तविकता।'

// Fixed:
'बंद-लूप प्रौद्योगिकी — केवल एक विचार नहीं, बल्कि एक कार्यशील वास्तविकता।'
// ("Not just an idea, but a working reality.")
```

### WR-03: `impact_kg` in Hindi Omits Unit Connector — Renders Grammatically Incomplete

**File:** `index.html:1146`
**Issue:** The donate amount widget renders text via:
```javascript
'$'+n+' = ~'+co2.toLocaleString()+(_ta.impact_kg||' kg of CO₂')
```

All other locales include a language-appropriate connector:
- `en`: `' kg of CO₂'` → "$10 = ~3,200 kg of CO₂"
- `es`: `' kg de CO₂'`
- `pt`: `' kg de CO₂'`
- `hi`: `' kg CO₂'` → "$10 = ~3,200 kg CO₂"

The Hindi value `' kg CO₂'` drops the unit connector entirely. While English speakers read "3,200 kg CO₂" as acceptable shorthand, Hindi text rendered without a unit relationship word (`का`, `की मात्रा में`) is stylistically inconsistent with the translated content around it. The output reads as an incomplete unit phrase next to fully-translated Hindi sentences.

**Fix:**

```javascript
// Current (line 1146):
impact_kg:' kg CO₂'

// Fixed:
impact_kg:' kg CO₂ की बचत'
// ("3,200 kg CO₂ saved" — consistent with the surrounding impact copy)
```

---

## Info

### IN-01: `hero_title` and `hero_sub` Are Dead Keys — No DOM Element Binds Them

**File:** `index.html:1074, 1076`
**Issue:** Both `hero_title` and `hero_sub` exist in all four locale objects (including `hi`) but no HTML element carries `data-i18n="hero_title"` or `data-i18n="hero_sub"`. The keys translate correctly and are valid JS, but they are never rendered. This is a pre-existing issue across all locales; Phase 2 faithfully replicated the dead keys into Hindi. These 2 keys per locale (8 total across en/es/pt/hi) waste space and can mislead maintainers.

**Fix:** Either add `data-i18n="hero_title"` to the appropriate heading element, or remove `hero_title` and `hero_sub` from all four locale objects if no binding is intended.

### IN-02: `<html lang="en">` Hardcoded — No `dir` Attribute Consideration

**File:** `index.html:2`
**Issue:** Hindi uses LTR script (Devanagari), so `dir` is not a concern here. However the hardcoded `lang="en"` means no `dir` management exists at all. If a future locale (Arabic, Urdu) is added to this same pattern, RTL text will break layout without any mechanism to update `dir`. The current implementation has no hook for this.

**Fix:** Noting for future locale work — add `document.documentElement.dir = (lang === 'ar') ? 'rtl' : 'ltr';` inside `setLang()` alongside the `lang` attribute fix from WR-01.

---

_Reviewed: 2026-05-14_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
