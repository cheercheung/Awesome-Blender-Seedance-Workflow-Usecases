<div align="center">

<a href="#quick-start"><img src="images/en.png" alt="Blender + Seedance usecase repository banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Use on EvoLink](https://img.shields.io/badge/Use_on-EvoLink-black)](#quick-start)
[![MCP + Skill](https://img.shields.io/badge/MCP_%2B_Skill-Pending-orange)](#quick-start)
[![Agent Workflow](https://img.shields.io/badge/Agent_Workflow-Pending-blue)](#quick-start)

[![English](https://img.shields.io/badge/English-111111)](README.md)
[![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md)
[![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md)
[![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md)
[![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md)
[![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md)
[![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md)
[![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md)
[![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md)
[![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

## 🍌 Introduction

Welcome to the Blender + Seedance usecase repository.

**We collect real-world Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI, and agent-assisted workflows that creators used to control Seedance video generation.**

The current collection is curated from user-provided X/Twitter source data. Each case links to the original post and creator profile.

The Quick Start below walks users through Blender MCP setup, EvoLink skill installation, API key setup, and running the workflow inside an agent.

## 📊 Overview

- **25 selected Blender + Seedance cases** from public creator posts in the owner-provided source dataset.
- Covers camera control, Blender previs, multi-character blocking, action choreography, Blender MCP, Codex/Claude-assisted blockouts, FBX/Mixamo references, ComfyUI/style transfer, and known limitations.
- Each case includes the original source, creator attribution, a concise takeaway, evidence type, and publication date.
- The public list was rebuilt from the 35-candidate audit plus the requested new links into 25 primary cases.
- Use this repo to inspect practical workflows before routing users to the final EvoLink MCP + skill landing page.

> [!NOTE]
> The collection favors concrete workflow evidence over hype: source-backed steps, reference-video methods, agent/MCP usage, reproducible constraints, and clearly stated limits.

<a id="quick-start"></a>
## ⚡ Quick Start Workflow

Set up the local Blender control path first, then install the EvoLink skills your agent will call.

### 1. Install Blender MCP

Follow the official Blender MCP setup guide, open Blender, and make sure your agent can connect to the Blender MCP server before generating references.

- Official setup: [Blender MCP setup](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

### 2. Install EvoLink skills

Install the Seedance generation skill and the Topaz upscaling skill in the agent workspace.

```bash
npm i evolink-seedance
npm i evolink-topaz-video-upscale
```

### 3. Get an API key

Create an EvoLink API key from your account, then expose it to the agent runtime.

```bash
export EVOLINK_API_KEY="<your-evolink-api-key>"
```

### 4. Run it inside your agent

After MCP, skills, and API key are ready, ask your agent to build a Blender blockout, export the reference video, generate with Seedance, and upscale the final clip when needed.

```text
Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.
```

> [!NOTE]
> The Blender MCP setup page is the source of truth for Blender-side installation details.

## 📑 Menu

| Section | Cases |
|---|---|
| [🎥 Camera Control & Previs](#camera-control-previs) | Case 1, 2, 3, 4, 5 |
| [🎬 Character & Action Blocking](#character-action-blocking) | Case 6, 8, 9, 21 |
| [🤖 Agentic Blender MCP](#agentic-blender-mcp) | Case 10, 11, 22 |
| [🧩 Reference, Prompt & Multi-Input Mapping](#reference-prompt-multi-input-mapping) | Case 13, 14, 23, 24, 26, 27 |
| [🛠️ Production Pipelines & Toolchains](#production-pipelines-toolchains) | Case 15, 16, 17, 18 |
| [🧪 Limits, Tests & Troubleshooting](#limits-tests-troubleshooting) | Case 20, 25, 28 |
| [🙏 Acknowledge](#acknowledge) | Credits and correction policy |

<a id="camera-control-previs"></a>
### 🎥 Camera Control & Previs

| Case | What it shows | Type |
|---|---|---|
| [Blender Blockout as Seedance Motion Reference](#case-1) | A merged direction workflow: use the full gray-box method from the original case, then push it into action-previs timing, speed, shake, and spatial choreography before Seedance generation. | Demo |
| [Camera Blocking with Midjourney Start Frame](#case-2) | A compact precision-camera recipe: Blender supplies the camera move, Midjourney supplies the start frame, and Seedance follows the motion reference. | Demo |
| [ComfyUI Camera Control with Blender Previs](#case-3) | A ComfyUI control case where Blender previz is combined with separate upright and upside-down reference frames to test motion adherence. | Demo |
| [Viewport Preview to Realistic Start Frame](#case-4) | A short viewport-preview tutorial: block out the scene, export the preview, turn the first frame realistic, then provide both references to Seedance. | Demo |
| [One Reference Video, Multiple Worlds](#case-5) | A style/world-variation case where the same Blender reference video drives different generated worlds in Seedance. | Demo |

<a id="character-action-blocking"></a>
### 🎬 Character & Action Blocking

| Case | What it shows | Type |
|---|---|---|
| [Multi-Character Dialogue with Matched Poses](#case-6) | A dialogue-shot workflow where Blender is used to match character poses and camera motion before Seedance generates the performed scene. | Demo |
| [Handheld Follow Camera through Space](#case-8) | A handheld-follow case where Blender controls how a character travels through space and Seedance carries the gritty camera move into the final video. | Demo |
| [Camera and Character Blocking for Tactical Action](#case-9) | A tactical blocking case where Blender directs camera orbit, lens choice, cover positions, gunfire beats, and character movement before generation. | Demo |
| [Ambush Scene Previs Beyond a Simple Camera Move](#case-21) | An ambush-scene case showing how Blender previs can solve staging, timing, and camera movement before Seedance generates the shot. | Demo |

<a id="agentic-blender-mcp"></a>
### 🤖 Agentic Blender MCP

| Case | What it shows | Type |
|---|---|---|
| [Codex + Blender MCP Reference Video Workflow](#case-10) | An agentic Blender MCP case where Codex builds a simple 3D market, cat motion, camera framing, and an MP4 reference for Seedance. | Integration |
| [Codex-Built Architecture and Camera Work](#case-11) | A Codex-assisted beginner case where architecture and camera work are generated in Blender and then tested as Seedance reference motion. | Integration |
| [Claude-Built Blender MCP Previs in Minutes](#case-22) | A fast agentic-previs case where Claude uses Blender MCP to build a shot reference in two to three minutes. | Integration |

<a id="reference-prompt-multi-input-mapping"></a>
### 🧩 Reference, Prompt & Multi-Input Mapping

| Case | What it shows | Type |
|---|---|---|
| [Reproducible Seedance Prompt with Blender Reference](#case-13) | A merged reproducibility and troubleshooting case: the setup spells out the reference-video conditions, while the paired test records where camera/rhythm control worked and foot motion failed. | Tutorial |
| [Mixamo Motion as Beginner Blender Reference](#case-14) | A beginner-friendly motion-source case: use Mixamo motion in Blender as the controllable movement base before sending the reference to Seedance. | Tutorial |
| [Position-Only Reference Control for a Faster Scene](#case-23) | A reference-weighting case: keep the reference useful for positions while letting the prompt recover speed and dynamism. | Tutorial |
| [Physical Toy Reference Instead of 3D Software](#case-24) | A physical-reference case: use toys as quick motion and staging references when opening Blender is too much overhead. | Demo |
| [Reference Control for a Specific Failed Prompt Scene](#case-26) | A control fallback case: when prompt-only generation fails, use a reference to force the scene even if some dynamism is reduced. | Demo |
| [Character Proportion and Simple Background Tips](#case-27) | A stability checklist case: match character proportions beyond height and simplify any background that does not need precise alignment. | Tutorial |

<a id="production-pipelines-toolchains"></a>
### 🛠️ Production Pipelines & Toolchains

| Case | What it shows | Type |
|---|---|---|
| [Hermes, Krea, ComfyUI and Blender MCP Stack](#case-15) | A multi-tool agent pipeline where Hermes installs and connects Krea, ComfyUI, Blender MCP, and Seedance to produce both image and physical references. | Integration |
| [Blender MCP Viewport to Seedance Style Transfer](#case-16) | A viewport-to-style-transfer case: Blender MCP provides camera and element control, then Seedance/Magnific add texture and lighting. | Integration |
| [Blender Previz to Anime Seedance Render](#case-17) | A 3D-previs-to-anime case showing how camera moves and motion can be preserved while Seedance changes the render style. | Integration |
| [FBX Clay Pass with Claude-Keyframed Camera](#case-18) | An FBX clay-pass workflow where Blender imports the motion, Claude helps keyframe camera moves, and the rendered pass becomes Seedance reference video. | Integration |

<a id="limits-tests-troubleshooting"></a>
### 🧪 Limits, Tests & Troubleshooting

| Case | What it shows | Type |
|---|---|---|
| [Reference-Only Blender Blockout without Start Frame](#case-20) | A no-start-frame variant showing that Blender blockout plus detailed environment references can work when the workflow cannot rely on a starter frame. | Limit |
| [Toy Reference Prompt Reinforcement and NG Example](#case-25) | A troubleshooting case showing why reference videos often need prompt reinforcement instead of raw imitation. | Limit |
| [Cloth Physics Stress Test with Blender and Seedance](#case-28) | A cloth-physics stress test showing where Blender-guided Seedance can work but still needs iteration for difficult motion. | Limit |

<a id="camera-control-previs-cases"></a>
## 🎥 Camera Control & Previs

<a id="case-1"></a>
### Case 1: [Blender Blockout as Seedance Motion Reference](https://x.com/noman23761/status/2071534020014563328) (by [@noman23761](https://x.com/noman23761))

**A merged direction workflow: use the full gray-box method from the original case, then push it into action-previs timing, speed, shake, and spatial choreography before Seedance generation.**

- Source notes: Merged with former case 7: together these sources show the full gray-box workflow and the action-previs variant with rough timing, speed, shake, and spatial choreography.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case1.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case1.mp4)

Type: Demo | Date: 2026-06-29

---

<a id="case-2"></a>
### Case 2: [Camera Blocking with Midjourney Start Frame](https://x.com/reidhannaford/status/2069074506849685773) (by [@reidhannaford](https://x.com/reidhannaford))

**A compact precision-camera recipe: Blender supplies the camera move, Midjourney supplies the start frame, and Seedance follows the motion reference.**

- Source notes: The source gives a clear three-step workflow and reports that the generated video tracks the Blender camera move closely.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case2.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case2.mp4)

Type: Demo | Date: 2026-06-22

---

<a id="case-3"></a>
### Case 3: [ComfyUI Camera Control with Blender Previs](https://x.com/JMSvid/status/2070258132840796579) (by [@JMSvid](https://x.com/JMSvid))

**A ComfyUI control case where Blender previz is combined with separate upright and upside-down reference frames to test motion adherence.**

- Source notes: The case is useful because it combines Blender previz with multiple still references inside a ComfyUI-style control setup.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case3.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case3.mp4)

Type: Demo | Date: 2026-06-25

---

<a id="case-4"></a>
### Case 4: [Viewport Preview to Realistic Start Frame](https://x.com/DiabloNemesis/status/2070441923706503380) (by [@DiabloNemesis](https://x.com/DiabloNemesis))

**A short viewport-preview tutorial: block out the scene, export the preview, turn the first frame realistic, then provide both references to Seedance.**

- Source notes: The post gives a concise workflow with concrete artifacts: viewport preview, first-frame image, and Seedance reference video. The requested case 29 media is an exact duplicate of this video, so it is linked here instead of becoming a second public case.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case4.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case4.mp4), [case29.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case29.mp4)

Type: Demo | Date: 2026-06-26

---

<a id="case-5"></a>
### Case 5: [One Reference Video, Multiple Worlds](https://x.com/koldo2k/status/2071307945002815967) (by [@koldo2k](https://x.com/koldo2k))

**A style/world-variation case where the same Blender reference video drives different generated worlds in Seedance.**

- Source notes: The source is useful because it separates motion control from world/style variation using the same reference video.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case5.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case5.mp4)

Type: Demo | Date: 2026-06-28

---

<a id="character-action-blocking-cases"></a>
## 🎬 Character & Action Blocking

<a id="case-6"></a>
### Case 6: [Multi-Character Dialogue with Matched Poses](https://x.com/reidhannaford/status/2069420552394043625) (by [@reidhannaford](https://x.com/reidhannaford))

**A dialogue-shot workflow where Blender is used to match character poses and camera motion before Seedance generates the performed scene.**

- Source notes: The source adds multi-character dialogue and pose matching, making it distinct from single-character camera-control demos.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case6.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case6.mp4)

Type: Demo | Date: 2026-06-23

---

<a id="case-8"></a>
### Case 8: [Handheld Follow Camera through Space](https://x.com/reidhannaford/status/2070507963429671062) (by [@reidhannaford](https://x.com/reidhannaford))

**A handheld-follow case where Blender controls how a character travels through space and Seedance carries the gritty camera move into the final video.**

- Source notes: The source moves the character through the scene while the camera follows, which makes it useful for handheld movement shots.
- Audit status: kept after manual duplicate and originality review.


Type: Demo | Date: 2026-06-26

---

<a id="case-9"></a>
### Case 9: [Camera and Character Blocking for Tactical Action](https://x.com/SamJWasserman/status/2070742850095230991) (by [@SamJWasserman](https://x.com/SamJWasserman))

**A tactical blocking case where Blender directs camera orbit, lens choice, cover positions, gunfire beats, and character movement before generation.**

- Source notes: The source shows simultaneous camera and character blocking, which is stronger than a simple camera-only reference.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case9.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case9.mp4)

Type: Demo | Date: 2026-06-27

---

<a id="case-21"></a>
### Case 21: [Ambush Scene Previs Beyond a Simple Camera Move](https://x.com/reidhannaford/status/2071595581508563168) (by [@reidhannaford](https://x.com/reidhannaford))

**An ambush-scene case showing how Blender previs can solve staging, timing, and camera movement before Seedance generates the shot.**

- Source notes: Requested as case 21. Kept as a distinct Reid Hannaford example because it pushes the workflow beyond a simple camera move into scene staging.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case21.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case21.mp4)

Type: Demo | Date: 2026-06-29

---

<a id="agentic-blender-mcp-cases"></a>
## 🤖 Agentic Blender MCP

<a id="case-10"></a>
### Case 10: [Codex + Blender MCP Reference Video Workflow](https://x.com/akiyoshisan/status/2071081230108660199) (by [@akiyoshisan](https://x.com/akiyoshisan))

**An agentic Blender MCP case where Codex builds a simple 3D market, cat motion, camera framing, and an MP4 reference for Seedance.**

- Source notes: The author says the test was inspired by another creator, but the described scene, motion, camera, and export process are their own experiment.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case10.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case10.mp4)

Type: Integration | Date: 2026-06-28

---

<a id="case-11"></a>
### Case 11: [Codex-Built Architecture and Camera Work](https://x.com/6_KAKUU/status/2071051063663452374) (by [@6_KAKUU](https://x.com/6_KAKUU))

**A Codex-assisted beginner case where architecture and camera work are generated in Blender and then tested as Seedance reference motion.**

- Source notes: The post is valuable as a beginner Codex workflow: the user delegates architecture and camera work to Codex before Seedance.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case11.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case11.mp4)

Type: Integration | Date: 2026-06-28

---

<a id="case-22"></a>
### Case 22: [Claude-Built Blender MCP Previs in Minutes](https://x.com/JoshDaws/status/2071401550845481090) (by [@JoshDaws](https://x.com/JoshDaws))

**A fast agentic-previs case where Claude uses Blender MCP to build a shot reference in two to three minutes.**

- Source notes: Requested as case 22. Kept because it demonstrates speed and agent control rather than manual Blender work.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case22.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case22.mp4)

Type: Integration | Date: 2026-06-29

---

<a id="reference-prompt-multi-input-mapping-cases"></a>
## 🧩 Reference, Prompt & Multi-Input Mapping

<a id="case-13"></a>
### Case 13: [Reproducible Seedance Prompt with Blender Reference](https://x.com/aidoga_lab/status/2070864815275585913) (by [@aidoga_lab](https://x.com/aidoga_lab))

**A merged reproducibility and troubleshooting case: the setup spells out the reference-video conditions, while the paired test records where camera/rhythm control worked and foot motion failed.**

- Source notes: Merged with former case 19: the pair keeps both the reproducible setup and the limitation note about foot sliding.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case13.jpg](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case13.jpg), [case13.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case13.mp4), [case19.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case19.mp4)

Type: Tutorial | Date: 2026-06-27

---

<a id="case-14"></a>
### Case 14: [Mixamo Motion as Beginner Blender Reference](https://x.com/tanabe_fragm/status/2070685291183243459) (by [@tanabe_fragm](https://x.com/tanabe_fragm))

**A beginner-friendly motion-source case: use Mixamo motion in Blender as the controllable movement base before sending the reference to Seedance.**

- Source notes: The source is useful for beginners because it names Mixamo as a practical motion source for Blender reference videos.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case14.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case14.mp4)

Type: Tutorial | Date: 2026-06-27

---

<a id="case-23"></a>
### Case 23: [Position-Only Reference Control for a Faster Scene](https://x.com/kan_mi_no9/status/2071380621214224403) (by [@kan_mi_no9](https://x.com/kan_mi_no9))

**A reference-weighting case: keep the reference useful for positions while letting the prompt recover speed and dynamism.**

- Source notes: Requested as case 23. Kept with the paired kan_mi_no9 test as a distinct reference-control variant.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case23.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case23.mp4)

Type: Tutorial | Date: 2026-06-28

---

<a id="case-24"></a>
### Case 24: [Physical Toy Reference Instead of 3D Software](https://x.com/gcduncombe/status/2070617538745229546) (by [@gcduncombe](https://x.com/gcduncombe))

**A physical-reference case: use toys as quick motion and staging references when opening Blender is too much overhead.**

- Source notes: Requested as case 24. Kept because it expands the reference-video idea beyond software-only previs.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case24.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case24.mp4)

Type: Demo | Date: 2026-06-26

---

<a id="case-26"></a>
### Case 26: [Reference Control for a Specific Failed Prompt Scene](https://x.com/kan_mi_no9/status/2071168235022827587) (by [@kan_mi_no9](https://x.com/kan_mi_no9))

**A control fallback case: when prompt-only generation fails, use a reference to force the scene even if some dynamism is reduced.**

- Source notes: Requested as case 26. Kept as the practical counterpart to the later kan_mi_no9 variation case.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case26.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case26.mp4)

Type: Demo | Date: 2026-06-28

---

<a id="case-27"></a>
### Case 27: [Character Proportion and Simple Background Tips](https://x.com/craftcapitallab/status/2070512271391068287) (by [@craftcapitallab](https://x.com/craftcapitallab))

**A stability checklist case: match character proportions beyond height and simplify any background that does not need precise alignment.**

- Source notes: Requested as case 27. Kept because it offers specific, reusable setup advice.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case27.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case27.mp4)

Type: Tutorial | Date: 2026-06-26

---

<a id="production-pipelines-toolchains-cases"></a>
## 🛠️ Production Pipelines & Toolchains

<a id="case-15"></a>
### Case 15: [Hermes, Krea, ComfyUI and Blender MCP Stack](https://x.com/SamJWasserman/status/2069656428437225826) (by [@SamJWasserman](https://x.com/SamJWasserman))

**A multi-tool agent pipeline where Hermes installs and connects Krea, ComfyUI, Blender MCP, and Seedance to produce both image and physical references.**

- Source notes: The case demonstrates a broader agent-built creative stack, not just manual Blender previs.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case15.jpg](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case15.jpg), [case15.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case15.mp4)

Type: Integration | Date: 2026-06-24

---

<a id="case-16"></a>
### Case 16: [Blender MCP Viewport to Seedance Style Transfer](https://x.com/techhalla/status/2070814203435274715) (by [@techhalla](https://x.com/techhalla))

**A viewport-to-style-transfer case: Blender MCP provides camera and element control, then Seedance/Magnific add texture and lighting.**

- Source notes: This is the stronger techhalla source because it explains the viewport animation and downstream style/lighting step.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case16.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case16.mp4)

Type: Integration | Date: 2026-06-27

---

<a id="case-17"></a>
### Case 17: [Blender Previz to Anime Seedance Render](https://x.com/restofart/status/2070086939756159368) (by [@restofart](https://x.com/restofart))

**A 3D-previs-to-anime case showing how camera moves and motion can be preserved while Seedance changes the render style.**

- Source notes: The source directly frames the workflow as Blender 3D previz transformed into an anime render while keeping camera motion.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case17.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case17.mp4)

Type: Integration | Date: 2026-06-25

---

<a id="case-18"></a>
### Case 18: [FBX Clay Pass with Claude-Keyframed Camera](https://x.com/Viggle_PINOC/status/2070183934265012392) (by [@Viggle_PINOC](https://x.com/Viggle_PINOC))

**An FBX clay-pass workflow where Blender imports the motion, Claude helps keyframe camera moves, and the rendered pass becomes Seedance reference video.**

- Source notes: The source gives a specific FBX-to-clay-pass process and includes camera keyframing before reference export.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case18.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case18.mp4)

Type: Integration | Date: 2026-06-25

---

<a id="limits-tests-troubleshooting-cases"></a>
## 🧪 Limits, Tests & Troubleshooting

<a id="case-20"></a>
### Case 20: [Reference-Only Blender Blockout without Start Frame](https://x.com/magneticskiff/status/2070711034793361559) (by [@magneticskiff](https://x.com/magneticskiff))

**A no-start-frame variant showing that Blender blockout plus detailed environment references can work when the workflow cannot rely on a starter frame.**

- Source notes: This case covers an important variant where reference images replace the usual start-frame dependency.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case20.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case20.mp4)

Type: Limit | Date: 2026-06-27

---

<a id="case-25"></a>
### Case 25: [Toy Reference Prompt Reinforcement and NG Example](https://x.com/tea_story_hoshi/status/2071002538703479089) (by [@tea_story_hoshi](https://x.com/tea_story_hoshi))

**A troubleshooting case showing why reference videos often need prompt reinforcement instead of raw imitation.**

- Source notes: Requested as case 25. Kept because it includes both working examples and a failed comparison.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case25.jpg](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case25.jpg), [case25.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case25.mp4)

Type: Limit | Date: 2026-06-27

---

<a id="case-28"></a>
### Case 28: [Cloth Physics Stress Test with Blender and Seedance](https://x.com/fatboypink/status/2070577334701473800) (by [@fatboypink](https://x.com/fatboypink))

**A cloth-physics stress test showing where Blender-guided Seedance can work but still needs iteration for difficult motion.**

- Source notes: Requested as case 28. Kept as a concrete limitation/stress-test case.
- Audit status: kept after manual duplicate and originality review.
- Local media: [case28.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case28.mp4)

Type: Limit | Date: 2026-06-26

---

<a id="acknowledge"></a>
## 🙏 Acknowledge

This repository was inspired by creators who publicly shared Blender + Seedance workflows, tests, prompts, reference videos, and production notes.

- [@noman23761](https://x.com/noman23761)
- [@reidhannaford](https://x.com/reidhannaford)
- [@JMSvid](https://x.com/JMSvid)
- [@DiabloNemesis](https://x.com/DiabloNemesis)
- [@koldo2k](https://x.com/koldo2k)
- [@SamJWasserman](https://x.com/SamJWasserman)
- [@akiyoshisan](https://x.com/akiyoshisan)
- [@6_KAKUU](https://x.com/6_KAKUU)
- [@aidoga_lab](https://x.com/aidoga_lab)
- [@tanabe_fragm](https://x.com/tanabe_fragm)
- [@techhalla](https://x.com/techhalla)
- [@restofart](https://x.com/restofart)
- [@Viggle_PINOC](https://x.com/Viggle_PINOC)
- [@magneticskiff](https://x.com/magneticskiff)
- [@JoshDaws](https://x.com/JoshDaws)
- [@kan_mi_no9](https://x.com/kan_mi_no9)
- [@gcduncombe](https://x.com/gcduncombe)
- [@tea_story_hoshi](https://x.com/tea_story_hoshi)
- [@craftcapitallab](https://x.com/craftcapitallab)
- [@fatboypink](https://x.com/fatboypink)

*We cannot guarantee that every case is attributed to the original creator. If anything needs to be corrected, please contact us and we will update it.*

If you have more interesting usage cases to share, open an issue or pull request and help expand the EvoLink usecase library.

[![Star History Chart](https://api.star-history.com/svg?repos=cheercheung/Awesome-Blender-Seedance-Workflow-Usecases&type=Date)](https://www.star-history.com/#cheercheung/Awesome-Blender-Seedance-Workflow-Usecases&Date)

