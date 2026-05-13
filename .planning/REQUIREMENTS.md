# Requirements: Pearl of Restoration — Investment Platform

**Defined:** 2026-05-13
**Core Value:** A prospective investor can understand the PEARL token opportunity and take action (buy tokens, refer friends) in under 60 seconds in their own language.

## v1 Requirements

### Performance

- [x] **PERF-01**: Page load begins within 2s — HTML under 200KB (images extracted to `media/` folder)
- [x] **PERF-02**: All existing product images (Oil Regeneration, MWF, Activated Carbon, KDK) display correctly after base64 extraction

### Multilingual

- [ ] **I18N-01**: User can switch between EN, ES, PT-BR, and HI via language buttons in the nav
- [ ] **I18N-02**: All visible text — including all new token/calculator/referral/feed sections — is translated in all 4 locales
- [ ] **I18N-03**: Selected language persists across page reloads (localStorage)

### Token Sale

- [ ] **TOKEN-01**: Token section displays PEARL token name, price per token, total supply, and current fundraising progress bar
- [ ] **TOKEN-02**: "Buy PEARL" button opens the Telegram bot purchase link (`t.me/BOTNAME?start=buy`)
- [ ] **TOKEN-03**: Tokenomics section explains the 15% annual revenue participation model with compliant "utility token" framing (not "investment returns")

### Investment Calculator

- [ ] **CALC-01**: Revenue Participation Estimator accepts a USD investment amount and displays: token count received, formula-based annual revenue share percentage, estimated USDT payout at projected revenue — with mandatory "estimated, not guaranteed" disclaimer
- [ ] **CALC-02**: Calculator UI/logic integrated from existing dashboard HTML file (CSS scoped under `.pearl-calc` wrapper to prevent style collision)

### Facility Feed

- [ ] **CAM-01**: Facility feed section displays the latest construction photo from the production site
- [ ] **CAM-02**: Photo is loaded from an external HTTPS CDN URL (no base64 inline); page refreshes the image every 5 minutes using cache-busting query string

### Referral Program

- [ ] **REF-01**: Referral program section explains the 2-level USDT payout structure with clear visual diagram
- [ ] **REF-02**: User can enter their bot-assigned referral code and the site generates their personal `t.me/BOTNAME?start=REF_{CODE}` link
- [ ] **REF-03**: User can copy their generated referral link to clipboard with one click

## v2 Requirements

### Token Analytics

- **ANLT-01**: Live token holder count pulled from TON contract
- **ANLT-02**: Fundraising progress bar updates automatically from on-chain data
- **ANLT-03**: Historical revenue distribution chart

### Advanced Calculator

- **CALC-03**: Multi-year ROI projection (3-year / 5-year scenarios)
- **CALC-04**: Compare PEARL against benchmark returns (treasury, S&P)

### Live Facility Feed

- **CAM-03**: Live RTSP stream via HLS relay (blocked on relay server infrastructure)

### SEO

- **SEO-01**: Separate locale HTML files for multilingual SEO (hreflang support)

## Out of Scope

| Feature | Reason |
|---------|--------|
| TonConnect SDK / browser wallet signing | Both buy paths redirect to Telegram bot; no on-chain signing in browser for v1 |
| Live RTSP/HLS camera stream | No relay server; static periodic photo is sufficient for trust signal |
| Custom backend or database | Telegram bot handles all purchase tracking and referral attribution |
| Countdown timers | Identified anti-feature — scam signal to savvy crypto investors |
| On-site KYC forms | False compliance theater; real KYC handled at purchase if required |
| Live token price ticker | Token not yet listed on exchanges; ticker would show stale/zero data |
| Russian geography, company names, GOST | International positioning — never expose origin jurisdiction |
| hreflang meta tags | Crawler does not execute JS language switch; broken hreflang is worse than none |
| Client-generated referral codes | Trivially forgeable from Telegram ID; codes must come from bot only |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| PERF-01 | Phase 1 | Complete |
| PERF-02 | Phase 1 | Complete |
| I18N-01 | Phase 2 | Pending |
| I18N-02 | Phase 2 | Pending |
| I18N-03 | Phase 2 | Pending |
| TOKEN-01 | Phase 3 | Pending |
| TOKEN-02 | Phase 3 | Pending |
| TOKEN-03 | Phase 3 | Pending |
| CALC-01 | Phase 4 | Pending |
| CALC-02 | Phase 4 | Pending |
| CAM-01 | Phase 5 | Pending |
| CAM-02 | Phase 5 | Pending |
| REF-01 | Phase 6 | Pending |
| REF-02 | Phase 6 | Pending |
| REF-03 | Phase 6 | Pending |

**Coverage:**
- v1 requirements: 15 total
- Mapped to phases: 15
- Unmapped: 0 ✓

---
*Requirements defined: 2026-05-13*
*Last updated: 2026-05-13 after initial definition*
