# Maintenance

## Source of Truth

- Public curated source: `blender-seedance-usecase-curated.json`
- Human-readable curated source: `blender-seedance-usecase-curated.md`
- Owner-provided input: `data/primary-use-case-posts.json`
- Owner-provided video source map: `data/usecase-video-sources.json`
- Manual originality audit: `docs/usecase-originality-audit.md`
- GitHub About metadata proposal: `docs/github-about.md`
- Downloaded public media: `media/caseN.mp4`

## Current State

- Selected public cases: 25
- Owner-provided video rows: 26
- Candidate pool before audit: 35
- Primary CTA: Quick Start workflow with Blender MCP, EvoLink skills, API key, and agent usage
- Public push: approved to the existing target repository after local verification
- GitHub repository creation: not approved and not needed for this repo
- GitHub About metadata: drafted in `docs/github-about.md`; applying it requires repository settings permission

## Case Rules

Each public case must include:

- Stable `<a id="case-x"></a>` anchor
- Source-linked `### Case X` heading
- Creator attribution
- Bold usage takeaway
- Source-grounded notes
- Local media links when the source data exposes media
- `Type: ... | Date: YYYY-MM-DD`

Never invent prompts, results, benchmark claims, availability, pricing, or creator attribution.
Do not re-add removed candidates without updating the audit file.

## Validation

```bash
python3 scripts/verify_repo.py
git diff --check
```

## Release Blockers

Replace the Quick Start destination with the final landing page once the owner provides it. Until then, `#quick-start` is the primary conversion anchor and should explain Blender MCP setup, EvoLink skill installation, API key setup, and agent usage.
