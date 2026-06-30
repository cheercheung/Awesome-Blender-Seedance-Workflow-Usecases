# Maintenance

## Source of Truth

- Public curated source: `blender-seedance-usecase-curated.json`
- Human-readable curated source: `blender-seedance-usecase-curated.md`
- Owner-provided input: `data/primary-use-case-posts.json`
- Manual originality audit: `docs/usecase-originality-audit.md`
- Downloaded public media: `media/case-XX/`

## Current State

- Selected public cases: 25
- Candidate pool before audit: 35
- Primary CTA: Quick Start workflow with Blender MCP, EvoLink skills, API key, and agent usage
- Public push: not approved
- GitHub repository creation: not approved; push target approved after local verification

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
