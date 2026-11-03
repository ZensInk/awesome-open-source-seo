# Contributing

PRs welcome. Before you open one, check the list — both [README.md](./README.md) and [README.zh.md](./README.zh.md) — and the search — your tool may already be here, possibly under a different category.

## Criteria

A project qualifies if it:

1. Is source-available under an open license, or explicitly licensed in the repo
2. Actually runs — you can install and execute it yourself
3. Does SEO/GEO work (tools, not content, not courses)
4. Is not a fork of an entry already listed

Self-promotion is allowed but disclose it in the PR, like everyone else does.

## Entry format

One line per tool, placed in the right category (create a subcategory only if you're adding 3+ tools that fit it). Add it to **both** language versions — `README.md` and `README.zh.md`:

```markdown
- [name](https://github.com/owner/repo) ![CLI][CLI Icon] ![Active][Active Icon] — One-sentence description of what it does and why it matters. (1.5k★, MIT)
```

```markdown
- [name](https://github.com/owner/repo) ![CLI][CLI Icon] ![Active][Active Icon] — 一句话说清它做什么、为什么值得用。(1.5k★, MIT)
```

Rules:

- **Both languages**: the Chinese line is a real translation, not a machine dump, and goes in the same category as the English one. PRs that only touch one file are asked to add the other

- **Star count** comes from the live API — any number works, the bot will correct it on the next monthly refresh
- **License** goes inside the parens after the star count, if the repo states one
- **Badges**: add `![CLI][CLI Icon]` (runs from a terminal), `![Self-host][Self-host Icon]` (self-hostable web app), `![GEO/AI][GEO Icon]` (targets AI-search visibility) as applicable. **Don't add `![Active][Active Icon]` manually** — the bot adds or removes it based on the last 12 months of commits
- Describe what the tool does, not marketing copy

## What happens after you PR

A GitHub Action runs [`scripts/refresh.py`](./scripts/refresh.py) monthly: star counts update, Active badges are re-evaluated, archived repos get flagged with ⚠️, and 404s get reported for removal. Your entry stays honest without anyone hand-editing numbers.
