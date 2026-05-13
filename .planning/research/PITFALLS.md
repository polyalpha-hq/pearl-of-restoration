# Domain Pitfalls

**Domain:** Static HTML marketing site → multilingual crypto token investment platform (GitHub Pages, no backend)
**Researched:** 2026-05-13
**Project:** Pearl of Restoration / PEARL token (TON blockchain)

---

## Critical Pitfalls

These mistakes cause rewrites, legal exposure, or silent loss of investor trust.

---

### Pitfall 1: The Calculator Makes You a Securities Issuer

**What goes wrong:** Adding an investment calculator that shows "estimated annual payout" or "expected USDT income" is the single highest-risk action on this site. Under the Howey test, a token becomes a security when buyers have a "reasonable expectation of profits from the efforts of others." A calculator with fields labeled "your investment → your annual USDT return" is exhibit A in that argument — regardless of how many places the page says "utility token."

**Why it happens:** Developers treat the calculator as a UX feature. Legal teams treat it as a prospectus. The SEC has explicitly stated that websites, white papers, and calculators are scrutinized as marketing communications establishing profit expectations.

**Consequences:**
- Token classified as unregistered security in any jurisdiction that applies Howey or equivalent
- Platform takedown risk from GitHub (ToS violation) and payment processors
- Personal liability for the director (Andrey Baranovsky) named in the About section

**Prevention:**
- Label the calculator "Revenue Participation Estimator" not "Investment Calculator"
- Output field must say "Estimated participation share in production revenue (not guaranteed)" — never "your profit" or "your return"
- Add a mandatory disclaimer above the calculator: "Historical production data does not guarantee future distributions. This is not a financial instrument. Consult a qualified advisor."
- Never show annualized percentage return figures — only show token count and a raw formula explanation
- Do not show dollar amounts as outputs; show only the mathematical share ratio

**Detection:** Read your output labels aloud. If they sound like a brokerage prospectus, rewrite them.

**Phase:** CALC-01 / CALC-02 — must be reviewed before these features go live.

---

### Pitfall 2: Monolithic File Corruption During Refactoring

**What goes wrong:** The current `index.html` is 8.5MB with ~14 base64 image blobs inline. Any text editor operation on this file — find-and-replace, section cut/paste, adding i18n attributes — risks silently corrupting a base64 blob. A corrupted blob produces a broken image with no error in the browser console. Git diffs become unreadable because diffing a base64 blob is 200KB of character-level noise.

**Why it happens:** Base64 strings have no delimiter — they are just very long attribute values. A stray newline inside a `data:image/jpeg;base64,...` value will break the image silently. Text editors with line-length limits (VS Code default wrap, some terminal editors) can insert breaks automatically.

**Consequences:**
- Production images disappear after a deploy; discovered by a real user, not a test
- The existing gallery (7 photos in Block I) could silently drop images
- Git history becomes unauditable — you cannot diff what changed

**Prevention:**
- PERF-01 (extract images to `media/`) MUST be completed and verified before ANY i18n refactoring begins — this is a hard prerequisite
- After extraction, verify each `<img src="media/photo.jpg">` loads in a fresh browser tab before committing
- Use a dedicated script (not manual find-replace) for base64 extraction — the GitHub Gist pattern of regex-extract works; manual copy-paste does not
- Backup the current `index.html` as a git tag (`v6.1-baseline`) before starting extraction, not as a file on the Desktop

**Detection:** After any file edit, open the page in an incognito browser window (no cache) and visually check every image in all four product blocks and the Read More panels.

**Phase:** PERF-01 must complete before I18N-01 or TOKEN-01 work begins.

---

### Pitfall 3: i18n Attribute Spray Breaks Existing JS

**What goes wrong:** Adding `data-i18n="key"` attributes to elements and then calling `element.innerHTML = translation` overwrites any event listeners attached inline or via `addEventListener` on those elements. The existing site has JS that hides/shows panels by toggling `style="display:none"` on elements. If those elements also receive `data-i18n` updates that rewrite `innerHTML`, child elements with listeners get cloned without their events.

**Why it happens:** The `innerHTML` setter tears down and rebuilds the DOM subtree. Any event listeners added via `addEventListener` on child elements are lost. The existing code uses inline handlers (`onclick`) in some places (safe) and `addEventListener` in others (lost after innerHTML replacement).

**Consequences:**
- Tab buttons stop working after language switch
- Read More panels stop toggling
- QR modal open/close breaks in some languages but not others (depending on which language was active at page load)

**Prevention:**
- Use `textContent` for plain text translation targets, not `innerHTML`
- For elements that contain child nodes with event listeners (the tab buttons, panel toggles, modal triggers), never translate the parent — translate only leaf text nodes by wrapping text in `<span data-i18n="key">text</span>` inside the interactive element
- Before writing the i18n engine, map all `addEventListener` calls in the existing 4 script blocks and mark those elements as "translate-children-only" targets
- Translate `placeholder`, `alt`, `title`, `aria-label` via `data-i18n-attr="placeholder:key"` pattern, not innerHTML

**Detection:** After every language switch, test: tab switching, all four Read More panel toggles, QR modal open/close, CO2 counter.

**Phase:** I18N-01 / I18N-02 — architecture decision must be made before implementation starts.

---

### Pitfall 4: hreflang on a Single-URL SPA Is Invisible to Google

**What goes wrong:** The site is a single `index.html` at a single URL. Google cannot crawl `/es/`, `/pt-br/`, or `/hi/` because they do not exist. Adding `<link rel="alternate" hreflang="es" href="https://polyalpha-hq.github.io/pearl-of-restoration/?lang=es">` in the `<head>` will be ignored by Google's crawler because the crawler will not execute JavaScript to apply the language switch — it sees only the default English content regardless of what the URL query string says.

**Why it happens:** Developers assume query params or hash routing creates separate crawlable pages. Google's documentation explicitly states hreflang alternate URLs must return the actual localized content, not a JS-transformed version of the same page.

**Consequences:**
- Zero SEO benefit from multilingual work — all four language versions compete on the same URL with the same English content
- Hindi and Portuguese-speaking investors searching in their language will not find the site

**Prevention — Two valid options for GitHub Pages:**

Option A (No build system): Create separate HTML files per locale: `es/index.html`, `pt-br/index.html`, `hi/index.html`, each with hard-coded translated content. Each file has correct `hreflang` pointing to all others. This is the only approach that works without a build system.

Option B (Acceptable SEO tradeoff): Accept that multilingual support is for user experience only, not SEO. Do not add hreflang tags at all — incorrect hreflang is worse than no hreflang (Google ignores broken implementations). Focus SEO on English only.

**Do not do:** Add hreflang to a single-URL JS-switched site and assume it works.

**Detection:** Use Google Search Console after deploy. If all crawled pages are `index.html` with English content regardless of `?lang=` parameter, hreflang is not being honored.

**Phase:** I18N-03 — decision must be explicit in the roadmap before implementation.

---

### Pitfall 5: Client-Side Referral Codes Are Trivially Forgeable

**What goes wrong:** Generating a referral link like `t.me/BOTNAME?start=REF_CODE` in the browser from a user-entered Telegram ID means any user can type any string into the input field and generate a link claiming to be someone else's referral. The Telegram bot receives the `start` parameter and attributes a purchase to whatever code was passed — which the buyer could have fabricated to steal another user's referral credit, or to avoid attributing to anyone.

**Why it happens:** The static site has no way to validate that a Telegram ID entered by a user actually belongs to them. There is no authentication layer.

**Consequences:**
- Referral fraud: buyers generate fake codes, referrers do not receive their USDT payouts
- Loss of trust in the referral program — a single complaint from a top referrer can collapse the network
- Cannot be fixed post-launch without a backend; the Telegram bot must be modified to validate codes

**Prevention:**
- The bot should be the authority: when a user first interacts with the bot, it assigns them a unique referral code (not just their Telegram ID). The website's referral section should instruct users to get their code from the bot (`/mycode` command), not generate one in the browser
- The website input field becomes a "paste your code here to share" UX, not a generator — the actual code comes from the trusted bot, not from client-side computation
- Never derive the referral code from the Telegram ID directly in JS — if the code is `"REF_" + telegramId`, an attacker can iterate IDs and steal credit

**Detection:** Can a user visit the referral section, type any number in the input, and get a working `t.me/...?start=...` link? If yes, the codes are forgeable.

**Phase:** REF-02 / REF-03 — architecture must be settled with the bot owner before frontend work begins.

---

## High Pitfalls

---

### Pitfall 6: CSS Collision When Integrating the Dashboard HTML

**What goes wrong:** The existing dashboard is a separate HTML file with its own `<style>` block. When its styles are copied into `index.html`, generic selectors like `.container`, `.card`, `.btn`, `.row`, `h2`, `h3` will override or be overridden by the existing site's CSS. The existing site uses minified CSS with `!important` in several places (common in minified blocks). The result is a dashboard that looks correct in isolation but is visually broken inside the main page.

**Why it happens:** Both files were written independently without namespacing. The existing site's dark background (`body { background: #04080f }`) will apply inside the dashboard container. Dashboard colors designed for a white background will be invisible on near-black.

**Consequences:**
- Calculator fields unreadable (white text on white background, or dark text on dark background)
- Layout collapses because `.container` max-width conflicts
- Buttons in the dashboard take on the site's gold styling, breaking dashboard UX

**Prevention:**
- Wrap the entire dashboard HTML in a single wrapper div: `<div class="pearl-calc">...</div>`
- Prefix all dashboard CSS selectors with `.pearl-calc` before integrating — find-replace in the dashboard's style block
- Audit for any `body`, `html`, `:root` rules in the dashboard CSS — these cannot be scoped and must be removed or explicitly overridden
- Test the integration in a staging branch before merging to main

**Detection:** Open browser DevTools, inspect the calculator container. If any property shows "Inherited" from a rule in the main site's style block, there is pollution.

**Phase:** CALC-02 — CSS prefixing is mandatory before integration.

---

### Pitfall 7: GitHub Pages CDN Caching Hides Deploy Failures

**What goes wrong:** GitHub Pages uses Fastly CDN with a ~10-minute edge cache. After deploying a fix (e.g., a broken language switch or a wrong wallet address), the live site continues serving the old file. Testers report "it's still broken" and developers push another commit thinking the first did not deploy. This creates deploy loops and confusion.

**Why it happens:** There is no cache-busting mechanism for `index.html` itself on GitHub Pages. The CDN holds the old version regardless of git push recency.

**Consequences:**
- Wallet address corrections take up to 10 minutes to propagate — during which users see the old address
- i18n updates that fix broken translations are not immediately visible
- Developers waste time re-pushing commits

**Prevention:**
- After any deploy, always verify the live URL by appending `?nocache=<timestamp>` — this bypasses the browser cache but not the CDN
- For critical fixes (wallet addresses, broken functionality), configure a Cloudflare free-tier proxy in front of GitHub Pages — Cloudflare's cache can be purged on demand via its dashboard
- If Cloudflare is not in place, add a cache-busting comment (`<!-- deploy: 2026-05-13T14:00 -->`) to `index.html` on every commit — this forces Fastly to treat it as a new file

**Detection:** After a `git push`, wait 2 minutes, then load the live URL in an incognito window. Compare the deploy timestamp comment.

**Phase:** Affects all phases — establish the Cloudflare or cache-busting discipline at PERF-01.

---

### Pitfall 8: Language Persistence Breaks on Hard Reload

**What goes wrong:** `localStorage.setItem('lang', 'es')` persists the language. But if a user shares the URL with someone else, or clicks a search result link, the recipient gets the page in English (the default) — not in the language the sharer expected. Worse: if the user clears their browser data or opens on a different device, their language is lost.

**Why it happens:** localStorage is device-local and session-specific. It is not part of the URL.

**Consequences:**
- Shared links always show English, defeating multilingual marketing (Hindi/Portuguese users sharing the site get friends who see English)
- Support requests: "the site is not in Spanish anymore" after browser data clear

**Prevention:**
- Use `?lang=es` query parameter as the primary persistence mechanism, with localStorage as the fallback
- On page load: check URL param first → check localStorage → browser `navigator.language` last
- When user switches language: update both the URL param (via `history.replaceState`) AND localStorage
- Shareable URLs then correctly deliver localized content to new visitors

**Detection:** Set language to Hindi. Copy the URL. Paste it in a new incognito window. Does it load in Hindi? If not, persistence is URL-only in localStorage.

**Phase:** I18N-03 (language persistence spec).

---

### Pitfall 9: Construction Feed Photo CORS Error on GitHub Pages

**What goes wrong:** The static facility photo is loaded via `<img src="https://external-cdn.example.com/latest.jpg">`. If the external CDN does not set permissive CORS headers (or if the URL is HTTP not HTTPS), modern browsers will block the request with a mixed-content or CORS error. The image shows as broken with no visible error to the user.

**Why it happens:** GitHub Pages serves over HTTPS. Loading HTTP sub-resources is blocked by default in all modern browsers (mixed content policy). External servers may not have CORS configured.

**Consequences:**
- The construction feed section is permanently broken in production even though it works locally
- Camera host (whoever runs the facility server) must configure headers — coordination dependency

**Prevention:**
- Verify the camera/CDN URL is HTTPS before building the CAM-01 feature
- Confirm the server returns `Access-Control-Allow-Origin: *` or at minimum the GitHub Pages origin
- Add a fallback: if the image fails to load (`onerror`), show a placeholder image from the `media/` folder with a "Photo updating..." label
- Test from an HTTPS context, not just local `file://` — open a deployed branch on GitHub Pages to verify

**Detection:** Open DevTools Network tab. If the construction photo request shows a red CORS or mixed-content error, the CDN configuration is not ready.

**Phase:** CAM-01 / CAM-02.

---

## Moderate Pitfalls

---

### Pitfall 10: Missing `x-default` and Self-Referential hreflang

**What goes wrong:** Even if separate locale HTML files are created (the correct approach for GitHub Pages SEO), forgetting to include a self-referential hreflang tag on each page and the `x-default` tag causes Google to ignore the entire hreflang implementation. A study by Ahrefs found 67% of sites with hreflang have broken implementations.

**Prevention:**
- Every locale page must reference all other locale pages AND itself
- Add `<link rel="alternate" hreflang="x-default" href=".../index.html">` only on the root English page, not on all locale pages
- Use ISO 639-1 codes: `en`, `es`, `pt-BR`, `hi` — not `en-US`, not `en-UK`

**Phase:** I18N-01 (if SEO approach chosen).

---

### Pitfall 11: Translation Strings in Attributes Are Skipped

**What goes wrong:** A common i18n implementation translates `textContent` of elements but forgets `placeholder`, `alt`, `title`, and `aria-label` attributes. Hindi and Spanish users see input placeholders in English. Screen readers announce the English alt text.

**Prevention:**
- Audit every `<input placeholder>`, `<img alt>`, `<button title>`, and `aria-label` in the current HTML
- The i18n engine must handle attribute translation via a separate mechanism (e.g., `data-i18n-attr="placeholder:search_placeholder"`)
- Create a test checklist: for each language, inspect every form field placeholder and image alt in DevTools

**Phase:** I18N-02.

---

### Pitfall 12: Hindi and Portuguese Text Expansion Breaks Layout

**What goes wrong:** Hindi translations routinely run 20-40% longer than English equivalents. The existing site uses `clamp()` for font sizes but not for button widths or nav container widths. Nav items and CTA buttons overflow or wrap unexpectedly in Hindi.

**Prevention:**
- Before writing any Hindi translations, test by padding every English string by 40% (replace "Buy PEARL" with "Buy PEARL NOW TOKEN")
- Use `white-space: nowrap` only where absolutely required — remove it for language-variable UI elements
- Allocate extra layout review time for the Hindi pass specifically; the other three languages are closer to English in character density

**Phase:** I18N-02 (Hindi pass).

---

### Pitfall 13: `innerHTML` in Translation Creates XSS Vector

**What goes wrong:** Some i18n implementations use `element.innerHTML = translations[lang][key]` to support bold/italic within translated strings (e.g., `"<strong>15%</strong> annual revenue"`). If the translation JSON file is ever served from a compromised or user-controlled source, this becomes a stored XSS attack. On a crypto investment site, injected content could replace wallet addresses or redirect Telegram bot links.

**Prevention:**
- Use `textContent` for all plain string translations — not `innerHTML`
- For strings that require embedded markup (bold numbers, line breaks), create the markup in HTML and translate only the text nodes: `<p><strong data-i18n="percent">15%</strong> <span data-i18n="revenue_label">annual revenue</span></p>`
- Translation JSON files must be bundled in the repository (no remote fetch from a CDN or API) — this eliminates the external attack surface entirely

**Phase:** I18N-01 (architectural decision when designing the i18n engine).

---

### Pitfall 14: TON Wallet / Telegram Bot Link Hardcoded in Multiple Places

**What goes wrong:** The buy CTA (`t.me/BOTNAME`) appears in the hero, the token sale section, the calculator CTA, and potentially the referral section. If the bot username ever changes (bot renamed, moved to a different account), every hardcoded instance must be found and updated. One missed instance sends users to a dead link.

**Prevention:**
- Define the bot URL as a single JS constant at the top of the script block: `const TELEGRAM_BOT_URL = 'https://t.me/BOTNAME';`
- All CTA elements reference this constant via JS, not hardcoded `href` values
- Alternatively, use a CSS variable approach: define the URL in a `<meta name="bot-url" content="...">` tag and read it once in JS — but JS constant is simpler

**Phase:** TOKEN-02 / REF-02 (ensure consistency when building these features).

---

### Pitfall 15: "15% Annual Distribution" Language Triggers Securities Framing

**What goes wrong:** The phrase "15% annual revenue distribution" on a token sale page, next to a "Buy PEARL" button, is functionally identical to a prospectus promising dividend yield. Regulators in the EU (MiCA), UK (FCA), and US (SEC) all have guidance that revenue-sharing tokens warrant securities classification review. The TOKEN-03 (token economics page) is the highest-risk content page on the site.

**Prevention:**
- Replace "receive 15% annually" with "participate in production revenue sharing per token holdings"
- Never show percentage yields in the same visual proximity as a buy button
- Add a prominent disclaimer on the token economics page: "Participation in revenue sharing is subject to actual production results. Past or modeled distributions are illustrative only and do not constitute a guarantee or promise of return."
- Have the TOKEN-03 page reviewed by a legal contact familiar with the applicable jurisdiction before publishing

**Phase:** TOKEN-03 (legal review gate before publish).

---

## Minor Pitfalls

---

### Pitfall 16: Browser `navigator.language` Returns Unexpected Subtags

**What goes wrong:** Language detection using `navigator.language` returns values like `en-US`, `pt-BR`, `hi-IN`, `es-419` — not the simple two-letter codes you mapped to translation keys. `translations['hi']` works but `translations['hi-IN']` returns `undefined`, silently falling back to English for all Hindi users.

**Prevention:** Always normalize: `const lang = navigator.language.split('-')[0].toLowerCase();` — then map to your four supported locale keys.

**Phase:** I18N-01.

---

### Pitfall 17: `.DS_Store` Files Committed to GitHub Pages

**What goes wrong:** macOS creates `.DS_Store` files in every directory. The CONCERNS.md already flags this. If media files are added to `media/` without a `.gitignore`, `.DS_Store` files in that directory get committed and are publicly served by GitHub Pages. This is a minor privacy leak (reveals directory names from the developer's filesystem) and a repo hygiene issue.

**Prevention:** Add `.gitignore` with `**/.DS_Store` before creating the `media/` folder. This is a one-minute fix that prevents a persistent annoyance.

**Phase:** PERF-01 (create `.gitignore` as the first commit in this phase).

---

### Pitfall 18: CO2 Counter Breaks Under Language Switch

**What goes wrong:** The CO2 counter uses a formula (`$1 = 100L = 320kg CO2`) and updates via a JS interval. If the language switch replaces the element's `textContent`, the counter's interval timer may reference a now-replaced DOM node and display `NaN` or stop updating.

**Prevention:** The counter element and its child span should not have `data-i18n` attributes. Translate only the surrounding label text. The counter's numeric value is language-agnostic.

**Phase:** I18N-02 (flag during translation attribute mapping).

---

## Phase-Specific Warnings

| Phase Topic | Likely Pitfall | Mitigation |
|-------------|---------------|------------|
| PERF-01 (image extraction) | Base64 blob corruption | Use a script, not manual edit; verify every image before commit |
| I18N-01 (engine design) | innerHTML XSS, JS event listener destruction | Use textContent, translate leaf nodes only |
| I18N-02 (translation pass) | Hindi text expansion breaks layout, attribute strings skipped | 40% padding test, full attribute audit |
| I18N-03 (persistence) | localStorage-only breaks shareable links | URL param + localStorage dual mechanism |
| TOKEN-01/03 (token sale + economics) | Securities framing via calculator outputs and "15% yield" language | Legal review gate; reframe as participation not returns |
| CALC-01 (calculator) | Output labels imply guaranteed return | No dollar output amounts; mandatory disclaimer above fold |
| CALC-02 (dashboard integration) | CSS namespace collision, dark background breaks dashboard | Prefix all dashboard CSS with `.pearl-calc` wrapper |
| REF-02/03 (referral generator) | Forgeable codes from client-side Telegram ID input | Codes must originate from the bot, not the browser |
| CAM-01/02 (construction feed) | CORS/mixed-content error, no fallback | HTTPS CDN verified, onerror fallback image required |

---

## Sources

- Howey test and token securities classification: [SEC Digital Asset Framework](https://www.sec.gov/files/dlt-framework.pdf), [Skadden Howey analysis 2025](https://www.skadden.com/insights/publications/2025/08/howeys-still-here)
- i18n pitfalls: [Shopify i18n best practices](https://shopify.engineering/internationalization-i18n-best-practices-front-end-developers), [Phrase localization mistakes](https://phrase.com/blog/posts/10-common-mistakes-in-software-localization/)
- Vanilla JS i18n implementation: [Andreas Remdt i18n script](https://andreasremdt.com/blog/building-a-super-small-and-simple-i18n-script-in-javascript/), [Phrase JS localization guide](https://phrase.com/blog/posts/step-step-guide-javascript-localization/)
- hreflang mistakes: [Search Engine Journal hreflang audit](https://www.searchenginejournal.com/ask-an-seo-what-are-the-most-common-hreflang-mistakes/556455/), [Collaborada hreflang mistakes](https://www.collaborada.com/blog/common-hreflang-mistakes)
- Client-side referral security: [Rhino Security Labs referral abuse](https://rhinosecuritylabs.com/research/referral-beware-your-rewards-are-mine-part-1/), [OWASP Client-Side Top 10](https://owasp.org/www-project-top-10-client-side-security-risks/)
- GitHub Pages caching: [mrmarble.dev caching GitHub Pages](https://mrmarble.dev/blog/caching-github-pages/)
- CSS namespace conflicts: [MDN handling conflicts](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_conflicts)
- Crypto marketing compliance: [Aurum Law crypto marketing checklist](https://aurum.law/newsroom/Crypto-Marketing-Compliance), [CoinLaw compliance mistakes](https://coinlaw.io/most-costly-crypto-compliance-mistakes/)
