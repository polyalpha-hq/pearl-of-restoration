# Roadmap — Pearl of Restoration Investment Platform

**Project:** PEARL
**Milestone:** v1
**Defined:** 2026-05-13
**Granularity:** coarse (6 phases)
**Mode:** yolo

---

## Phases

- [x] **Phase 1: Image Extraction & Baseline** — Extract all base64 images to `media/` folder, bringing `index.html` from 8.5MB to ~50KB (completed 2026-05-13)
- [ ] **Phase 2: Hindi Locale** — Add HI to the existing EN/ES/PT-BR i18n engine with full translations
- [ ] **Phase 3: Token Sale Section** — Ship PEARL token section with price, supply, progress bar, Buy CTA, and tokenomics page
- [ ] **Phase 4: Revenue Participation Estimator** — Integrate existing dashboard HTML as investment calculator with scoped CSS
- [ ] **Phase 5: Facility Photo Feed** — Add construction feed section loading latest photo from CDN URL with 5-minute refresh
- [ ] **Phase 6: Referral Section** — Add 2-level referral payout explainer and personal link generator with clipboard copy

---

## Phase Details

### Phase 1: Image Extraction & Baseline
**Goal:** Extract all base64-encoded images from `index.html` to the `media/` folder, reducing file size from ~8.5MB to under 50KB so that all subsequent editing work is safe and fast.
**Mode:** mvp
**Requirements:** PERF-01, PERF-02
**Success Criteria** (what must be TRUE):
  1. Visitor's browser begins rendering the page within 2 seconds on a 10 Mbps connection (HTML under 200KB served from GitHub Pages)
  2. All four product blocks (Oil Regeneration, MWF, Activated Carbon, KDK) display their photos correctly — no broken images, no missing content
  3. A developer can open and edit `index.html` in a standard text editor without risk of accidentally corrupting base64 blobs
**Depends on:** Nothing (first phase — technical prerequisite for all subsequent phases)
**Plans:** 2/2 plans complete
  - [x] 01-01-PLAN.md — Build extraction tooling and safety net (.gitignore, git tag, extract_base64_images.py)
  - [x] 01-02-PLAN.md — Run extraction, swap index.html, verify visually (human checkpoint + commit)

### Phase 2: Hindi Locale
**Goal:** Add HI (Hindi) as the fourth language in the existing i18n engine so that all current and future content is authored once and published in all four locales simultaneously.
**Mode:** mvp
**Requirements:** I18N-01, I18N-02, I18N-03
**Success Criteria** (what must be TRUE):
  1. A visitor can click the HI button in the nav and the entire page — all existing sections — renders in Hindi without a page reload
  2. Switching between EN, ES, PT-BR, and HI produces complete translations with no untranslated English strings visible in any locale
  3. After selecting Hindi and closing or refreshing the browser, the page reloads in Hindi (localStorage persistence confirmed)
**Depends on:** Phase 1
**Plans:** TBD

### Phase 3: Token Sale Section
**Goal:** Publish the PEARL token sale section — token explainer, price per token, total supply, fundraising progress bar, Buy CTA routing to Telegram bot, and a tokenomics page framing the 15% revenue participation model as a compliant utility token.
**Mode:** mvp
**Requirements:** TOKEN-01, TOKEN-02, TOKEN-03
**Success Criteria** (what must be TRUE):
  1. A visitor scrolling the page sees the PEARL token section displaying: token name, price per token, total supply, and a visual fundraising progress bar showing current raise against the $24.75M target
  2. Clicking "Buy PEARL" opens the Telegram bot purchase link (`t.me/BOTNAME?start=buy`) — no on-site transaction occurs
  3. The tokenomics page explains the 15% annual revenue participation model using "utility token" and "revenue participation" language exclusively — no phrase "investment return", "profit", or "guaranteed" appears in any locale
  4. All token section text is translated and renders correctly in all four locales (EN, ES, PT-BR, HI)
**Depends on:** Phase 2
**Blocked on:** TOKEN-03 content must pass a legal review gate before the tokenomics page is published
**Plans:** TBD
**UI hint**: yes

### Phase 4: Revenue Participation Estimator
**Goal:** Integrate the existing dashboard HTML file as an investment calculator embedded in the site, with CSS scoped under `.pearl-calc` to prevent style collision, and a mandatory "estimated, not guaranteed" disclaimer visible at all times.
**Mode:** mvp
**Requirements:** CALC-01, CALC-02
**Success Criteria** (what must be TRUE):
  1. A visitor enters a USD amount and immediately sees: the number of PEARL tokens that amount buys, the resulting annual revenue share percentage, and the estimated annual USDT payout at projected revenue
  2. The disclaimer "Estimated, not guaranteed. Past revenue does not predict future distributions." (or locale equivalent) is visible at all times — it cannot be dismissed or scrolled past without being read
  3. The calculator's visual style matches the existing dashboard design exactly — no layout breakage from style collision with the parent page
**Depends on:** Phase 2
**Blocked on:** Dashboard HTML file must be provided by project owner before implementation begins
**Plans:** TBD
**UI hint**: yes

### Phase 5: Facility Photo Feed
**Goal:** Add a facility construction feed section that displays the latest photo from the production site, loaded from an external HTTPS CDN URL and automatically refreshed every 5 minutes using a cache-busting query string.
**Mode:** mvp
**Requirements:** CAM-01, CAM-02
**Success Criteria** (what must be TRUE):
  1. A visitor sees a facility feed section with a photo of the production site — on first visit, either a real photo or a labeled placeholder image is shown (never a broken image icon)
  2. The photo is loaded via an `<img src="https://...">` tag pointing to an external HTTPS URL — no base64 data is embedded in `index.html` for this image
  3. If a visitor leaves the page open for 5 minutes, the photo refreshes automatically (cache-busting query string confirmed in browser network tab)
**Depends on:** Phase 1
**Blocked on:** CDN/server endpoint must be set up by the camera operator before a live photo URL can be substituted for the placeholder
**Plans:** TBD
**UI hint**: yes

### Phase 6: Referral Section
**Goal:** Add a referral program section explaining the 2-level USDT payout structure, allowing a visitor to enter their bot-assigned referral code and instantly generate and copy their personal `t.me/BOTNAME?start=REF_{CODE}` link.
**Mode:** mvp
**Requirements:** REF-01, REF-02, REF-03
**Success Criteria** (what must be TRUE):
  1. A visitor can read the referral program section and understand the 2-level payout structure from a visual diagram without needing to open the Telegram bot
  2. A visitor enters their bot-assigned referral code into the input field and sees their personal `t.me/BOTNAME?start=REF_{CODE}` link generated instantly in the browser — no server request required
  3. A visitor clicks the copy button and their referral link is copied to the clipboard; a visible confirmation (e.g., "Copied!") appears for at least 2 seconds
  4. The referral section text and diagram labels are translated and display correctly in all four locales (EN, ES, PT-BR, HI)
**Depends on:** Phase 2
**Blocked on:** Telegram bot owner must confirm that the `/mycode` command exists and that referral codes are assigned per-user before link format can be finalized
**Plans:** TBD
**UI hint**: yes

---

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Image Extraction & Baseline | 2/2 | Complete   | 2026-05-13 |
| 2. Hindi Locale | 0/? | Not started | - |
| 3. Token Sale Section | 0/? | Not started | - |
| 4. Revenue Participation Estimator | 0/? | Not started | - |
| 5. Facility Photo Feed | 0/? | Not started | - |
| 6. Referral Section | 0/? | Not started | - |

---

## Requirement Coverage

| Requirement | Phase | Status |
|-------------|-------|--------|
| PERF-01 | Phase 1 | Pending |
| PERF-02 | Phase 1 | Pending |
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

**Coverage:** 15/15 v1 requirements mapped. No orphans.

---

*Roadmap defined: 2026-05-13*
