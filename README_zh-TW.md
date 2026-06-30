<div align="center">

<a href="#quick-start"><img src="images/zh-tw.png" alt="Blender + Seedance usecase repository banner" width="760"></a>

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

Blender + Seedance 使用案例倉庫。

**這裡收集真實的 Blender、Blender MCP、viewport、previs、FBX、Mixamo、ComfyUI 和 agent 輔助工作流，用來控制 Seedance 影片生成。**

目前集合來自使用者提供的 X/Twitter 精選資料。每個案例都連結到原帖和創作者主頁。

下面的 Quick Start 會引導使用者完成 Blender MCP setup、安裝 EvoLink skills、配置 API key，並在自己的 agent 裡執行。

## 📊 Overview

- **25 個精選 Blender + Seedance 案例**，來自使用者提供資料集中公開創作者貼文。
- 涵蓋相機控制、Blender previs、多角色 blocking、動作編排、Blender MCP、Codex/Claude 輔助 blockout、FBX/Mixamo 參考、ComfyUI/style transfer 和已知限制。
- 每個案例都包含原始來源、創作者署名、簡明 takeaway、證據類型和發布日期。
- 公開列表基於 35 個候選審計結果和這次新增連結，重建為 25 個主案例。
- 這個倉庫用於先展示真實工作流，再把使用者引導到最終 EvoLink MCP + skill 落地頁。

> [!NOTE]
> 這個集合優先保留具體證據：步驟、參考影片、agent/MCP 用法、可重現條件和明確限制，而不是空泛宣傳。

<a id="quick-start"></a>
## ⚡ Quick Start 工作流

先把本地 Blender 控制鏈路搭好，再安裝 agent 會呼叫的 EvoLink skills。

### 1. 安裝 Blender MCP

按照官方 Blender MCP setup 頁面完成配置，開啟 Blender，並在生成參考影片之前確認 agent 能連接到 Blender MCP server。

- 官方 setup: [Blender MCP setup](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

### 2. 安裝 EvoLink skills

在 agent workspace 裡安裝 Seedance 生成 skill 和 Topaz 影片放大 skill。

```bash
npm i evolink-seedance
npm i evolink-topaz-video-upscale
```

### 3. 取得 API key

在 EvoLink 帳號裡建立 API key，然後把它暴露給 agent runtime。

```bash
export EVOLINK_API_KEY="<your-evolink-api-key>"
```

### 4. 在自己的 agent 裡執行

MCP、skills 和 API key 都準備好之後，就可以讓 agent 建立 Blender blockout、匯出參考影片、呼叫 Seedance 生成，並在需要時用 Topaz 放大最終影片。

```text
Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.
```

> [!NOTE]
> Blender 側安裝細節以 Blender MCP setup 頁面為準。

## 📑 目錄

| 章節 | 案例 |
|---|---|
| [🎥 Camera Control & Previs / 相機控制與預演](#camera-control-previs) | Case 1, 2, 3, 4, 5 |
| [🎬 Character & Action Blocking / 角色與動作 blocking](#character-action-blocking) | Case 6, 8, 9, 21 |
| [🤖 Agentic Blender MCP / Agent 輔助 Blender MCP](#agentic-blender-mcp) | Case 10, 11, 22 |
| [🧩 Reference, Prompt & Multi-Input Mapping / 參考、prompt 與多輸入映射](#reference-prompt-multi-input-mapping) | Case 13, 14, 23, 24, 26, 27 |
| [🛠️ Production Pipelines & Toolchains / 生產管線與工具鏈](#production-pipelines-toolchains) | Case 15, 16, 17, 18 |
| [🧪 Limits, Tests & Troubleshooting / 限制、測試與排查](#limits-tests-troubleshooting) | Case 20, 25, 28 |
| [🙏 致謝](#acknowledge) | Credits and correction policy |

<a id="camera-control-previs"></a>
### 🎥 Camera Control & Previs / 相機控制與預演

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [Blender 灰盒預演 + 起始幀 + Seedance motion reference](#case-1) | 合并后的導演流程：保留原始灰盒方法，再加入動作預演里的时序、速度、抖動和空间调度，最后交给 Seedance 生成。 | Demo |
| [Blender 运鏡參考 + Midjourney 起始幀 + Seedance](#case-2) | 精确运鏡的三步配方：Blender 负责相机运動，Midjourney 负责起始幀，Seedance 按參考运動生成影片。 | Demo |
| [Blender previz + Comfy + 三輸入控制](#case-3) | ComfyUI 控制案例：Blender previz 搭配 upright/upside-down 參考幀，测試 Seedance 的运動遵循能力。 | Demo |
| [Viewport preview 導出后进 Seedance](#case-4) | Viewport preview 教程：blockout 場景、導出預覽、把首幀轉成真實圖，再把两类參考交给 Seedance。 | Demo |
| [同一 reference video 生成不同世界](#case-5) | 同一參考影片生成不同世界：用同一段 Blender reference 锁定运動，再让 Seedance 改变世界和风格。 | Demo |

<a id="character-action-blocking"></a>
### 🎬 Character & Action Blocking / 角色與動作 blocking

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [多角色 + 對話 + 精准运鏡](#case-6) | 多角色對話鏡头：先在 Blender 里匹配角色姿势和相机运動，再让 Seedance 生成表演结果。 | Demo |
| [手持跟拍 + 角色绕车运動](#case-8) | 手持跟拍：Blender 控制角色穿越空间和相机跟随，Seedance 把这种粗粝跟拍感带到最终影片。 | Demo |
| [角色 blocking + 相机 blocking 同时控制](#case-9) | 战术動作 blocking：在生成前用 Blender 规划相机环绕、鏡头、掩体位置、枪火節奏和角色移動。 | Demo |
| [伏击場景 previs + Seedance 動作调度](#case-21) | 伏击場景案例：先用 Blender previs 解决 staging、timing 和 camera movement，再交给 Seedance 生成鏡头。 | Demo |

<a id="agentic-blender-mcp"></a>
### 🤖 Agentic Blender MCP / Agent 輔助 Blender MCP

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [Codex + Blender MCP 生成場景/動作/参照影片](#case-10) | Agentic Blender MCP 案例：Codex 生成簡易市場、貓的動作、相机構圖，并導出给 Seedance 的 MP4 參考。 | Integration |
| [Codex 生成 Blender 建筑和 camera work 后送 Seedance](#case-11) | Codex 辅助新手案例：建筑和 camera work 由 Codex 在 Blender 中生成，再测試 Seedance 參考运動。 | Integration |
| [Claude 用 Blender MCP 几分钟生成 previs](#case-22) | 快速 agentic previs 案例：Claude 通过 Blender MCP 在 2-3 分钟内搭出鏡头參考。 | Integration |

<a id="reference-prompt-multi-input-mapping"></a>
### 🧩 Reference, Prompt & Multi-Input Mapping / 參考、prompt 與多輸入映射

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [日本語複現條件 + 完整 prompt](#case-13) | 合并后的複現与排查案例：一條寫清參考影片條件，另一條记录相机/節奏控制有效但脚步動作仍会失败。 | Tutorial |
| [Mixamo motion + Blender + Seedance 初学者路径](#case-14) | 新手运動来源案例：从 Mixamo 拿動作導入 Blender，作为可控运動基础后再送入 Seedance。 | Tutorial |
| [只保留位置关系的參考控制](#case-23) | 參考权重案例：只让參考影片约束位置关系，再用 prompt 补回速度感和動态感。 | Tutorial |
| [用實体玩具替代 3D 软件做參考](#case-24) | 實体參考案例：当不想打开 Blender 时，用玩具快速拍攝运動和 staging 參考。 | Demo |
| [用參考控制修複 prompt 反複失败的場景](#case-26) | 控制兜底案例：prompt-only 反複失败时，用 reference 强制場景成立，即使会损失部分動态。 | Demo |
| [角色比例与簡化背景的稳定性技巧](#case-27) | 稳定性 checklist：角色比例不只看头身，还要匹配手脚体积；无须對齐的背景尽量簡化。 | Tutorial |

<a id="production-pipelines-toolchains"></a>
### 🛠️ Production Pipelines & Toolchains / 生產管線與工具鏈

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [Hermes/Krea2/ComfyUI/Blender MCP/Seedance 實驗](#case-15) | 多工具 agent 管线：Hermes 安装并連接 Krea、ComfyUI、Blender MCP 和 Seedance，生成圖像与物理參考。 | Integration |
| [Blender MCP viewport animation + Seedance/Magnific texture/lighting](#case-16) | Viewport 到风格化案例：Blender MCP 提供相机和元素控制，再用 Seedance/Magnific 加纹理和光照。 | Integration |
| [Blender 3D previz → Seedance anime render](#case-17) | 3D previz 到動画渲染：用 Seedance 改变画面风格，同时保留 Blender 里的相机运動和動作。 | Integration |
| [FBX clay model + Claude keyframe + Seedance refs](#case-18) | FBX clay pass 流程：Blender 導入動作，Claude 辅助关键幀相机，渲染后的 clay pass 成为 Seedance 參考影片。 | Integration |

<a id="limits-tests-troubleshooting"></a>
### 🧪 Limits, Tests & Troubleshooting / 限制、測試與排查

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [不用 start frame 的 Blender blockout reference](#case-20) | 无起始幀变体：当不能依赖 starter frame 时，用 Blender blockout 加详细环境參考也能工作。 | Limit |
| [玩具參考 + prompt 补强 + NG 對照](#case-25) | 排查案例：參考影片通常需要 prompt 补强，不能只让模型机械照搬。 | Limit |
| [Blender + Seedance 布料物理压力测試](#case-28) | 布料物理压力测試：Blender-guided Seedance 可用，但複杂运動仍需要多轮迭代。 | Limit |

<a id="camera-control-previs-cases"></a>
## 🎥 Camera Control & Previs / 相機控制與預演

<a id="case-1"></a>
### Case 1: [Blender 灰盒預演 + 起始幀 + Seedance motion reference](https://x.com/noman23761/status/2071534020014563328) (by [@noman23761](https://x.com/noman23761))

**合并后的導演流程：保留原始灰盒方法，再加入動作預演里的时序、速度、抖動和空间调度，最后交给 Seedance 生成。**

- 來源筆記：完整说明从 image model 起始幀、Blender 灰盒場景/相机動画，到 Seedance 參考影片生成的端到端流程。
- 複用角度：可直接改寫成“用 Blender blockout 精准導演 AI 鏡头”的主 use case。
- 本地媒體: [case1.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case1.mp4)

類型: Demo | 日期: 2026-06-29

---

<a id="case-2"></a>
### Case 2: [Blender 运鏡參考 + Midjourney 起始幀 + Seedance](https://x.com/reidhannaford/status/2069074506849685773) (by [@reidhannaford](https://x.com/reidhannaford))

**精确运鏡的三步配方：Blender 负责相机运動，Midjourney 负责起始幀，Seedance 按參考运動生成影片。**

- 來源筆記：列出 3 步 workflow：Blender block camera、Midjourney start frame、两者送入 Seedance。
- 複用角度：适合做 precision camera control 的基础案例。
- 本地媒體: [case2.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case2.mp4)

類型: Demo | 日期: 2026-06-22

---

<a id="case-3"></a>
### Case 3: [Blender previz + Comfy + 三輸入控制](https://x.com/JMSvid/status/2070258132840796579) (by [@JMSvid](https://x.com/JMSvid))

**ComfyUI 控制案例：Blender previz 搭配 upright/upside-down 參考幀，测試 Seedance 的运動遵循能力。**

- 來源筆記：说明用 Blender previz 作为 guide，并配 upright/upside-down reference frames。
- 複用角度：适合做多輸入相机控制 case。
- 本地媒體: [case3.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case3.mp4)

類型: Demo | 日期: 2026-06-25

---

<a id="case-4"></a>
### Case 4: [Viewport preview 導出后进 Seedance](https://x.com/DiabloNemesis/status/2070441923706503380) (by [@DiabloNemesis](https://x.com/DiabloNemesis))

**Viewport preview 教程：blockout 場景、導出預覽、把首幀轉成真實圖，再把两类參考交给 Seedance。**

- 來源筆記：明确流程：Blender block out scene、export viewport preview、抽第一幀轉真實圖、作为 reference 送 Seedance。
- 複用角度：适合做 viewport preview → Seedance 的短教程案例。
- 本地媒體: [case4.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case4.mp4), [case29.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case29.mp4)

類型: Demo | 日期: 2026-06-26

---

<a id="case-5"></a>
### Case 5: [同一 reference video 生成不同世界](https://x.com/koldo2k/status/2071307945002815967) (by [@koldo2k](https://x.com/koldo2k))

**同一參考影片生成不同世界：用同一段 Blender reference 锁定运動，再让 Seedance 改变世界和风格。**

- 來源筆記：说明用 Blender 控制、Seedance 想象，同一 reference video 生成不同 worlds，并提到 prompt。
- 複用角度：适合做 style/world variation case。
- 本地媒體: [case5.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case5.mp4)

類型: Demo | 日期: 2026-06-28

---

<a id="character-action-blocking-cases"></a>
## 🎬 Character & Action Blocking / 角色與動作 blocking

<a id="case-6"></a>
### Case 6: [多角色 + 對話 + 精准运鏡](https://x.com/reidhannaford/status/2069420552394043625) (by [@reidhannaford](https://x.com/reidhannaford))

**多角色對話鏡头：先在 Blender 里匹配角色姿势和相机运動，再让 Seedance 生成表演结果。**

- 來源筆記：说明用 Midjourney 起始幀、Blender pose/camera，再交给 Seedance，實現两個一致角色和對話鏡头。
- 複用角度：适合做多角色表演/對話場景 use case。
- 本地媒體: [case6.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case6.mp4)

類型: Demo | 日期: 2026-06-23

---

<a id="case-8"></a>
### Case 8: [手持跟拍 + 角色绕车运動](https://x.com/reidhannaford/status/2070507963429671062) (by [@reidhannaford](https://x.com/reidhannaford))

**手持跟拍：Blender 控制角色穿越空间和相机跟随，Seedance 把这种粗粝跟拍感带到最终影片。**

- 來源筆記：说明在 Blender 中移動角色并做 handheld camera follow，Seedance 跟随运動和质感。
- 複用角度：适合做手持跟拍、角色移動穿越空间的案例。


類型: Demo | 日期: 2026-06-26

---

<a id="case-9"></a>
### Case 9: [角色 blocking + 相机 blocking 同时控制](https://x.com/SamJWasserman/status/2070742850095230991) (by [@SamJWasserman](https://x.com/SamJWasserman))

**战术動作 blocking：在生成前用 Blender 规划相机环绕、鏡头、掩体位置、枪火節奏和角色移動。**

- 來源筆記：明确實現 camera orbit、lens choice、gunfire/cover positions/pop-outs，并说 prompt below。
- 複用角度：适合做動作場景 tactical blocking case。
- 本地媒體: [case9.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case9.mp4)

類型: Demo | 日期: 2026-06-27

---

<a id="case-21"></a>
### Case 21: [伏击場景 previs + Seedance 動作调度](https://x.com/reidhannaford/status/2071595581508563168) (by [@reidhannaford](https://x.com/reidhannaford))

**伏击場景案例：先用 Blender previs 解决 staging、timing 和 camera movement，再交给 Seedance 生成鏡头。**

- 來源筆記：明确把 Midjourney 起始圖、Blender blocking/相机動画和 Seedance 組合，用于複杂伏击場景而不只是簡单运鏡。
- 複用角度：适合做複杂場景先解决 staging、timing 和 camera movement，再生成鏡头的案例。
- 本地媒體: [case21.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case21.mp4)

類型: Demo | 日期: 2026-06-29

---

<a id="agentic-blender-mcp-cases"></a>
## 🤖 Agentic Blender MCP / Agent 輔助 Blender MCP

<a id="case-10"></a>
### Case 10: [Codex + Blender MCP 生成場景/動作/参照影片](https://x.com/akiyoshisan/status/2071081230108660199) (by [@akiyoshisan](https://x.com/akiyoshisan))

**Agentic Blender MCP 案例：Codex 生成簡易市場、貓的動作、相机構圖，并導出给 Seedance 的 MP4 參考。**

- 來源筆記：列出 Blender MCP 連接 Codex、生成貓/市場/屋台、15 秒 motion、camera work、導出 MP4 reference 的完整流程。
- 複用角度：适合做 Agentic Blender MCP + Seedance use case。
- 本地媒體: [case10.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case10.mp4)

類型: Integration | 日期: 2026-06-28

---

<a id="case-11"></a>
### Case 11: [Codex 生成 Blender 建筑和 camera work 后送 Seedance](https://x.com/6_KAKUU/status/2071051063663452374) (by [@6_KAKUU](https://x.com/6_KAKUU))

**Codex 辅助新手案例：建筑和 camera work 由 Codex 在 Blender 中生成，再测試 Seedance 參考运動。**

- 來源筆記：说明 Blender 初学第 3 天，建筑到 camera work 都由 Codex 完成，Seedance 能跟随。
- 複用角度：适合做 Codex-assisted camera work case。
- 本地媒體: [case11.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case11.mp4)

類型: Integration | 日期: 2026-06-28

---

<a id="case-22"></a>
### Case 22: [Claude 用 Blender MCP 几分钟生成 previs](https://x.com/JoshDaws/status/2071401550845481090) (by [@JoshDaws](https://x.com/JoshDaws))

**快速 agentic previs 案例：Claude 通过 Blender MCP 在 2-3 分钟内搭出鏡头參考。**

- 來源筆記：说明 Claude 通过 Blender MCP 为鏡头创建 previs，并强调 2-3 分钟完成。
- 複用角度：适合做 agent 快速搭建鏡头預演的短案例。
- 本地媒體: [case22.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case22.mp4)

類型: Integration | 日期: 2026-06-29

---

<a id="reference-prompt-multi-input-mapping-cases"></a>
## 🧩 Reference, Prompt & Multi-Input Mapping / 參考、prompt 與多輸入映射

<a id="case-13"></a>
### Case 13: [日本語複現條件 + 完整 prompt](https://x.com/aidoga_lab/status/2070864815275585913) (by [@aidoga_lab](https://x.com/aidoga_lab))

**合并后的複現与排查案例：一條寫清參考影片條件，另一條记录相机/節奏控制有效但脚步動作仍会失败。**

- 來源筆記：给出 start frame、Blender reference video、Seedance 2.0、5s、以及长 prompt。
- 複用角度：适合做可複現 prompt/source case。
- 本地媒體: [case13.jpg](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case13.jpg), [case13.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case13.mp4), [case19.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case19.mp4)

類型: Tutorial | 日期: 2026-06-27

---

<a id="case-14"></a>
### Case 14: [Mixamo motion + Blender + Seedance 初学者路径](https://x.com/tanabe_fragm/status/2070685291183243459) (by [@tanabe_fragm](https://x.com/tanabe_fragm))

**新手运動来源案例：从 Mixamo 拿動作導入 Blender，作为可控运動基础后再送入 Seedance。**

- 來源筆記：测試 Blender x Seedance，并建议初学者下载 Mixamo motion 導入 Blender。
- 複用角度：适合做 beginner motion-source case。
- 本地媒體: [case14.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case14.mp4)

類型: Tutorial | 日期: 2026-06-27

---

<a id="case-23"></a>
### Case 23: [只保留位置关系的參考控制](https://x.com/kan_mi_no9/status/2071380621214224403) (by [@kan_mi_no9](https://x.com/kan_mi_no9))

**參考权重案例：只让參考影片约束位置关系，再用 prompt 补回速度感和動态感。**

- 來源筆記：说明通过调低參考影片對動作的约束、聚焦位置关系，补回 Seedance 的速度感和動态感。
- 複用角度：适合做 reference adherence 调参案例。
- 本地媒體: [case23.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case23.mp4)

類型: Tutorial | 日期: 2026-06-28

---

<a id="case-24"></a>
### Case 24: [用實体玩具替代 3D 软件做參考](https://x.com/gcduncombe/status/2070617538745229546) (by [@gcduncombe](https://x.com/gcduncombe))

**實体參考案例：当不想打开 Blender 时，用玩具快速拍攝运動和 staging 參考。**

- 來源筆記：提出不打开 3D 软件时也可以用玩具拍攝运動/構圖參考，作为 Blender+AI render 讨论的替代路径。
- 複用角度：适合做 physical previs / toy reference 的轻量替代案例。
- 本地媒體: [case24.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case24.mp4)

類型: Demo | 日期: 2026-06-26

---

<a id="case-26"></a>
### Case 26: [用參考控制修複 prompt 反複失败的場景](https://x.com/kan_mi_no9/status/2071168235022827587) (by [@kan_mi_no9](https://x.com/kan_mi_no9))

**控制兜底案例：prompt-only 反複失败时，用 reference 强制場景成立，即使会损失部分動态。**

- 來源筆記：说明虽然会损失部分 Seedance 自由运鏡和動态，但在必须得到特定画面的場景里很有用。
- 複用角度：适合做“prompt 失败时用 reference 兜底”的案例。
- 本地媒體: [case26.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case26.mp4)

類型: Demo | 日期: 2026-06-28

---

<a id="case-27"></a>
### Case 27: [角色比例与簡化背景的稳定性技巧](https://x.com/craftcapitallab/status/2070512271391068287) (by [@craftcapitallab](https://x.com/craftcapitallab))

**稳定性 checklist：角色比例不只看头身，还要匹配手脚体积；无须對齐的背景尽量簡化。**

- 來源筆記：总结了让參考更稳定的具体技巧：figure 不只调头身，还要让手脚体积贴合角色设计；不需要對齐的背景尽量簡单。
- 複用角度：适合做 Blender/參考影片的稳定性 checklist。
- 本地媒體: [case27.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case27.mp4)

類型: Tutorial | 日期: 2026-06-26

---

<a id="production-pipelines-toolchains-cases"></a>
## 🛠️ Production Pipelines & Toolchains / 生產管線與工具鏈

<a id="case-15"></a>
### Case 15: [Hermes/Krea2/ComfyUI/Blender MCP/Seedance 實驗](https://x.com/SamJWasserman/status/2069656428437225826) (by [@SamJWasserman](https://x.com/SamJWasserman))

**多工具 agent 管线：Hermes 安装并連接 Krea、ComfyUI、Blender MCP 和 Seedance，生成圖像与物理參考。**

- 來源筆記：说明 agent 安装 Krea2、連接 ComfyUI 和 Blender MCP，生成 reference image + physical ref vid 后送 Seedance。
- 複用角度：适合做 multi-agent creative pipeline 候选。
- 本地媒體: [case15.jpg](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case15.jpg), [case15.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case15.mp4)

類型: Integration | 日期: 2026-06-24

---

<a id="case-16"></a>
### Case 16: [Blender MCP viewport animation + Seedance/Magnific texture/lighting](https://x.com/techhalla/status/2070814203435274715) (by [@techhalla](https://x.com/techhalla))

**Viewport 到风格化案例：Blender MCP 提供相机和元素控制，再用 Seedance/Magnific 加纹理和光照。**

- 來源筆記：说明 adding 3D gives camera/element control，并声称 exactly how I did it。
- 複用角度：适合做 Blender MCP + style transfer 主案例。
- 本地媒體: [case16.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case16.mp4)

類型: Integration | 日期: 2026-06-27

---

<a id="case-17"></a>
### Case 17: [Blender 3D previz → Seedance anime render](https://x.com/restofart/status/2070086939756159368) (by [@restofart](https://x.com/restofart))

**3D previz 到動画渲染：用 Seedance 改变画面风格，同时保留 Blender 里的相机运動和動作。**

- 來源筆記：说明 full camera moves and motion preserved，定位 previz → AI-render pipeline。
- 複用角度：适合作为 anime/render pipeline case。
- 本地媒體: [case17.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case17.mp4)

類型: Integration | 日期: 2026-06-25

---

<a id="case-18"></a>
### Case 18: [FBX clay model + Claude keyframe + Seedance refs](https://x.com/Viggle_PINOC/status/2070183934265012392) (by [@Viggle_PINOC](https://x.com/Viggle_PINOC))

**FBX clay pass 流程：Blender 導入動作，Claude 辅助关键幀相机，渲染后的 clay pass 成为 Seedance 參考影片。**

- 來源筆記：具体 step：Blender 導入 FBX 到 clay model、设置 camera、Claude keyframe camera moves、導出 mp4 给 Seedance refs。
- 複用角度：适合做 FBX/Mixamo 動画參考流程。
- 本地媒體: [case18.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case18.mp4)

類型: Integration | 日期: 2026-06-25

---

<a id="limits-tests-troubleshooting-cases"></a>
## 🧪 Limits, Tests & Troubleshooting / 限制、測試與排查

<a id="case-20"></a>
### Case 20: [不用 start frame 的 Blender blockout reference](https://x.com/magneticskiff/status/2070711034793361559) (by [@magneticskiff](https://x.com/magneticskiff))

**无起始幀变体：当不能依赖 starter frame 时，用 Blender blockout 加详细环境參考也能工作。**

- 來源筆記：说明 Seedance + Blender blockout 可以使用 references 而非 starter frames，环境參考有足够细節时效果较好。
- 複用角度：适合做 reference-only variant 候选。
- 本地媒體: [case20.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case20.mp4)

類型: Limit | 日期: 2026-06-27

---

<a id="case-25"></a>
### Case 25: [玩具參考 + prompt 补强 + NG 對照](https://x.com/tea_story_hoshi/status/2071002538703479089) (by [@tea_story_hoshi](https://x.com/tea_story_hoshi))

**排查案例：參考影片通常需要 prompt 补强，不能只让模型机械照搬。**

- 來源筆記：同时给出成功例和 NG 例：解析參考影片并用 prompt 补强会更自然，直接忠實參考则動作和姿势容易僵硬。
- 複用角度：适合做 reference video troubleshooting 与 prompt reinforcement 案例。
- 本地媒體: [case25.jpg](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case25.jpg), [case25.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case25.mp4)

類型: Limit | 日期: 2026-06-27

---

<a id="case-28"></a>
### Case 28: [Blender + Seedance 布料物理压力测試](https://x.com/fatboypink/status/2070577334701473800) (by [@fatboypink](https://x.com/fatboypink))

**布料物理压力测試：Blender-guided Seedance 可用，但複杂运動仍需要多轮迭代。**

- 來源筆記：明确把目标设为测試 Seedance 對 cloth physics 的处理能力，并说明这是较难解决的輸出。
- 複用角度：适合做 cloth physics / complex motion stress test 案例。
- 本地媒體: [case28.mp4](https://github.com/cheercheung/Awesome-Blender-Seedance-Workflow-Usecases/raw/main/media/case28.mp4)

類型: Limit | 日期: 2026-06-26

---

<a id="acknowledge"></a>
## 🙏 致謝

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

