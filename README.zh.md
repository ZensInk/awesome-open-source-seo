# Awesome Open-Source SEO（开源 SEO 工具精选）

**[English version](./README.md)**

**[网页版](https://zens.ink/zh/awesome)**

一个只收录开源 SEO 工具的精选清单——可自托管、可 fork、可逐行读源码。

每一条都是真实源码 + 开放协议。不收 SaaS 试用、不放联盟链接、不搞免费增值墙。

> 为什么要有这个清单：现有的 awesome-seo 列表把工具、文章、课程、付费产品混在一起。本清单只收工具、只收有源码的——在你自己机器上跑不起来的，不配出现在这里。

**徽章说明** —— ![CLI][CLI Icon] 命令行运行 · ![Self-host][Self-host Icon] 带可自托管的 Web 界面 · ![GEO/AI][GEO Icon] 面向 AI 搜索可见性 · ![Active][Active Icon] 近 12 个月内有提交 · ⚠️ 表示仓库已归档。

星标数、活跃徽章和归档标记由[这个脚本](./scripts/refresh.py)每月自动刷新——没有过期快照。最近刷新：2026 年 10 月。

## 目录

- [一站式平台](#一站式平台)
- [爬虫与站点审计](#爬虫与站点审计)
  - [站点爬虫与审计器](#站点爬虫与审计器)
  - [CI 与性能预算](#ci-与性能预算)
  - [爬虫框架](#爬虫框架)
- [排名追踪](#排名追踪)
- [分析与日志](#分析与日志)
  - [自托管 Web 分析](#自托管-web-分析)
  - [日志与服务器分析](#日志与服务器分析)
- [GSC 数据导出](#gsc-数据导出)
- [SERP 与关键词研究](#serp-与关键词研究)
  - [SERP API 与抓取器](#serp-api-与抓取器)
  - [关键词与数据工具库](#关键词与数据工具库)
- [GEO 与 AI 搜索可见性](#geo-与-ai-搜索可见性)
  - [Agent 技能与提示词库](#agent-技能与提示词库)
  - [GEO 平台与审计器](#geo-平台与审计器)
  - [llms.txt 基础设施](#llmstxt-基础设施)
- [框架与 CMS 集成](#框架与-cms-集成)
  - [React 与 Next.js](#react-与-nextjs)
  - [PHP、WordPress 与 Laravel](#phpwordpress-与-laravel)
  - [静态站点生成器](#静态站点生成器)
  - [其他框架](#其他框架)
- [收录与站点地图](#收录与站点地图)
- [CLI 工具集](#cli-工具集)
- [其他精选清单](#其他精选清单)
- [推荐组合](#推荐组合)

## 一站式平台

- [open-seo](https://github.com/every-app/open-seo) ![Self-host][Self-host Icon] ![Active][Active Icon] — Semrush 和 Ahrefs 的开源替代，目前最完整的一站式尝试。(22.5k★, MIT)
- [rankme.fast](https://github.com/SelmiAbderrahim/rankme.fast) ![Self-host][Self-host Icon] ![Active][Active Icon] — 自托管 SEO 平台，早期开发活跃：排名追踪、审计、报告一体。(631★, AGPL-3.0)

## 爬虫与站点审计

### 站点爬虫与审计器

- [python-seo-analyzer](https://github.com/sethblack/python-seo-analyzer) ![CLI][CLI Icon] ![Active][Active Icon] — Python 爬虫，抓整站并输出结构问题报告，这个领域最老的项目之一。(1.5k★)
- [linkinator](https://github.com/JustinBeckwith/linkinator) ![CLI][CLI Icon] ![Active][Active Icon] — 断链检查器，爬网站验证所有链接，作者是 Google 工程师。(1.3k★, MIT)
- [LibreCrawl](https://github.com/PhialsBasement/LibreCrawl) ![Active][Active Icon] — 免费桌面端 SEO 爬虫，Screaming Frog 的开源替代。(1k★, MIT)
- [seonaut](https://github.com/StJudeWasHere/seonaut) ![Self-host][Self-host Icon] ![Active][Active Icon] — 带网页界面的开源 SEO 审计工具，可自托管。(804★, MIT)
- [crawlseo](https://github.com/crawlseo/crawlseo) ![Self-host][Self-host Icon] ![Active][Active Icon] — 开源 SEO 监控：Search Console + 爬虫 + Core Web Vitals 三合一。(621★, MIT)
- [seo-audits-toolkit](https://github.com/StanGirard/seo-audits-toolkit) ![CLI][CLI Icon] — Lighthouse + 安全响应头爬虫，整站审计。(815★)
- [search-solved-public-seo](https://github.com/searchsolved/search-solved-public-seo) ![CLI][CLI Icon] ![Active][Active Icon] — Lee Foot 的实用 Python SEO 脚本集。(418★)

### CI 与性能预算

- [lighthouse](https://github.com/GoogleChrome/lighthouse) ![CLI][CLI Icon] ![Active][Active Icon] — Google 官方开源审计器，性能 + SEO + 最佳实践，CLI 或 CI 运行。(30.9k★, Apache-2.0)
- [lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci) ![CLI][CLI Icon] ![Active][Active Icon] — 每次提交跑 Lighthouse 并在 CI 里断言预算。(7.1k★, Apache-2.0)

### 爬虫框架

本身不是 SEO 工具——给 JS 渲染页和定制化抽取写爬虫的标准原材料。

- [scrapy](https://github.com/scrapy/scrapy) ![Active][Active Icon] — Python 爬虫框架。(64.6k★, BSD-3-Clause)
- [brozzler](https://github.com/internetarchive/brozzler) ![Active][Active Icon] — Internet Archive 出品的分布式浏览器（Playwright）爬虫。(822★)

## 排名追踪

- [SerpBear](https://github.com/towfiqi/serpbear) ![Self-host][Self-host Icon] ![Active][Active Icon] — 自托管排名追踪（Next.js + SQLite，Docker），无限域名/关键词，接 GSC 和 Google Ads，Slack/Telegram 告警。最常被推荐的自托管追踪器。(2.1k★, GPL-3.0)
- [serposcope](https://github.com/serphacker/serposcope) ![Self-host][Self-host Icon] — 老牌自托管排名监控（Java），多地区、代理、验证码支持。Legacy 但久经考验。(757★, GPLv3) ⚠️ archived
- [Seo-Panel](https://github.com/sendtogeo/Seo-Panel) ![Self-host][Self-host Icon] — 多站点 SEO 控制面板（PHP + MySQL），含排名、审计、外链监控、白标报告，适合 Agency。(138★, GPL-3.0)

## 分析与日志

### 自托管 Web 分析

- [plausible](https://github.com/plausible/analytics) ![Self-host][Self-host Icon] ![Active][Active Icon] — 轻量、无 Cookie、隐私优先的分析。(29.3k★, AGPL-3.0)
- [matomo](https://github.com/matomo-org/matomo) ![Self-host][Self-host Icon] ![Active][Active Icon] — 自托管 Google Analytics 替代。一手数据，合规友好。(21.9k★, GPL-3.0)

### 日志与服务器分析

- [goaccess](https://github.com/allinurl/goaccess) ![CLI][CLI Icon] ![Active][Active Icon] — 实时终端日志分析器（Nginx/Apache）。从原始日志看 Googlebot 抓取、404、带宽，技术 SEO 神器。(21k★, MIT)
- [OpenSearch](https://github.com/opensearch-project/OpenSearch) ![Self-host][Self-host Icon] ![Active][Active Icon] — 大规模日志与点击流查询的搜索引擎，含爬取行为分析。(13.8k★, Apache-2.0)

## GSC 数据导出

- [google-search-console-export-all](https://github.com/swalker-888/google-search-console-export-all) ![CLI][CLI Icon] — 批量 CSV 导出 Search Console 数据，绕过界面 1000 行限制。(12★)

## SERP 与关键词研究

### SERP API 与抓取器

- [openserp](https://github.com/karust/openserp) ![Self-host][Self-host Icon] ![Active][Active Icon] — 自托管 SERP API，浏览器渲染的真实 Google 结果。(1.4k★, MIT)
- [clauneck](https://github.com/serpapi/clauneck) — 从网页抓邮箱和社交账号，线索调研用。(204★, MIT)

### 关键词与数据工具库

- [advertools](https://github.com/eliasdabbas/advertools) ![CLI][CLI Icon] ![Active][Active Icon] — 在线营销生产力库：爬虫、SERP 分析、关键词处理一体化。(1.5k★, MIT)

## GEO 与 AI 搜索可见性

最新的品类。这些工具度量和优化的是站点在 AI 回答里的表现，而不只是蓝色链接。

### Agent 技能与提示词库

- [claude-seo](https://github.com/AgriciDaniel/claude-seo) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Claude Code 的通用 SEO 技能：25 个子技能 + 18 个子代理，覆盖审计、内容与技术 SEO。(18.4k★, MIT)
- [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) ![GEO/AI][GEO Icon] ![Active][Active Icon] — GEO 优先的 SEO 技能，专注 AI 搜索优化。(10.9k★, MIT)
- [seomachine](https://github.com/TheCraigHewitt/seomachine) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Claude Code 工作区，端到端产出 SEO 长文：从关键词到可发布草稿。(7.5k★, MIT)
- [open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) ![GEO/AI][GEO Icon] ![Active][Active Icon] — 免费 SEO MCP server + Claude 技能：关键词研究、排名追踪、审计，agent 直接调用。(4.6k★, MIT)
- [notfair-plugin](https://github.com/nowork-studio/notfair-plugin) ![GEO/AI][GEO Icon] ![Active][Active Icon] — 给 AI agent 用的开源 SEO、GEO 和营销技能。(3.9k★, MIT)
- [gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Claude Code 的 AEO/GEO 技能：从标签管理角度埋好站点，让 AI 引擎引用你。(1.3k★, MIT)
- [codex-seo](https://github.com/AgriciDaniel/codex-seo) ![GEO/AI][GEO Icon] ![Active][Active Icon] — claude-seo 套件的 Codex 版：26 个工作流 + 24 个 TOML agent。(799★)
- [seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Agent skill，Python + LLM 双层审计任意 URL：robots、sitemap、canonical、H1、schema、PSI。(761★, MIT)
- [fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) ![GEO/AI][GEO Icon] ![Active][Active Icon] — 一个技能审计并优化 SEO、AEO、GEO 全家桶。(709★, MIT)
- [seo-ops](https://github.com/tigerless-labs/seo-ops) ![GEO/AI][GEO Icon] ![Active][Active Icon] — Agent skill，给一个 URL，返回爬虫视角的 SEO 基础项通过/失败报告。(700★)
- [Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master) ![GEO/AI][GEO Icon] ![Active][Active Icon] — 把 Google SEO 官方文档做成的 AI 提示词库。(556★, MIT)

### GEO 平台与审计器

- [GEOFlow](https://github.com/yaojingang/GEOFlow) ![Self-host][Self-host Icon] ![GEO/AI][GEO Icon] ![Active][Active Icon] — GEO 内容工程与多站点分发系统。(3.8k★, Apache-2.0)
- [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) ![GEO/AI][GEO Icon] ![Active][Active Icon] — AEO/GEO 审计工具包：跑完检查项，输出 AI 搜索可见性优先修复清单。(1k★, MIT)
- [geolook](https://github.com/aigclink/geolook) ![GEO/AI][GEO Icon] ![Active][Active Icon] — 端到端 GEO 实现：状态分析、诊断、报告。(749★, MIT)
- [GEORank](https://github.com/yaojingang/GEORank) ![Self-host][Self-host Icon] ![GEO/AI][GEO Icon] ![Active][Active Icon] — GEOFlow 作者出品的 GEO 排名平台：追踪站点在生成式引擎回答中的浮现。(492★, Apache-2.0)
- [elmo](https://github.com/elmohq/elmo) ![Self-host][Self-host Icon] ![GEO/AI][GEO Icon] ![Active][Active Icon] — 开源 AEO/GEO 平台：度量并改进站点在 AI 回答中的呈现。(420★, MIT)
- [notra](https://github.com/usenotra/notra) ![GEO/AI][GEO Icon] ![Active][Active Icon] — 问 ChatGPT、Claude、Gemini 买家会问的问题，追踪谁被引用。(256★, AGPL-3.0)
- [AutoGEO](https://github.com/cxcscmu/AutoGEO) ![GEO/AI][GEO Icon] ![Active][Active Icon] — 学术派 GEO 框架（ICLR'26）：自动学习哪些内容编辑能搞动生成式引擎排名。(224★, MIT)
- [searchstack-aeo](https://github.com/alexpospekhov/searchstack-aeo) ![Self-host][Self-host Icon] ![GEO/AI][GEO Icon] ![Active][Active Icon] — 面向 AI 原生站点的开源 AEO/GEO/SEO 技术栈。(104★, MIT)

- [CiteLadder](https://github.com/abhij1306/CiteLadder) ![Self-host][Self-host Icon] ![GEO/AI][GEO Icon] — 自托管的 AI 搜索可见性追踪器：看 ChatGPT、Gemini、Claude 和 Google AI Overviews 怎么回答买家问题、点名哪些品牌、引用哪些页面，附带 MCP server。(4★, AGPL-3.0)
- [Traclux](https://github.com/ZaneLau/traclux-probe) ![Self-host][Self-host Icon] ![GEO/AI][GEO Icon] ![Active][Active Icon] — 可自部署的 GEO 工作台：用 CSSM-HI 生成探针，接入配置的模型执行，再查看保存的回答和品牌分析。(0★, Apache-2.0)

### llms.txt 基础设施

- [llms-txt](https://github.com/AnswerDotAI/llms-txt) ![GEO/AI][GEO Icon] ![Active][Active Icon] — llms.txt 提案本体（Answer.ai 出品）：帮语言模型读懂你站点的 markdown 地图，多数 GEO 工具为之写文件。(2.7k★, Apache-2.0)
- [llmstxt-generator](https://github.com/firecrawl/llmstxt-generator) ![GEO/AI][GEO Icon] — Firecrawl 的生成器，把任意网站转成 llms.txt + llms-full.txt。已停更但仍是最省事的路径。(539★)

## 框架与 CMS 集成

### React 与 Next.js

- [next-seo](https://github.com/garmeeh/next-seo) ![Active][Active Icon] — Next.js SEO 插件：meta、Open Graph、JSON-LD 声明式处理。(8.5k★, MIT)

### PHP、WordPress 与 Laravel

- [wordpress-seo](https://github.com/Yoast/wordpress-seo) ![Active][Active Icon] — Yoast SEO，WordPress 生态份额最大的 SEO 插件。(2k★)
- [laravel-seo](https://github.com/ralphjsmit/laravel-seo) ![Active][Active Icon] — Laravel 应用的 SEO 处理。(868★, MIT)
- [the-seo-framework](https://github.com/sybrew/the-seo-framework) ![Active][Active Icon] — 轻量自动化的 WordPress SEO 插件。(482★, GPL-3.0)

### 静态站点生成器

- [jekyll-seo-tag](https://github.com/jekyll/jekyll-seo-tag) ![Active][Active Icon] — Jekyll 插件，为搜索引擎和社交网络输出 meta 标签。(1.7k★, MIT)
- [astro-seo](https://github.com/jonasmerlin/astro-seo) ![Active][Active Icon] — Astro 的 SEO 组件。(1.4k★, MIT)

### 其他框架

- [meta-tags](https://github.com/kpumuk/meta-tags) ![Active][Active Icon] — Ruby on Rails 的 SEO meta 标签方案。(2.8k★, MIT)
- [nuxt-seo](https://github.com/harlan-zw/nuxt-seo) ![Active][Active Icon] — Nuxt 的全套技术 SEO 与 AEO。(1.4k★, MIT)
- [svelte-seo](https://github.com/artiebits/svelte-seo) ![Active][Active Icon] — Svelte/SvelteKit 的 SEO meta 标签。(563★, MIT)

## 收录与站点地图

- [google-indexing-script](https://github.com/goenning/google-indexing-script) ![CLI][CLI Icon] — 用 Indexing API 快速让 Google 收录你的站。(7.7k★, MIT)
- [next-sitemap](https://github.com/iamvishnusankar/next-sitemap) ![Active][Active Icon] — Next.js 的 sitemap 和 robots.txt 生成器。(3.7k★, MIT)
- [laravel-sitemap](https://github.com/spatie/laravel-sitemap) ![Active][Active Icon] — Laravel 站点地图生成。(2.6k★, MIT)
- [jekyll-sitemap](https://github.com/jekyll/jekyll-sitemap) — Jekyll 站点地图插件。(983★, MIT)

## CLI 工具集

- [zens-ink](https://github.com/ZensInk/zens-ink-seo-package) ![CLI][CLI Icon] ![Active][Active Icon] — 本组织维护。零依赖 Python CLI，19 个工具：关键词挖掘、SERP 难度评分、技术站点审计、16 维度 GEO 评分。PyPI 包名 `zens-ink`。(53★, MIT)

## 其他精选清单

- [awesome-seo (bmpi-dev)](https://github.com/bmpi-dev/awesome-seo) ![Active][Active Icon] — Google SEO 研究与流量变现资源。(2.8k★, MIT)
- [search-engine-optimization](https://github.com/marcobiedermann/search-engine-optimization) — 清单式 SEO 资源合集。(2.8k★, MIT)
- [awesome-seo-tools (serpapi)](https://github.com/serpapi/awesome-seo-tools) ![Active][Active Icon] — SEO 工具精选，含商业工具。(1.1k★)
- [awesome-seo (teles)](https://github.com/teles/awesome-seo) ![Active][Active Icon] — 通用 SEO 链接精选。(884★)

## 推荐组合

没有哪个开源工具能单挑 Semrush 或 Ahrefs，它们的护城河是外链库和搜索量数据。但执行层（审计、爬取、排名追踪、自有数据分析）已经成熟，组合一套能覆盖大部分日常需求。诚实的边界：要做竞品外链挖掘，留一个 Ahrefs/Semrush 只读账号买数据，执行和自有数据交给开源。

**小站 / 独立站**

- [SerpBear](https://github.com/towfiqi/serpbear)（排名） + [seonaut](https://github.com/StJudeWasHere/seonaut)（审计） + [Matomo](https://github.com/matomo-org/matomo) 或 [Plausible](https://github.com/plausible/analytics)（分析） + [lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci)（CI 检查）

**Agency**

- [Seo-Panel](https://github.com/sendtogeo/Seo-Panel)（多站管理） + [SerpBear](https://github.com/towfiqi/serpbear) + GSC 批量导出（[google-search-console-export-all](https://github.com/swalker-888/google-search-console-export-all)） + [seonaut](https://github.com/StJudeWasHere/seonaut) 做定期爬取

**开发者 / AI 工作流**

- [zens-ink](https://github.com/ZensInk/zens-ink-seo-package) 或 [RustySEO](https://www.rustyseo.com/) 打底 + [scrapy](https://github.com/scrapy/scrapy) 补定制爬取 + [goaccess](https://github.com/allinurl/goaccess) 看原始日志 + [seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) 做 LLM 辅助审计

## 贡献指南

欢迎提 PR——收录标准与条目格式见 [CONTRIBUTING.md](./CONTRIBUTING.md)。允许自荐，但请在 PR 里说明，和所有人一样。

## 许可

[CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/) — 本清单随意使用。

---

由 [ZensInk](https://zens.ink) 维护——面向独立开发者的零依赖、免费额度优先 SEO 工具集。

[CLI Icon]: media/cli.svg
[Self-host Icon]: media/selfhost.svg
[GEO Icon]: media/geo.svg
[Active Icon]: media/active.svg
