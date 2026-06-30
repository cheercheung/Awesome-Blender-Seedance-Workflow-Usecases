<div align="center">

<a href="#quick-start"><img src="images/zh.png" alt="Blender + Seedance usecase repository banner" width="760"></a>

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

Blender + Seedance 使用案例仓库。

**这里收集真实的 Blender、Blender MCP、viewport、previs、FBX、Mixamo、ComfyUI 和 agent 辅助工作流，用来控制 Seedance 视频生成。**

当前集合来自用户提供的 X/Twitter 精选数据。每个案例都链接到原帖和创作者主页。

下面的 Quick Start 会引导用户完成 Blender MCP setup、安装 EvoLink skills、配置 API key，并在自己的 agent 里运行。

## 📊 Overview

- **25 个精选 Blender + Seedance 案例**，来自用户提供数据集中公开创作者帖子。
- 覆盖相机控制、Blender previs、多角色 blocking、动作编排、Blender MCP、Codex/Claude 辅助 blockout、FBX/Mixamo 参考、ComfyUI/style transfer 和已知限制。
- 每个案例都包含原始来源、创作者署名、简明 takeaway、证据类型和发布日期。
- 公开列表基于 35 个候选审计结果和这次新增链接，重建为 25 个主案例。
- 这个仓库用于先展示真实工作流，再把用户引导到最终 EvoLink MCP + skill 落地页。

> [!NOTE]
> 这个集合优先保留具体证据：步骤、参考视频、agent/MCP 用法、可复现条件和明确限制，而不是空泛宣传。

<a id="quick-start"></a>
## ⚡ Quick Start 工作流

先把本地 Blender 控制链路搭好，再安装 agent 会调用的 EvoLink skills。

### 1. 安装 Blender MCP

按照官方 Blender MCP setup 页面完成配置，打开 Blender，并在生成参考视频之前确认 agent 能连接到 Blender MCP server。

- 官方 setup: [Blender MCP setup](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

### 2. 安装 EvoLink skills

在 agent workspace 里安装 Seedance 生成 skill 和 Topaz 视频放大 skill。

```bash
npm i evolink-seedance
npm i evolink-topaz-video-upscale
```

### 3. 获取 API key

在 EvoLink 账号里创建 API key，然后把它暴露给 agent runtime。

```bash
export EVOLINK_API_KEY="<your-evolink-api-key>"
```

### 4. 在自己的 agent 里运行

MCP、skills 和 API key 都准备好之后，就可以让 agent 创建 Blender blockout、导出参考视频、调用 Seedance 生成，并在需要时用 Topaz 放大最终视频。

```text
Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.
```

> [!NOTE]
> Blender 侧安装细节以 Blender MCP setup 页面为准。

## 📑 目录

| 章节 | 案例 |
|---|---|
| [🎥 Camera Control & Previs / 相机控制与预演](#camera-control-previs) | Case 1, 2, 3, 4, 5 |
| [🎬 Character & Action Blocking / 角色与动作 blocking](#character-action-blocking) | Case 6, 8, 9, 21 |
| [🤖 Agentic Blender MCP / Agent 辅助 Blender MCP](#agentic-blender-mcp) | Case 10, 11, 22 |
| [🧩 Reference, Prompt & Multi-Input Mapping / 参考、prompt 与多输入映射](#reference-prompt-multi-input-mapping) | Case 13, 14, 23, 24, 26, 27 |
| [🛠️ Production Pipelines & Toolchains / 生产管线与工具链](#production-pipelines-toolchains) | Case 15, 16, 17, 18 |
| [🧪 Limits, Tests & Troubleshooting / 限制、测试与排查](#limits-tests-troubleshooting) | Case 20, 25, 28 |
| [🙏 致谢](#acknowledge) | Credits and correction policy |

<a id="camera-control-previs"></a>
### 🎥 Camera Control & Previs / 相机控制与预演

| 案例 | 展示内容 | 类型 |
|---|---|---|
| [Blender 灰盒预演 + 起始帧 + Seedance motion reference](#case-1) | 合并后的导演流程：保留原始灰盒方法，再加入动作预演里的时序、速度、抖动和空间调度，最后交给 Seedance 生成。 | Demo |
| [Blender 运镜参考 + Midjourney 起始帧 + Seedance](#case-2) | 精确运镜的三步配方：Blender 负责相机运动，Midjourney 负责起始帧，Seedance 按参考运动生成视频。 | Demo |
| [Blender previz + Comfy + 三输入控制](#case-3) | ComfyUI 控制案例：Blender previz 搭配 upright/upside-down 参考帧，测试 Seedance 的运动遵循能力。 | Demo |
| [Viewport preview 导出后进 Seedance](#case-4) | Viewport preview 教程：blockout 场景、导出预览、把首帧转成真实图，再把两类参考交给 Seedance。 | Demo |
| [同一 reference video 生成不同世界](#case-5) | 同一参考视频生成不同世界：用同一段 Blender reference 锁定运动，再让 Seedance 改变世界和风格。 | Demo |

<a id="character-action-blocking"></a>
### 🎬 Character & Action Blocking / 角色与动作 blocking

| 案例 | 展示内容 | 类型 |
|---|---|---|
| [多角色 + 对话 + 精准运镜](#case-6) | 多角色对话镜头：先在 Blender 里匹配角色姿势和相机运动，再让 Seedance 生成表演结果。 | Demo |
| [手持跟拍 + 角色绕车运动](#case-8) | 手持跟拍：Blender 控制角色穿越空间和相机跟随，Seedance 把这种粗粝跟拍感带到最终视频。 | Demo |
| [角色 blocking + 相机 blocking 同时控制](#case-9) | 战术动作 blocking：在生成前用 Blender 规划相机环绕、镜头、掩体位置、枪火节奏和角色移动。 | Demo |
| [伏击场景 previs + Seedance 动作调度](#case-21) | 伏击场景案例：先用 Blender previs 解决 staging、timing 和 camera movement，再交给 Seedance 生成镜头。 | Demo |

<a id="agentic-blender-mcp"></a>
### 🤖 Agentic Blender MCP / Agent 辅助 Blender MCP

| 案例 | 展示内容 | 类型 |
|---|---|---|
| [Codex + Blender MCP 生成场景/动作/参照视频](#case-10) | Agentic Blender MCP 案例：Codex 生成简易市场、猫的动作、相机构图，并导出给 Seedance 的 MP4 参考。 | Integration |
| [Codex 生成 Blender 建筑和 camera work 后送 Seedance](#case-11) | Codex 辅助新手案例：建筑和 camera work 由 Codex 在 Blender 中生成，再测试 Seedance 参考运动。 | Integration |
| [Claude 用 Blender MCP 几分钟生成 previs](#case-22) | 快速 agentic previs 案例：Claude 通过 Blender MCP 在 2-3 分钟内搭出镜头参考。 | Integration |

<a id="reference-prompt-multi-input-mapping"></a>
### 🧩 Reference, Prompt & Multi-Input Mapping / 参考、prompt 与多输入映射

| 案例 | 展示内容 | 类型 |
|---|---|---|
| [日本语复现条件 + 完整 prompt](#case-13) | 合并后的复现与排查案例：一条写清参考视频条件，另一条记录相机/节奏控制有效但脚步动作仍会失败。 | Tutorial |
| [Mixamo motion + Blender + Seedance 初学者路径](#case-14) | 新手运动来源案例：从 Mixamo 拿动作导入 Blender，作为可控运动基础后再送入 Seedance。 | Tutorial |
| [只保留位置关系的参考控制](#case-23) | 参考权重案例：只让参考视频约束位置关系，再用 prompt 补回速度感和动态感。 | Tutorial |
| [用实体玩具替代 3D 软件做参考](#case-24) | 实体参考案例：当不想打开 Blender 时，用玩具快速拍摄运动和 staging 参考。 | Demo |
| [用参考控制修复 prompt 反复失败的场景](#case-26) | 控制兜底案例：prompt-only 反复失败时，用 reference 强制场景成立，即使会损失部分动态。 | Demo |
| [角色比例与简化背景的稳定性技巧](#case-27) | 稳定性 checklist：角色比例不只看头身，还要匹配手脚体积；无须对齐的背景尽量简化。 | Tutorial |

<a id="production-pipelines-toolchains"></a>
### 🛠️ Production Pipelines & Toolchains / 生产管线与工具链

| 案例 | 展示内容 | 类型 |
|---|---|---|
| [Hermes/Krea2/ComfyUI/Blender MCP/Seedance 实验](#case-15) | 多工具 agent 管线：Hermes 安装并连接 Krea、ComfyUI、Blender MCP 和 Seedance，生成图像与物理参考。 | Integration |
| [Blender MCP viewport animation + Seedance/Magnific texture/lighting](#case-16) | Viewport 到风格化案例：Blender MCP 提供相机和元素控制，再用 Seedance/Magnific 加纹理和光照。 | Integration |
| [Blender 3D previz → Seedance anime render](#case-17) | 3D previz 到动画渲染：用 Seedance 改变画面风格，同时保留 Blender 里的相机运动和动作。 | Integration |
| [FBX clay model + Claude keyframe + Seedance refs](#case-18) | FBX clay pass 流程：Blender 导入动作，Claude 辅助关键帧相机，渲染后的 clay pass 成为 Seedance 参考视频。 | Integration |

<a id="limits-tests-troubleshooting"></a>
### 🧪 Limits, Tests & Troubleshooting / 限制、测试与排查

| 案例 | 展示内容 | 类型 |
|---|---|---|
| [不用 start frame 的 Blender blockout reference](#case-20) | 无起始帧变体：当不能依赖 starter frame 时，用 Blender blockout 加详细环境参考也能工作。 | Limit |
| [玩具参考 + prompt 补强 + NG 对照](#case-25) | 排查案例：参考视频通常需要 prompt 补强，不能只让模型机械照搬。 | Limit |
| [Blender + Seedance 布料物理压力测试](#case-28) | 布料物理压力测试：Blender-guided Seedance 可用，但复杂运动仍需要多轮迭代。 | Limit |

<a id="camera-control-previs-cases"></a>
## 🎥 Camera Control & Previs / 相机控制与预演

<a id="case-1"></a>
### Case 1: [Blender 灰盒预演 + 起始帧 + Seedance motion reference](https://x.com/noman23761/status/2071534020014563328) (by [@noman23761](https://x.com/noman23761))

**合并后的导演流程：保留原始灰盒方法，再加入动作预演里的时序、速度、抖动和空间调度，最后交给 Seedance 生成。**

- 来源笔记：完整说明从 image model 起始帧、Blender 灰盒场景/相机动画，到 Seedance 参考视频生成的端到端流程。
- 复用角度：可直接改写成“用 Blender blockout 精准导演 AI 镜头”的主 use case。
- 视频预览:

https://github.com/user-attachments/assets/c56d8da8-6ebf-430b-b012-0a85e28c092b

类型: Demo | 日期: 2026-06-29

---

<a id="case-2"></a>
### Case 2: [Blender 运镜参考 + Midjourney 起始帧 + Seedance](https://x.com/reidhannaford/status/2069074506849685773) (by [@reidhannaford](https://x.com/reidhannaford))

**精确运镜的三步配方：Blender 负责相机运动，Midjourney 负责起始帧，Seedance 按参考运动生成视频。**

- 来源笔记：列出 3 步 workflow：Blender block camera、Midjourney start frame、两者送入 Seedance。
- 复用角度：适合做 precision camera control 的基础案例。
- 视频预览:

https://github.com/user-attachments/assets/4bbd421d-dc83-4cae-927d-caa0f7aa143a

类型: Demo | 日期: 2026-06-22

---

<a id="case-3"></a>
### Case 3: [Blender previz + Comfy + 三输入控制](https://x.com/JMSvid/status/2070258132840796579) (by [@JMSvid](https://x.com/JMSvid))

**ComfyUI 控制案例：Blender previz 搭配 upright/upside-down 参考帧，测试 Seedance 的运动遵循能力。**

- 来源笔记：说明用 Blender previz 作为 guide，并配 upright/upside-down reference frames。
- 复用角度：适合做多输入相机控制 case。
- 视频预览:

https://github.com/user-attachments/assets/987cf30d-de8b-4cf1-809a-5deaea8ceff0

类型: Demo | 日期: 2026-06-25

---

<a id="case-4"></a>
### Case 4: [Viewport preview 导出后进 Seedance](https://x.com/DiabloNemesis/status/2070441923706503380) (by [@DiabloNemesis](https://x.com/DiabloNemesis))

**Viewport preview 教程：blockout 场景、导出预览、把首帧转成真实图，再把两类参考交给 Seedance。**

- 来源笔记：明确流程：Blender block out scene、export viewport preview、抽第一帧转真实图、作为 reference 送 Seedance。
- 复用角度：适合做 viewport preview → Seedance 的短教程案例。
- 视频预览:

https://github.com/user-attachments/assets/5b39d216-e84a-4372-83e6-a636bcf9d2fe

类型: Demo | 日期: 2026-06-26

---

<a id="case-5"></a>
### Case 5: [同一 reference video 生成不同世界](https://x.com/koldo2k/status/2071307945002815967) (by [@koldo2k](https://x.com/koldo2k))

**同一参考视频生成不同世界：用同一段 Blender reference 锁定运动，再让 Seedance 改变世界和风格。**

- 来源笔记：说明用 Blender 控制、Seedance 想象，同一 reference video 生成不同 worlds，并提到 prompt。
- 复用角度：适合做 style/world variation case。
- 视频预览:

https://github.com/user-attachments/assets/a6304e6a-d431-4cf7-9dd2-f664594e34c5

类型: Demo | 日期: 2026-06-28

---

<a id="character-action-blocking-cases"></a>
## 🎬 Character & Action Blocking / 角色与动作 blocking

<a id="case-6"></a>
### Case 6: [多角色 + 对话 + 精准运镜](https://x.com/reidhannaford/status/2069420552394043625) (by [@reidhannaford](https://x.com/reidhannaford))

**多角色对话镜头：先在 Blender 里匹配角色姿势和相机运动，再让 Seedance 生成表演结果。**

- 来源笔记：说明用 Midjourney 起始帧、Blender pose/camera，再交给 Seedance，实现两个一致角色和对话镜头。
- 复用角度：适合做多角色表演/对话场景 use case。
- 视频预览:

https://github.com/user-attachments/assets/8f92ed66-1c9f-4fc1-885e-71240add8f56

类型: Demo | 日期: 2026-06-23

---

<a id="case-8"></a>
### Case 8: [手持跟拍 + 角色绕车运动](https://x.com/reidhannaford/status/2070507963429671062) (by [@reidhannaford](https://x.com/reidhannaford))

**手持跟拍：Blender 控制角色穿越空间和相机跟随，Seedance 把这种粗粝跟拍感带到最终视频。**

- 来源笔记：说明在 Blender 中移动角色并做 handheld camera follow，Seedance 跟随运动和质感。
- 复用角度：适合做手持跟拍、角色移动穿越空间的案例。
- 视频预览:

https://github.com/user-attachments/assets/598b62bd-246c-4699-8a5c-4735b536c380

类型: Demo | 日期: 2026-06-26

---

<a id="case-9"></a>
### Case 9: [角色 blocking + 相机 blocking 同时控制](https://x.com/SamJWasserman/status/2070742850095230991) (by [@SamJWasserman](https://x.com/SamJWasserman))

**战术动作 blocking：在生成前用 Blender 规划相机环绕、镜头、掩体位置、枪火节奏和角色移动。**

- 来源笔记：明确实现 camera orbit、lens choice、gunfire/cover positions/pop-outs，并说 prompt below。
- 复用角度：适合做动作场景 tactical blocking case。
- 视频预览:

https://github.com/user-attachments/assets/e92e6c44-3fef-4690-bce3-85de50ecf547

类型: Demo | 日期: 2026-06-27

---

<a id="case-21"></a>
### Case 21: [伏击场景 previs + Seedance 动作调度](https://x.com/reidhannaford/status/2071595581508563168) (by [@reidhannaford](https://x.com/reidhannaford))

**伏击场景案例：先用 Blender previs 解决 staging、timing 和 camera movement，再交给 Seedance 生成镜头。**

- 来源笔记：明确把 Midjourney 起始图、Blender blocking/相机动画和 Seedance 组合，用于复杂伏击场景而不只是简单运镜。
- 复用角度：适合做复杂场景先解决 staging、timing 和 camera movement，再生成镜头的案例。
- 视频预览:

https://github.com/user-attachments/assets/a254edb3-245d-4bc0-87cc-45bd17e82b99

类型: Demo | 日期: 2026-06-29

---

<a id="agentic-blender-mcp-cases"></a>
## 🤖 Agentic Blender MCP / Agent 辅助 Blender MCP

<a id="case-10"></a>
### Case 10: [Codex + Blender MCP 生成场景/动作/参照视频](https://x.com/akiyoshisan/status/2071081230108660199) (by [@akiyoshisan](https://x.com/akiyoshisan))

**Agentic Blender MCP 案例：Codex 生成简易市场、猫的动作、相机构图，并导出给 Seedance 的 MP4 参考。**

- 来源笔记：列出 Blender MCP 连接 Codex、生成猫/市场/屋台、15 秒 motion、camera work、导出 MP4 reference 的完整流程。
- 复用角度：适合做 Agentic Blender MCP + Seedance use case。
- 视频预览:

https://github.com/user-attachments/assets/cff81cc4-0f72-49d8-881f-aee6ded2d5cf

类型: Integration | 日期: 2026-06-28

---

<a id="case-11"></a>
### Case 11: [Codex 生成 Blender 建筑和 camera work 后送 Seedance](https://x.com/6_KAKUU/status/2071051063663452374) (by [@6_KAKUU](https://x.com/6_KAKUU))

**Codex 辅助新手案例：建筑和 camera work 由 Codex 在 Blender 中生成，再测试 Seedance 参考运动。**

- 来源笔记：说明 Blender 初学第 3 天，建筑到 camera work 都由 Codex 完成，Seedance 能跟随。
- 复用角度：适合做 Codex-assisted camera work case。
- 视频预览:

https://github.com/user-attachments/assets/247ccf17-4652-4c11-b8dc-efdba1567707

类型: Integration | 日期: 2026-06-28

---

<a id="case-22"></a>
### Case 22: [Claude 用 Blender MCP 几分钟生成 previs](https://x.com/JoshDaws/status/2071401550845481090) (by [@JoshDaws](https://x.com/JoshDaws))

**快速 agentic previs 案例：Claude 通过 Blender MCP 在 2-3 分钟内搭出镜头参考。**

- 来源笔记：说明 Claude 通过 Blender MCP 为镜头创建 previs，并强调 2-3 分钟完成。
- 复用角度：适合做 agent 快速搭建镜头预演的短案例。
- 视频预览:

https://github.com/user-attachments/assets/e9c22c6f-690f-4b3b-984c-a18506580c38

类型: Integration | 日期: 2026-06-29

---

<a id="reference-prompt-multi-input-mapping-cases"></a>
## 🧩 Reference, Prompt & Multi-Input Mapping / 参考、prompt 与多输入映射

<a id="case-13"></a>
### Case 13: [日本语复现条件 + 完整 prompt](https://x.com/aidoga_lab/status/2070864815275585913) (by [@aidoga_lab](https://x.com/aidoga_lab))

**合并后的复现与排查案例：一条写清参考视频条件，另一条记录相机/节奏控制有效但脚步动作仍会失败。**

- 来源笔记：给出 start frame、Blender reference video、Seedance 2.0、5s、以及长 prompt。
- 复用角度：适合做可复现 prompt/source case。
- 视频预览:

https://github.com/user-attachments/assets/2dabc892-946a-4879-9af0-0e21386b16a5

https://github.com/user-attachments/assets/222be6cc-82c7-4953-9abe-70618f6d499b

类型: Tutorial | 日期: 2026-06-27

---

<a id="case-14"></a>
### Case 14: [Mixamo motion + Blender + Seedance 初学者路径](https://x.com/tanabe_fragm/status/2070685291183243459) (by [@tanabe_fragm](https://x.com/tanabe_fragm))

**新手运动来源案例：从 Mixamo 拿动作导入 Blender，作为可控运动基础后再送入 Seedance。**

- 来源笔记：测试 Blender x Seedance，并建议初学者下载 Mixamo motion 导入 Blender。
- 复用角度：适合做 beginner motion-source case。
- 视频预览:

https://github.com/user-attachments/assets/3f04e458-a43f-4860-af2b-88eb6dd397cc

类型: Tutorial | 日期: 2026-06-27

---

<a id="case-23"></a>
### Case 23: [只保留位置关系的参考控制](https://x.com/kan_mi_no9/status/2071380621214224403) (by [@kan_mi_no9](https://x.com/kan_mi_no9))

**参考权重案例：只让参考视频约束位置关系，再用 prompt 补回速度感和动态感。**

- 来源笔记：说明通过调低参考视频对动作的约束、聚焦位置关系，补回 Seedance 的速度感和动态感。
- 复用角度：适合做 reference adherence 调参案例。
- 视频预览:

https://github.com/user-attachments/assets/91721f79-eeaf-4309-bc4a-11e8136c6dba

类型: Tutorial | 日期: 2026-06-28

---

<a id="case-24"></a>
### Case 24: [用实体玩具替代 3D 软件做参考](https://x.com/gcduncombe/status/2070617538745229546) (by [@gcduncombe](https://x.com/gcduncombe))

**实体参考案例：当不想打开 Blender 时，用玩具快速拍摄运动和 staging 参考。**

- 来源笔记：提出不打开 3D 软件时也可以用玩具拍摄运动/构图参考，作为 Blender+AI render 讨论的替代路径。
- 复用角度：适合做 physical previs / toy reference 的轻量替代案例。
- 视频预览:

https://github.com/user-attachments/assets/b6a3f37b-ef8c-46c1-ad53-a822797a7c09

类型: Demo | 日期: 2026-06-26

---

<a id="case-26"></a>
### Case 26: [用参考控制修复 prompt 反复失败的场景](https://x.com/kan_mi_no9/status/2071168235022827587) (by [@kan_mi_no9](https://x.com/kan_mi_no9))

**控制兜底案例：prompt-only 反复失败时，用 reference 强制场景成立，即使会损失部分动态。**

- 来源笔记：说明虽然会损失部分 Seedance 自由运镜和动态，但在必须得到特定画面的场景里很有用。
- 复用角度：适合做“prompt 失败时用 reference 兜底”的案例。
- 视频预览:

https://github.com/user-attachments/assets/e63c102e-11cf-4381-87fe-8cfe0d96702b

类型: Demo | 日期: 2026-06-28

---

<a id="case-27"></a>
### Case 27: [角色比例与简化背景的稳定性技巧](https://x.com/craftcapitallab/status/2070512271391068287) (by [@craftcapitallab](https://x.com/craftcapitallab))

**稳定性 checklist：角色比例不只看头身，还要匹配手脚体积；无须对齐的背景尽量简化。**

- 来源笔记：总结了让参考更稳定的具体技巧：figure 不只调头身，还要让手脚体积贴合角色设计；不需要对齐的背景尽量简单。
- 复用角度：适合做 Blender/参考视频的稳定性 checklist。
- 视频预览:

https://github.com/user-attachments/assets/71221c71-a7eb-428f-90e5-4a6111aaf890

类型: Tutorial | 日期: 2026-06-26

---

<a id="production-pipelines-toolchains-cases"></a>
## 🛠️ Production Pipelines & Toolchains / 生产管线与工具链

<a id="case-15"></a>
### Case 15: [Hermes/Krea2/ComfyUI/Blender MCP/Seedance 实验](https://x.com/SamJWasserman/status/2069656428437225826) (by [@SamJWasserman](https://x.com/SamJWasserman))

**多工具 agent 管线：Hermes 安装并连接 Krea、ComfyUI、Blender MCP 和 Seedance，生成图像与物理参考。**

- 来源笔记：说明 agent 安装 Krea2、连接 ComfyUI 和 Blender MCP，生成 reference image + physical ref vid 后送 Seedance。
- 复用角度：适合做 multi-agent creative pipeline 候选。
- 视频预览:

https://github.com/user-attachments/assets/e1df0f87-e93e-4339-b25a-a7ac4c4f8c4e

类型: Integration | 日期: 2026-06-24

---

<a id="case-16"></a>
### Case 16: [Blender MCP viewport animation + Seedance/Magnific texture/lighting](https://x.com/techhalla/status/2070814203435274715) (by [@techhalla](https://x.com/techhalla))

**Viewport 到风格化案例：Blender MCP 提供相机和元素控制，再用 Seedance/Magnific 加纹理和光照。**

- 来源笔记：说明 adding 3D gives camera/element control，并声称 exactly how I did it。
- 复用角度：适合做 Blender MCP + style transfer 主案例。
- 视频预览:

https://github.com/user-attachments/assets/80143b32-352b-4e86-8c1f-85826d940ba7

类型: Integration | 日期: 2026-06-27

---

<a id="case-17"></a>
### Case 17: [Blender 3D previz → Seedance anime render](https://x.com/restofart/status/2070086939756159368) (by [@restofart](https://x.com/restofart))

**3D previz 到动画渲染：用 Seedance 改变画面风格，同时保留 Blender 里的相机运动和动作。**

- 来源笔记：说明 full camera moves and motion preserved，定位 previz → AI-render pipeline。
- 复用角度：适合作为 anime/render pipeline case。
- 视频预览:

https://github.com/user-attachments/assets/13ba8e79-0b0a-44b9-be29-9c850bdeb95a

类型: Integration | 日期: 2026-06-25

---

<a id="case-18"></a>
### Case 18: [FBX clay model + Claude keyframe + Seedance refs](https://x.com/Viggle_PINOC/status/2070183934265012392) (by [@Viggle_PINOC](https://x.com/Viggle_PINOC))

**FBX clay pass 流程：Blender 导入动作，Claude 辅助关键帧相机，渲染后的 clay pass 成为 Seedance 参考视频。**

- 来源笔记：具体 step：Blender 导入 FBX 到 clay model、设置 camera、Claude keyframe camera moves、导出 mp4 给 Seedance refs。
- 复用角度：适合做 FBX/Mixamo 动画参考流程。
- 视频预览:

https://github.com/user-attachments/assets/bccdbf9a-b816-403f-ae1f-6e43b1e295a3

类型: Integration | 日期: 2026-06-25

---

<a id="limits-tests-troubleshooting-cases"></a>
## 🧪 Limits, Tests & Troubleshooting / 限制、测试与排查

<a id="case-20"></a>
### Case 20: [不用 start frame 的 Blender blockout reference](https://x.com/magneticskiff/status/2070711034793361559) (by [@magneticskiff](https://x.com/magneticskiff))

**无起始帧变体：当不能依赖 starter frame 时，用 Blender blockout 加详细环境参考也能工作。**

- 来源笔记：说明 Seedance + Blender blockout 可以使用 references 而非 starter frames，环境参考有足够细节时效果较好。
- 复用角度：适合做 reference-only variant 候选。
- 视频预览:

https://github.com/user-attachments/assets/dfa129d8-f06b-4018-a5bb-c1ed9e78d0d3

类型: Limit | 日期: 2026-06-27

---

<a id="case-25"></a>
### Case 25: [玩具参考 + prompt 补强 + NG 对照](https://x.com/tea_story_hoshi/status/2071002538703479089) (by [@tea_story_hoshi](https://x.com/tea_story_hoshi))

**排查案例：参考视频通常需要 prompt 补强，不能只让模型机械照搬。**

- 来源笔记：同时给出成功例和 NG 例：解析参考视频并用 prompt 补强会更自然，直接忠实参考则动作和姿势容易僵硬。
- 复用角度：适合做 reference video troubleshooting 与 prompt reinforcement 案例。
- 视频预览:

https://github.com/user-attachments/assets/d333d2d0-8317-49f0-8815-86db783cb578

类型: Limit | 日期: 2026-06-27

---

<a id="case-28"></a>
### Case 28: [Blender + Seedance 布料物理压力测试](https://x.com/fatboypink/status/2070577334701473800) (by [@fatboypink](https://x.com/fatboypink))

**布料物理压力测试：Blender-guided Seedance 可用，但复杂运动仍需要多轮迭代。**

- 来源笔记：明确把目标设为测试 Seedance 对 cloth physics 的处理能力，并说明这是较难解决的输出。
- 复用角度：适合做 cloth physics / complex motion stress test 案例。
- 视频预览:

https://github.com/user-attachments/assets/3ab561b2-ef3e-47a5-b2c4-8378a521e491

类型: Limit | 日期: 2026-06-26

---

<a id="acknowledge"></a>
## 🙏 致谢

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

