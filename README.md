# Awesome Open-Source SEO

**[中文版](./README.zh.md)**

**[Web version](https://zens.ink/awesome)**

A curated list of open-source SEO tools you can self-host, fork, and read line by line.

Every entry ships real source code under an open license. No SaaS trials, no affiliate links, no freemium walls.

> Why this list exists: existing awesome-seo lists mix tools with articles, courses, and paid products. This one is tools-only, source-available-only. If it doesn't run on your machine, it doesn't belong here.

**Badges** — ![CLI][CLI Icon] runs from a terminal · ![Self-host][Self-host Icon] ships a self-hostable web app · ![GEO/AI][GEO Icon] targets AI-search visibility · ![Active][Active Icon] has commits in the last 12 months · ⚠️ means the repo is archived.

Star counts, activity badges and archive flags are refreshed automatically every month by [this script](./scripts/refresh.py) — no stale snapshots. Last refresh: Oct 2026.

**Featured on this list?** Grab a badge for your README:

[![Featured in Awesome Open-Source SEO](https://img.shields.io/badge/Featured_in-Awesome_Open--Source_SEO-7c3aed?style=for-the-badge)](https://zens.ink/awesome)

````md
[![Featured in Awesome Open-Source SEO](https://img.shields.io/badge/Featured_in-Awesome_Open--Source_SEO-7c3aed?style=for-the-badge)](https://zens.ink/awesome)
````

## Contents

- [All-in-One Platforms](#all-in-one-platforms)
- [Crawlers & Site Audit](#crawlers--site-audit)
  - [Site Crawlers & Auditors](#site-crawlers--auditors)
  - [CI & Performance Budgets](#ci--performance-budgets)
  - [Crawler Frameworks](#crawler-frameworks)
- [Rank Tracking](#rank-tracking)
- [Analytics & Log Analysis](#analytics--log-analysis)
  - [Self-hosted Web Analytics](#self-hosted-web-analytics)
  - [Log & Server Analysis](#log--server-analysis)
- [GSC Data Extraction](#gsc-data-extraction)
- [SERP & Keyword Research](#serp--keyword-research)
  - [SERP APIs & Scrapers](#serp-apis--scrapers)
  - [Keyword & Data Toolkits](#keyword--data-toolkits)
- [GEO & AI Search Visibility](#geo--ai-search-visibility)
  - [Agent Skills & Prompt Libraries](#agent-skills--prompt-libraries)
  - [GEO Platforms & Auditors](#geo-platforms--auditors)
  - [llms.txt Infrastructure](#llmstxt-infrastructure)
- [Framework & CMS Integrations](#framework--cms-integrations)
  - [React & Next.js](#react--nextjs)
  - [PHP, WordPress & Laravel](#php-wordpress--laravel)
  - [Static Site Generators](#static-site-generators)
  - [Other Frameworks](#other-frameworks)
- [Indexing & Sitemaps](#indexing--sitemaps)
- [CLI Toolkits](#cli-toolkits)
- [Other Curated Lists](#other-curated-lists)
- [Recommended Stacks](#recommended-stacks)

## All-in-One Platforms

- [open-seo](https://github.com/every-app/open-seo) ![Self-host][Self-host Icon] ![Active][Active Icon] — Open-source alternative to Semrush and Ahrefs. The most complete attempt at a full suite so far. (22.5k★, MIT)
- [rankme.fast](https://github.com/SelmiAbderrahim/rankme.fast) ![Self-host][Self-host Icon] ![Active][Active Icon] — Self-hosted SEO platform in active early development: rank tracking, audits, and reporting under one roof. (631★, AGPL-3.0)

## Crawlers & Site Audit

### Site Crawlers & Auditors

- [python-seo-analyzer](https://github.com/sethblack/python-seo-analyzer) ![CLI][CLI Icon] ![Active][Active Icon] — Python tool that crawls a site and reports structural issues. One of the oldest projects in this space. (1.5k★)
- [linkinator](https://github.com/JustinBeckwith/linkinator) ![CLI][CLI Icon] ![Active][Active Icon] — Broken-link checker that crawls websites and validates links. Made by a Google engineer. (1.3k★, MIT)
- [LibreCrawl](https://github.com/PhialsBasement/LibreCrawl) ![Active][Active Icon] — Free desktop SEO crawler, an open-source alternative to Screaming Frog. (1k★, MIT)
- [seonaut](https://github.com/StJudeWasHere/seonaut) ![Self-host][Self-host Icon] ![Active][Active Icon] — Open-source SEO audit tool with a web interface. Self-hostable. (804★, MIT)
- [crawlseo](https://github.com/crawlseo/crawlseo) ![Self-host][Self-host Icon] ![Active][Active Icon] — Open-source SEO monitoring: Search Console + crawler + Core Web Vitals in one. (621★, MIT)
- [seo-audits-toolkit](https://github.com/StanGirard/seo-audits-toolkit) ![CLI][CLI Icon] — Lighthouse and security-header crawler that audits whole sites. (815★)
- [search-solved-public-seo](https://github.com/searchsolved/search-solved-public-seo) ![CLI][CLI Icon] ![Active][Active Icon] — Collection of practical Python SEO scripts by Lee Foot. (418★)

### CI & Performance Budgets

- [lighthouse](https://github.com/GoogleChrome/lighthouse) ![CLI][CLI Icon] ![Active][Active Icon] — Google's official open-source auditor for performance, SEO, and best practices. Runs from CLI or CI. (30.9k★, Apache-2.0)
- [lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci) ![CLI][CLI Icon] ![Active][Active Icon] — Runs Lighthouse on every commit and asserts budgets in CI. (7.1k★, Apache-2.0)

### Crawler Frameworks

Not SEO tools per se — the standard raw material for building custom crawlers for JS-rendered pages and structured extraction.

- [scrapy](https://github.com/scrapy/scrapy) ![Active][Active Icon] — The Python crawling framework. (64.6k★, BSD-3-Clause)
- [brozzler](https://github.com/internetarchive/brozzler) ![Active][Active Icon] — Distributed, browser-based (Playwright) web crawler from the Internet Archive. (822★)

## Rank Tracking

- [SerpBear](https://github.com/towfiqi/serpbear) ![Self-host][Self-host Icon] ![Active][Active Icon] — Self-hosted rank tracker (Next.js + SQLite, Docker) with unlimited domains/keywords, GSC and Google Ads integration, Slack/Telegram alerts. The most-recommended self-hosted tracker. (2.1k★, GPL-3.0)
- [serposcope](https://github.com/serphacker/serposcope) ![Self-host][Self-host Icon] — Long-running self-hosted rank monitor (Java) with multi-region, proxy, and captcha support. Legacy but battle-tested. (757★, GPLv3) ⚠️ archived
- [Seo-Panel](https://github.com/sendtogeo/Seo-Panel) ![Self-host][Self-host Icon] — Multi-site SEO control panel (PHP + MySQL) with rank tracking, audits, backlink monitoring, and white-label reports for agencies. (138★, GPL-3.0)

## Analytics & Log Analysis

### Self-hosted Web Analytics

- [plausible](https://github.com/plausible/analytics) ![Self-host][Self-host Icon] ![Active][Active Icon] — Lightweight, cookieless, privacy-first analytics. (29.3k★, AGPL-3.0)
- [matomo](https://github.com/matomo-org/matomo) ![Self-host][Self-host Icon] ![Active][Active Icon] — Self-hosted Google Analytics alternative. First-party data, compliance-friendly. (21.9k★, GPL-3.0)

### Log & Server Analysis

- [goaccess](https://github.com/allinurl/goaccess) ![CLI][CLI Icon] ![Active][Active Icon] — Real-time terminal log analyzer for Nginx/Apache. Watch Googlebot crawls, 404s, and bandwidth from raw logs — a technical SEO workhorse. (21k★, MIT)
- [OpenSearch](https://github.com/opensearch-project/OpenSearch) ![Self-host][Self-host Icon] ![Active][Active Icon] — Search engine for large-scale log and clickstream queries, including crawl-behavior analysis. (13.8k★, Apache-2.0)

## GSC Data Extraction

- [google-search-console-export-all](https://github.com/swalker-888/google-search-console-export-all) ![CLI][CLI Icon] — Bulk CSV export of Search Console data, bypassing the 1,000-row UI limit. (12★)

## SERP & Keyword Research

### SERP APIs & Scrapers

- [openserp](https://github.com/karust/openserp) ![Self-host][Self-host Icon] ![Active][Active Icon] — Self-hosted SERP API with browser-rendered Google results. For SEO and automation. (1.4k★, MIT)
- [clauneck](https://github.com/serpapi/clauneck) — Scrapes emails and social accounts from web pages, built for lead research. (204★, MIT)

### Keyword & Data Toolkits

- [advertools](https://github.com/eliasdabbas/advertools) ![CLI][CLI Icon] ![Active][Active Icon] — Online-marketing productivity and analysis library: crawling, SERP analysis, keyword processing. (1.5k★, MIT)

## GEO & AI Search Visibility

The newest category. These tools measure and improve how sites appear in AI answers, not just blue links.

### Agent Skills & Prompt Libraries

- [claude-seo](https://github.com/AgriciDaniel/claude-seo) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Universal SEO skill for Claude Code: 25 sub-skills and 18 sub-agents covering audit, content, and technical work. (18.4k★, MIT)
- [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) ![GEO/AI][GEO Icon] ![Active][Active Icon] — GEO-first SEO skill for AI coding assistants, focused on AI-search optimization. (10.9k★, MIT)
- [seomachine](https://github.com/TheCraigHewitt/seomachine) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Claude Code workspace for producing long-form, SEO-optimized content end to end, from keyword to published draft. (7.5k★, MIT)
- [open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Free SEO MCP server plus skills for Claude: keyword research, rank tracking, audits. Speaks the protocol your agent already uses. (4.6k★, MIT)
- [notfair-plugin](https://github.com/nowork-studio/notfair-plugin) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Open-source SEO, GEO, and marketing skills for AI agents. (3.9k★, MIT)
- [gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Claude Code skill for AEO/GEO: instrument your site so AI engines cite it, from a tag-management angle. (1.3k★, MIT)
- [codex-seo](https://github.com/AgriciDaniel/codex-seo) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Codex-first sibling of the claude-seo suite: 26 workflows and 24 TOML agents for technical SEO. (799★)
- [seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Agent skill that runs a Python + LLM two-layer audit on any URL: robots, sitemap, canonicals, H1, schema, PSI. (761★, MIT)
- [fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) ![GEO/AI][GEO Icon] ![Active][Active Icon] — One skill that audits and optimizes SEO, AEO, and GEO — every acronym the AI-search era has coined. (709★, MIT)
- [seo-ops](https://github.com/tigerless-labs/seo-ops) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Agent skill that fetches a URL and returns a crawler's-eye pass/fail report on the SEO fundamentals. (700★)
- [Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Google's SEO documentation turned into an AI prompt library. (556★, MIT)

### GEO Platforms & Auditors

- [GEOFlow](https://github.com/yaojingang/GEOFlow) ![Self-host][Self-host Icon] ![GEO/AI][GEO Icon] ![Active][Active Icon] — GEO content engineering and multi-site distribution system. (3.8k★, Apache-2.0)
- [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) ![GEO/AI][GEO Icon] ![Active][Active Icon] — AEO & GEO audit toolkit: run the checks, get a prioritized fix list for AI-search visibility. (1k★, MIT)
- [geolook](https://github.com/aigclink/geolook) ![GEO/AI][GEO Icon] ![Active][Active Icon] — End-to-end GEO implementation: status analysis, diagnosis, and reporting. (749★, MIT)
- [GEORank](https://github.com/yaojingang/GEORank) ![Self-host][Self-host Icon] ![GEO/AI][GEO Icon] ![Active][Active Icon] — GEO ranking platform from the GEOFlow author: track how sites surface in generative-engine answers. (492★, Apache-2.0)
- [elmo](https://github.com/elmohq/elmo) ![Self-host][Self-host Icon] ![GEO/AI][GEO Icon] ![Active][Active Icon] — Open-source AEO/GEO platform: measure and improve how your site shows up in AI answers. (420★, MIT)
- [notra](https://github.com/usenotra/notra) ![GEO/AI][GEO Icon] ![Active][Active Icon] — GEO monitoring that asks ChatGPT, Claude, and Gemini the questions your buyers ask, then tracks who gets cited. (256★, AGPL-3.0)
- [AutoGEO](https://github.com/cxcscmu/AutoGEO) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Research-grade GEO framework (ICLR'26): automatically learns which content edits move generative-engine rankings. (224★, MIT)
- [searchstack-aeo](https://github.com/alexpospekhov/searchstack-aeo) ![Self-host][Self-host Icon] ![GEO/AI][GEO Icon] ![Active][Active Icon] — Open-source AEO/GEO/SEO stack for AI-native websites. (104★, MIT)

- [Traclux](https://github.com/ZaneLau/traclux-probe) ![Self-host][Self-host Icon] ![GEO/AI][GEO Icon] ![Active][Active Icon] — Self-hosted GEO workbench: generate probes with CSSM-HI, execute them against a configured model, and inspect saved answers and brand analysis. (0★, Apache-2.0)

### llms.txt Infrastructure

- [llms-txt](https://github.com/AnswerDotAI/llms-txt) ![GEO/AI][GEO Icon] ![Active][Active Icon] — The llms.txt proposal itself, by Answer.ai: a markdown map that helps language models use your site. The convention most GEO tools write for. (2.7k★, Apache-2.0)
- [llmstxt-generator](https://github.com/firecrawl/llmstxt-generator) ![GEO/AI][GEO Icon] — Firecrawl's generator that turns any website into llms.txt + llms-full.txt. Unmaintained but still the simplest path. (539★)

## Framework & CMS Integrations

### React & Next.js

- [next-seo](https://github.com/garmeeh/next-seo) ![Active][Active Icon] — SEO plugin for Next.js: meta, Open Graph, JSON-LD handled declaratively. (8.5k★, MIT)

### PHP, WordPress & Laravel

- [wordpress-seo](https://github.com/Yoast/wordpress-seo) ![Active][Active Icon] — Yoast SEO for WordPress, the plugin that runs a large share of the web. (2k★)
- [laravel-seo](https://github.com/ralphjsmit/laravel-seo) ![Active][Active Icon] — SEO handling for Laravel applications. (868★, MIT)
- [the-seo-framework](https://github.com/sybrew/the-seo-framework) ![Active][Active Icon] — Lightweight, automated SEO plugin for WordPress. (482★, GPL-3.0)

### Static Site Generators

- [jekyll-seo-tag](https://github.com/jekyll/jekyll-seo-tag) ![Active][Active Icon] — Jekyll plugin adding metadata tags for search engines and social. (1.7k★, MIT)
- [astro-seo](https://github.com/jonasmerlin/astro-seo) ![Active][Active Icon] — SEO component for Astro. (1.4k★, MIT)

### Other Frameworks

- [meta-tags](https://github.com/kpumuk/meta-tags) ![Active][Active Icon] — SEO meta tags for Ruby on Rails. (2.8k★, MIT)
- [nuxt-seo](https://github.com/harlan-zw/nuxt-seo) ![Active][Active Icon] — Fully equipped technical SEO and AEO for Nuxt. (1.4k★, MIT)
- [svelte-seo](https://github.com/artiebits/svelte-seo) ![Active][Active Icon] — SEO meta tags for Svelte/SvelteKit. (563★, MIT)

## Indexing & Sitemaps

- [google-indexing-script](https://github.com/goenning/google-indexing-script) ![CLI][CLI Icon] — Script that gets your site indexed on Google fast, via the Indexing API. (7.7k★, MIT)
- [next-sitemap](https://github.com/iamvishnusankar/next-sitemap) ![Active][Active Icon] — Sitemap and robots.txt generator for Next.js. (3.7k★, MIT)
- [laravel-sitemap](https://github.com/spatie/laravel-sitemap) ![Active][Active Icon] — Sitemap generation for Laravel. (2.6k★, MIT)
- [jekyll-sitemap](https://github.com/jekyll/jekyll-sitemap) — Sitemap plugin for Jekyll. (983★, MIT)

## CLI Toolkits

- [zens-ink](https://github.com/ZensInk/zens-ink-seo-package) ![CLI][CLI Icon] ![GEO/AI][GEO Icon] ![Active][Active Icon] — Maintained by this organization. Zero-dependency Python CLI with 22 tools: keyword research, SERP difficulty scoring, technical site audit, and a 16-dimension GEO score. On PyPI as `zens-ink`. Ships 9 installable agent skills (`npx skills add ZensInk/zens-ink-seo-package`) covering keyword research, difficulty, intent, audits, competitor gaps, rank tracking, Reddit mining, and GEO readiness. (53★, MIT)

## Other Curated Lists

- [awesome-seo (bmpi-dev)](https://github.com/bmpi-dev/awesome-seo) ![Active][Active Icon] — Google SEO research and traffic monetization resources. (2.8k★, MIT)
- [search-engine-optimization](https://github.com/marcobiedermann/search-engine-optimization) — Checklist-style collection of SEO resources. (2.8k★, MIT)
- [awesome-seo-tools (serpapi)](https://github.com/serpapi/awesome-seo-tools) ![Active][Active Icon] — Curated list of SEO tools, includes commercial ones. (1.1k★)
- [awesome-seo (teles)](https://github.com/teles/awesome-seo) ![Active][Active Icon] — General curated list of SEO links. (884★)

## Recommended Stacks

No single open-source tool replaces Semrush or Ahrefs — the moat there is the backlink index and search-volume data. But execution-layer work (audits, crawling, rank tracking, first-party analytics) is mature. A combined stack covers most daily needs. The honest boundary: for competitive backlink mining, keep one paid Ahrefs/Semrush read-only account for data, and let open source handle execution and your own data.

**Small sites / indie sites**

- [SerpBear](https://github.com/towfiqi/serpbear) (rank tracking) + [seonaut](https://github.com/StJudeWasHere/seonaut) (audits) + [Matomo](https://github.com/matomo-org/matomo) or [Plausible](https://github.com/plausible/analytics) (analytics) + [lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci) (CI checks)

**Agencies**

- [Seo-Panel](https://github.com/sendtogeo/Seo-Panel) (multi-site management) + [SerpBear](https://github.com/towfiqi/serpbear) + GSC bulk export ([google-search-console-export-all](https://github.com/swalker-888/google-search-console-export-all)) + [seonaut](https://github.com/StJudeWasHere/seonaut) for recurring crawls

**Developers / AI workflows**

- [zens-ink](https://github.com/ZensInk/zens-ink-seo-package) or [RustySEO](https://www.rustyseo.com/) as the base + [scrapy](https://github.com/scrapy/scrapy) for custom crawls + [goaccess](https://github.com/allinurl/goaccess) for raw logs + [seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) for LLM-assisted audits

## Contributing

PRs welcome — see [CONTRIBUTING.md](./CONTRIBUTING.md) for criteria and the entry format. Self-promotion is allowed but disclose it in the PR, like everyone else does.

## License

[CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/) — use this list however you want.

---

Maintained by [ZensInk](https://zens.ink) — a zero-dependency, free-tier-first SEO toolkit for indie builders.

[CLI Icon]: media/cli.svg
[Self-host Icon]: media/selfhost.svg
[GEO Icon]: media/geo.svg
[Active Icon]: media/active.svg
