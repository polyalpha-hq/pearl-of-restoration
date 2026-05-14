---
gsd_state_version: 1.0
milestone: v1.0
milestone_name: milestone
status: ready_to_plan
last_updated: "2026-05-14T00:00:00.000Z"
progress:
  total_phases: 6
  completed_phases: 2
  total_plans: 4
  completed_plans: 4
  percent: 33
---

# Project State — Pearl of Restoration

## Status

Phase 2 Complete — Ready to plan Phase 3 (Token Sale Section)

## Project Reference

See: .planning/PROJECT.md (updated 2026-05-13)

**Core value:** A prospective investor can understand the PEARL token opportunity and take action in under 60 seconds in their own language.
**Current focus:** Phase 3 — Token Sale Section

## Phases

| # | Name | Status | Plans |
|---|------|--------|-------|
| 1 | Image Extraction & Baseline | Complete | 2 |
| 2 | Hindi Locale | Complete | 2 |
| 3 | Token Sale Section | Not started | 0 |
| 4 | Revenue Participation Estimator | Not started | 0 |
| 5 | Facility Photo Feed | Not started | 0 |
| 6 | Referral Section | Not started | 0 |

## Performance Metrics

| Metric | Value |
|--------|-------|
| Phases total | 6 |
| Phases complete | 2 |
| Requirements mapped | 15/15 |
| Plans created | 4 |
| Plans complete | 4 |

## Accumulated Context

### Key Decisions

- Telegram bot is the only purchase backend — no on-site transactions
- Static 5-minute photo refresh instead of live RTSP stream (no relay server)
- No TonConnect SDK for v1 — bot handles all on-chain logic
- GitHub Pages static deployment — no server-side execution
- PEARL positioned as utility token (revenue participation), never investment instrument

### External Blockers

- Phase 3 (Token Sale): TOKEN-03 tokenomics content requires legal review before publish
- Phase 4 (Calculator): Dashboard HTML file must be provided by project owner
- Phase 5 (Photo Feed): CDN/server endpoint must be set up by camera operator
- Phase 6 (Referral): Telegram bot owner must confirm `/mycode` command exists

### Content Rules (Never Violate)

- Never mention Russia, Russian origin, GOST, or Russian company names in any user-visible text
- Never use "investment return", "profit", or "guaranteed" in token/calculator content
- All buy/referral actions must route through Telegram bot — no website backend

### Technical Notes

- `index.html` is currently ~8.5MB due to 14+ base64-encoded images
- Phase 1 is a hard prerequisite — editing the 8.5MB file risks accidental base64 corruption
- After Phase 1, file should be under 50KB HTML with images in `media/` folder
- CSS for calculator must be scoped under `.pearl-calc` to prevent collision

## Session Continuity

**Next action:** Run `/gsd-discuss-phase 3` to discuss Phase 3 (Token Sale Section) before planning.

**Phase 3 entry condition:** Phase 2 complete. External blocker: TOKEN-03 content requires legal review before tokenomics page is published.

---

## Last Activity

2026-05-14 — Phase 2 complete: Hindi locale live — 122-key hi:{} block + HI nav button; all locales verified. CR-01 content policy fix applied (removed molasses/sugar factory reference from rm_block3_inner).
