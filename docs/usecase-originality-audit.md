# Use Case Originality Audit

Date: 2026-06-29
Updated: 2026-06-30

Scope: manual review of the 35 source posts in `data/primary-use-case-posts.md` and the corresponding curated records. The goal is to separate original creator posts from reposts, thread fragments, repeated variants, and weak non-use-case material before the public README is treated as a final use case repository.

## Summary

- Reviewed source text for all 35 candidates one by one.
- No exact repost or third-party repost was proven from the available source text and local metadata.
- Several posts are still not good standalone use cases: they are thread continuations, same-author repeated variants, thin showcases, or opinion/speculation rather than an executable workflow.
- 2026-06-29 baseline: public primary list was reduced from 35 to 20 cases.
- 2026-06-30 update: the public list was rebuilt to 25 cases after merging case 7 into case 1, merging case 19 into case 13, adding requested cases 21-28, and treating requested case 29 as a duplicate media file for the existing DiabloNemesis case.
- Removed items must not be described as "stolen" or "reposted" unless later live-source verification proves that. The current evidence supports "not final primary use case" rather than "confirmed repost" for most removed items.

## 2026-06-30 Update

Current public case labels are:

`1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28`

Implementation notes:

- Former case 7 is merged into case 1. Its playable media is now `media/case1.mp4`.
- Former case 19 is merged into case 13. Its playable media is now linked from case 13 as `media/case19.mp4`.
- Requested new cases 21-28 were added from the supplied X/Twitter URLs.
- Requested case 29, `https://x.com/DiabloNemesis/status/2070441923706503380`, is the same source as existing case 4. `media/case4.mp4` and `media/case29.mp4` have the same SHA-256 hash, so case 29 is not duplicated as a separate public use case.
- The current public README files link 29 local media files through GitHub raw URLs so videos can be opened directly.

## 2026-06-29 Baseline Keep List

These 20 were kept as the 2026-06-29 baseline because each had a distinct workflow, constraint, or production angle. The 2026-06-30 update above supersedes the final public count.

| Source # | Source | Author | Decision | Reason |
|---:|---|---|---|---|
| 1 | https://x.com/noman23761/status/2071534020014563328 | @noman23761 | Keep | Complete start-frame, Blender gray-box, camera animation, and Seedance motion-reference workflow. |
| 2 | https://x.com/reidhannaford/status/2069074506849685773 | @reidhannaford | Keep | Clear three-step precision camera control workflow with Blender motion reference and Midjourney start frame. |
| 3 | https://x.com/reidhannaford/status/2069420552394043625 | @reidhannaford | Keep | Distinct multi-character dialogue case with matched poses and camera movement. |
| 5 | https://x.com/reidhannaford/status/2070145120658137385 | @reidhannaford | Keep | Distinct action-choreography case with rough timing, shake, speed, and spatial blocking. |
| 6 | https://x.com/reidhannaford/status/2070507963429671062 | @reidhannaford | Keep | Distinct handheld-follow case where the character moves through space. |
| 7 | https://x.com/aidoga_lab/status/2070864815275585913 | @aidoga_lab | Keep | Reproducible setup with start frame, Blender reference video, Seedance version, duration, and prompt conditions. |
| 8 | https://x.com/aidoga_lab/status/2070864749865398684 | @aidoga_lab | Keep | Useful limitation case: camera, rhythm, and movement worked, but foot motion did not. |
| 9 | https://x.com/akiyoshisan/status/2071081230108660199 | @akiyoshisan | Keep | Inspired by another creator but describes the author's own Codex + Blender MCP test and production steps. |
| 10 | https://x.com/AIWarper/status/2069481237308452916 | @AIWarper | Keep | Strong prompt/reference-mapping case with multiple character and environment references. |
| 14 | https://x.com/JMSvid/status/2070258132840796579 | @JMSvid | Keep | Distinct ComfyUI control setup with Blender previz plus reference frames. |
| 19 | https://x.com/SamJWasserman/status/2070742850095230991 | @SamJWasserman | Keep | Tactical action case controlling camera orbit, lens choice, cover positions, and character blocking. |
| 20 | https://x.com/SamJWasserman/status/2069656428437225826 | @SamJWasserman | Keep | Distinct multi-tool agent workflow using Krea, ComfyUI, Blender MCP, and Seedance. |
| 21 | https://x.com/techhalla/status/2070814203435274715 | @techhalla | Keep | Strong Blender MCP viewport-to-Seedance style/lighting workflow; the paired shorter post is removed. |
| 23 | https://x.com/tanabe_fragm/status/2070685291183243459 | @tanabe_fragm | Keep | Beginner path using Mixamo motion imported into Blender before Seedance. |
| 24 | https://x.com/6_KAKUU/status/2071051063663452374 | @6_KAKUU | Keep | Codex-assisted Blender architecture and camera work from a beginner perspective. |
| 25 | https://x.com/restofart/status/2070086939756159368 | @restofart | Keep | 3D previz to anime render pipeline with camera and motion preservation. |
| 28 | https://x.com/DiabloNemesis/status/2070441923706503380 | @DiabloNemesis | Keep | Clear viewport-preview workflow: block out scene, export preview, extract first frame, then use Seedance. |
| 29 | https://x.com/Viggle_PINOC/status/2070183934265012392 | @Viggle_PINOC | Keep | FBX-to-clay-pass process with Claude-keyframed camera moves and Seedance reference export. |
| 31 | https://x.com/magneticskiff/status/2070711034793361559 | @magneticskiff | Keep | Distinct no-start-frame workflow using references plus Blender blockout. |
| 32 | https://x.com/koldo2k/status/2071307945002815967 | @koldo2k | Keep | Distinct same-reference-video, different-worlds variation case. |

## Removed From Primary List

These 15 should be removed from the public primary use case list. "Originality" means the available text does not prove a repost; "Removal reason" explains why it is not kept as a standalone public use case.

| Source # | Source | Author | Originality judgement | Removal reason |
|---:|---|---|---|---|
| 4 | https://x.com/reidhannaford/status/2069783215829569746 | @reidhannaford | Likely original | Same-author variant of the Reid Hannaford camera/blocking series; lower information density than kept cases 2, 3, 5, and 6. |
| 11 | https://x.com/AIWarper/status/2069847776620589430 | @AIWarper | Likely original | Reads as a continuation step for importing/exporting FBX clips, not a full standalone use case. |
| 12 | https://x.com/AIWarper/status/2070162937181065547 | @AIWarper | Likely original | Teaser-style "details below" post; the concrete AIWarper reference-mapping case is kept as source 10. |
| 13 | https://x.com/AIWarper/status/2070535586075885912 | @AIWarper | Likely original | One-prompt blockout experiment, but the text says Seedance adaptation is still unresolved; weak as a completed public case. |
| 15 | https://x.com/KimAkiyama81/status/2070668362229690789 | @KimAkiyama81 | Likely original | Thin showcase statement without enough workflow detail. |
| 16 | https://x.com/KimAkiyama81/status/2070266267051667505 | @KimAkiyama81 | Likely original | Thin viewport-preview teaser that points below; not enough standalone detail. |
| 17 | https://x.com/ai_gezgini/status/2070531406237728977 | @ai_gezgini | Likely original | General director checklist; useful as a principle, but less concrete than kept workflow cases. |
| 18 | https://x.com/ai_gezgini/status/2071529677353615522 | @ai_gezgini | Likely original | Same-author checklist variant for an action scene; overlaps source 17 and lacks separate workflow proof. |
| 22 | https://x.com/techhalla/status/2070832621328732396 | @techhalla | Likely original | Short paired post pointing to the style-transfer workflow below; source 21 is the stronger standalone version. |
| 26 | https://x.com/Flagiuss/status/2071335816190902624 | @Flagiuss | Likely original | Opinion/speculation about future navigation-style filmmaking, not a concrete use case. |
| 27 | https://x.com/Ukiyo_il/status/2071098235268071877 | @Ukiyo_il | Likely original | Beginner experiment, but the useful workflow is vague and the result is described as not working well. |
| 30 | https://x.com/VengadaS65199/status/2070049247823859770 | @VengadaS65199 | Likely original | Interesting hybrid film note, but Blender's exact role is broad post-production rather than a clear Seedance control method. |
| 33 | https://x.com/dave392750/status/2070851042661810551 | @dave392750 | Likely original | Troubleshooting note about Mixamo/storyboarding, but less clear as a public reusable workflow. |
| 34 | https://x.com/Toshi_nyaruo_AI/status/2071149652905537541 | @Toshi_nyaruo_AI | Likely original | Beginner Codex MCP export note overlaps stronger kept agentic examples. |
| 35 | https://x.com/Gen_x111x/status/2069803766581526534 | @Gen_x111x | Likely original | Multi-reference composition idea is relevant, but workflow detail is thinner than the kept reference-mapping cases. |

## Duplicate And Repost Findings

- Confirmed exact reposts inside the 35: none from local text and metadata.
- Confirmed derivative/aggregator posts inside the 35: none from local `source_role`; all 35 were tagged `primary_original`, but that tag alone was not accepted as final evidence.
- Same-author duplicate or near-duplicate clusters:
  - @reidhannaford: sources 2, 3, 4, 5, 6. Keep 2, 3, 5, 6; remove 4 as the lowest-information repeated variant.
  - @AIWarper: sources 10, 11, 12, 13. Keep 10; remove 11, 12, 13 as supporting or unresolved fragments.
  - @KimAkiyama81: sources 15, 16. Remove both; neither has enough standalone workflow detail.
  - @ai_gezgini: sources 17, 18. Remove both from primary list; they are checklist-style direction notes rather than demonstrable use cases.
  - @techhalla: sources 21, 22. Keep 21; remove 22 as the paired short pointer.
  - @SamJWasserman: sources 19, 20. Keep both; they are distinct tactical-blocking and multi-tool agent pipeline cases.
  - @aidoga_lab: sources 7, 8. Keep both; one is a reproducible prompt/setup, the other is a limitation/troubleshooting case.

## 2026-06-29 Implementation Decision

The 2026-06-29 public repo presented 20 primary cases. After the 2026-06-30 update, the public repo presents 25 cases and keeps the older removed candidates only in internal source data or audit history, not in the 11 public README files or `blender-seedance-usecase-curated.*`.
