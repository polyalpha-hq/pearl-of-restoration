# Technology Stack

**Project:** Pearl of Restoration — PEARL Token Investment Platform
**Researched:** 2026-05-13
**Mode:** Ecosystem — static HTML/JS/CSS expansion, no build system, GitHub Pages

---

## Baseline (Existing — Do Not Change)

| Layer | Technology | Version | Notes |
|-------|-----------|---------|-------|
| Markup | HTML5 | — | Single `index.html` file |
| Styling | CSS3 | — | Inline `<style>`, no preprocessor |
| Scripting | Vanilla JavaScript | ES2020+ | Inline `<script>`, no bundler |
| Fonts | Google Fonts CDN | — | Cinzel, Cinzel Decorative, EB Garamond |
| Icons | Font Awesome | 6.5.0 (current) | CDN + SRI integrity hash |
| QR Codes | qrcode.min.js | pinned local | Used in crypto donate modal |
| Contact Form | @formspree/ajax | 1.1.1 | CDN, deferred |
| Hosting | GitHub Pages | — | Static files only, no server execution |

**Confidence: HIGH** — Directly read from existing codebase STACK.md.

---

## New Features — Recommended Stack

### I18N-01 / I18N-02 / I18N-03: Multilingual (EN, ES, PT-BR, HI)

**Approach: Custom inline data-i18n attribute pattern — zero external dependencies.**

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Translation storage | Inline JS object literal per locale (`const TRANSLATIONS = { en: {...}, es: {...}, ... }`) | No fetch() needed, no CORS risk, works offline, no build step |
| DOM marking | `data-i18n="key"` attributes on all text nodes | Established pattern (vanilla-i18n, dom-i18n libraries all converge on this); negligible HTML overhead |
| Language switching | `querySelectorAll('[data-i18n]')` + `element.textContent = t[key]` | ~20 lines of JS, no library overhead |
| Persistence | `localStorage.setItem('lang', code)` on change; `localStorage.getItem('lang')` on load | Widely supported (Baseline 2015), survives page reload, works in GitHub Pages |
| Number/currency formatting | `Intl.NumberFormat(locale)` built-in browser API | Fully supported since 2019 in all major browsers; handles locale-specific decimal/thousands separators for the calculator output without dependencies |
| Plural rules | `Intl.PluralRules(locale)` built-in | Supported since 2019; handles Hindi and PT-BR plural edge cases correctly |
| Default locale | EN | Falls back to EN if localStorage is empty or locale is unrecognized |

**What NOT to use:**
- i18next, FormatJS, or react-intl: All require a build system or add 40–200KB. Overkill for 4 static locales.
- Fetching separate JSON files per locale: Introduces async complexity, CORS dependency, and race conditions on slow connections. With 4 locales and a single-file constraint, inline objects are cleaner.
- URL-based locale routing (e.g., `/es/index.html`): Requires multiple HTML files or server redirects — incompatible with single-file GitHub Pages constraint.

**Confidence: HIGH** — data-i18n pattern is the well-established community standard for no-framework static sites. `Intl.*` APIs confirmed widely available per MDN Baseline.

---

### TOKEN-02 / REF-02 / REF-03: Telegram Bot Deep Links

**Approach: Plain string construction — zero SDK required.**

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Deep link format | `https://t.me/{BOT_USERNAME}?start={PAYLOAD}` | Official Telegram specification. Opens private chat with bot, sends `/start PAYLOAD`. |
| Payload encoding | Base64url (`btoa(str).replace(/\+/g, '-').replace(/\//g, '_').replace(/=/g, '')`) for binary; plain alphanumeric for Telegram IDs | Allowed characters: A–Z, a–z, 0–9, `_`, `-`. Limit: 64 characters. |
| Referral code format | `REF_{TELEGRAM_USER_ID}` (e.g., `REF_123456789`) | Numeric Telegram IDs are stable, human-recognizable, and stay within 64-char limit. If compound data needed, use `{USER_ID}_{CAMPAIGN}` with base64url encoding. |
| Link display | `navigator.clipboard.writeText(url)` + visual confirmation | Clipboard API supported in all modern browsers; no library needed |
| Fallback | `<a href="...">` anchor tag | Always works when clipboard fails |

**What NOT to use:**
- TonConnect SDK (`@tonconnect/ui`, `@tonconnect/sdk`): These are for wallet connection and on-chain transaction signing in browser DApps. This project's purchase flow goes Telegram bot → bot handles TON. TonConnect in the browser adds 150KB+ bundle, requires a build system, and handles a flow this site never triggers. Confirmed out of scope in PROJECT.md.
- Telegram Mini App APIs: Only available when the page is loaded inside the Telegram client's webview. This site is an external web page.

**Confidence: HIGH** — Deep link format confirmed from official Telegram documentation (core.telegram.org/bots/features, core.telegram.org/api/links). Character set and 64-char limit confirmed from Telegram docs and aiogram library documentation.

---

### CALC-01 / CALC-02: Investment Calculator

**Approach: Vanilla JS, inline — integrate existing dashboard HTML directly.**

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Calculation engine | Vanilla JS arithmetic | No library needed for: `tokens = dollars / pricePerToken`, `annualPayout = tokens * revenueShare * totalRevenue / totalSupply` |
| Number formatting | `Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' })` and locale variants | Zero deps; handles locale-correct output for EN, ES, PT-BR, HI automatically |
| Input validation | HTML5 `type="number"` + `min` / `max` + JS range check | Sufficient for a marketing calculator; no form library needed |
| UI integration | Merge dashboard HTML into `index.html`; preserve existing CSS | Avoids iframe complexity; PROJECT.md states exact UI/logic must be preserved |

**What NOT to use:**
- Math.js or numeric.js: No need for complex math operations; plain JS arithmetic is faster, smaller, and more auditable.
- iframe embed of existing dashboard file: Creates i18n synchronization problem (can't translate inside iframe from parent), and adds a network request.

**Confidence: HIGH** — Pure vanilla JS investment calculators are a solved, dependency-free pattern. Intl.NumberFormat locale support confirmed.

---

### CAM-01 / CAM-02: Construction Feed Photo Refresh

**Approach: setInterval + Image src replacement with cache-busting query parameter.**

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Photo loading | `<img id="facility-cam">` with JS setting `src` | Most compatible; works without fetch/CORS |
| Cache busting | Append `?t={Date.now()}` to CDN URL on each refresh | Forces browser to request fresh copy; does not require CDN configuration |
| Refresh interval | 5–15 minutes (`setInterval`, configurable constant) | Matches the "periodic static refresh" requirement; avoids hammering CDN |
| Error handling | `img.onerror = () => img.src = FALLBACK_IMG` | Shows last known good photo if CDN is temporarily unavailable |
| CDN CORS | None required | Setting `img.src` directly does not trigger CORS; CORS only applies to `fetch()` / `XMLHttpRequest` |

**Important caveat:** Some CDNs (Cloudflare, Akamai) ignore query strings and serve cached content regardless. If the CDN chosen for camera photo upload ignores query strings, the solution is to have the camera uploader write to a predictable filename (e.g., `latest.jpg`) with `Cache-Control: no-cache, max-age=0` response headers on the CDN. In that case, the `?t=` parameter is still a safe belt-and-suspenders addition but the CDN header is the real solution.

**What NOT to use:**
- Service Worker with background sync: Overcomplicated for a marketing image refresh. Adds SW lifecycle management with no meaningful benefit.
- WebSocket or SSE: Requires a server. GitHub Pages is static-only.
- HLS / RTSP stream: Confirmed out of scope in PROJECT.md — no relay server available.

**Confidence: MEDIUM** — Pattern is well-established; caveat about CDN query string handling is real and depends on CDN choice (which is unknown at research time). Recommendation is sound but CDN selection may require testing.

---

### PERF-01 / PERF-02: Image Extraction (Base64 → media/ files)

**Approach: Manual extraction — no tooling required.**

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Extraction method | Copy base64 data URI value, decode to file, save to `media/` folder | One-time operation; no build tool justified |
| Replacement | `src="media/filename.jpg"` or `srcset` as appropriate | GitHub Pages serves files from `media/` directory natively |
| Verification | Check rendered output in browser before/after | No test framework needed for visual comparison |

**Constraint:** GitHub Pages repository source size limit is 1 GB (soft); published site limit is 1 GB. Current 8.5MB HTML is far under the limit, but the single-file approach is the bottleneck for performance (initial parse time). Post-extraction target of under 200KB HTML is achievable.

**Confidence: HIGH** — GitHub Pages limits confirmed from official GitHub Docs.

---

## Font Awesome Version Note

Font Awesome 7 was released in July 2025. The existing project uses 6.5.0. **Do not upgrade to v7 during this milestone.** FA7 drops jQuery and Less CSS support and changes the icon naming scheme — upgrading would require auditing all existing icon references. The 6.x line remains available on cdnjs and jsDelivr with full free-tier icon coverage. Pin to **6.6.x** (the latest 6.x maintenance release) only if a specific new icon is needed; otherwise keep 6.5.0 to avoid regressions.

**Confidence: MEDIUM** — FA7 release date confirmed (July 2025 per Wikipedia/Kickstarter). Breaking changes inferred from "drops jQuery and Less CSS, changes icon names" reports. Recommend verifying on docs.fontawesome.com before any version change.

---

## Complete Stack Summary

| Layer | Technology | Version | Confidence |
|-------|-----------|---------|------------|
| Markup | HTML5, single `index.html` | — | HIGH |
| Styling | CSS3 inline | — | HIGH |
| Scripting | Vanilla ES2020+ inline | — | HIGH |
| i18n | Custom data-i18n + inline JS objects | — (no lib) | HIGH |
| Number/date locale | `Intl.NumberFormat`, `Intl.PluralRules` | Browser built-in (Baseline 2019) | HIGH |
| Language persistence | `localStorage` | Browser built-in (Baseline 2015) | HIGH |
| Telegram deep links | Plain string: `t.me/BOT?start=CODE` | — (no lib) | HIGH |
| TON wallet | None — bot handles on-chain | — | HIGH |
| Investment calculator | Vanilla JS arithmetic + Intl formatting | — (no lib) | HIGH |
| Camera feed refresh | `setInterval` + `img.src` + `?t=Date.now()` | — (no lib) | MEDIUM |
| Icons | Font Awesome Free | 6.5.0 (existing) | HIGH |
| Contact form | Formspree ajax | 1.1.1 (existing) | HIGH |
| QR codes | qrcode.min.js | pinned local (existing) | HIGH |
| Hosting | GitHub Pages | — | HIGH |
| Build system | None | — | HIGH |

**Total new runtime dependencies added: 0.**

---

## Alternatives Considered and Rejected

| Category | Rejected | Reason |
|----------|----------|--------|
| i18n library | i18next, FormatJS, Polyglot.js | Require npm / build system; 40–200KB payload; unjustified for 4 locales |
| Wallet integration | TonConnect SDK | Handles browser-side wallet signing, which this project explicitly does not do; adds 150KB+ bundle |
| Calculator library | Math.js | No complex math needed; adds 170KB for zero benefit |
| Photo refresh | WebSocket, SSE, HLS | All require a persistent server connection — incompatible with GitHub Pages static hosting |
| Locale routing | Multi-file `/en/`, `/es/` structure | Requires multiple HTML files or server redirects; breaks single-file constraint |
| Font Awesome upgrade | FA 7.x | Breaking icon name changes; risks regressions in existing UI |

---

## GitHub Pages Constraints (Reference)

- No server-side code execution (no PHP, Node, Python)
- No configurable HTTP headers (cannot set CORS, CSP, Cache-Control from Pages config)
- Repository source: 1 GB soft limit
- Published site: 1 GB soft limit
- Bandwidth: 100 GB/month soft limit
- Builds: 10/hour soft limit (irrelevant — no build pipeline used)
- CORS for outbound fetch: GitHub Pages itself serves with `Access-Control-Allow-Origin: *`, but fetching external URLs is subject to the external server's CORS policy
- Commercial use: GitHub Pages acceptable use policy discourages e-commerce; PEARL site is a marketing/informational funnel, not a transaction processor (bot handles transactions)

---

## Sources

- Telegram deep link spec: https://core.telegram.org/bots/features (Telegram official docs)
- Telegram deep link API reference: https://core.telegram.org/api/links (Telegram official docs)
- TON Connect overview: https://docs.ton.org/ecosystem/ton-connect/overview (TON official docs)
- GitHub Pages limits: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits (GitHub official docs)
- Intl.NumberFormat MDN: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat (MDN, authoritative)
- Intl.PluralRules MDN: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules (MDN, authoritative)
- data-i18n pattern: https://andreasremdt.com/blog/building-a-super-small-and-simple-i18n-script-in-javascript/ (MEDIUM confidence — community article, consistent with multiple other sources)
- Font Awesome versions: https://fontawesome.com/versions + https://en.wikipedia.org/wiki/Font_Awesome
- Cache busting with query params: https://www.keycdn.com/support/what-is-cache-busting (MEDIUM confidence — CDN vendor documentation)
