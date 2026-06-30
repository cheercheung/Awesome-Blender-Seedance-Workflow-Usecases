#!/usr/bin/env python3
"""Generate the Blender + Seedance usecase repository surface from curated data."""

from __future__ import annotations

import json
import re
import textwrap
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "primary-use-case-posts.json"
REPO = "Awesome-Blender-Seedance-Workflow-Usecases"
OWNER = "cheercheung"
MODEL = "Blender + Seedance"
MODEL_ID = "seedance-2.0-reference-to-video"
CTA_ANCHOR = "#quick-start"
RAW_MEDIA_BASE = f"https://github.com/{OWNER}/{REPO}/raw/main/"
BANNER_SOURCE = ROOT / "images" / "banner.png"

LANGS = [
    ("en", "README.md", "English", "images/banner.png"),
    ("es", "README_es.md", "Español", "images/banner.png"),
    ("pt", "README_pt.md", "Português", "images/banner.png"),
    ("ja", "README_ja.md", "日本語", "images/banner.png"),
    ("ko", "README_ko.md", "한국어", "images/banner.png"),
    ("de", "README_de.md", "Deutsch", "images/banner.png"),
    ("fr", "README_fr.md", "Français", "images/banner.png"),
    ("tr", "README_tr.md", "Türkçe", "images/banner.png"),
    ("zh-TW", "README_zh-TW.md", "繁體中文", "images/banner.png"),
    ("zh-CN", "README_zh-CN.md", "简体中文", "images/banner.png"),
    ("ru", "README_ru.md", "Русский", "images/banner.png"),
]

LANG_BADGES = """[![English](https://img.shields.io/badge/English-111111)](README.md)
[![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md)
[![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md)
[![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md)
[![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md)
[![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md)
[![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md)
[![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md)
[![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md)
[![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)"""

CATEGORY_META = {
    "camera-control": ("🎥", "Camera Control & Previs"),
    "character-action": ("🎬", "Character & Action Blocking"),
    "agentic-mcp": ("🤖", "Agentic Blender MCP"),
    "reference-prompt": ("🧩", "Reference, Prompt & Multi-Input Mapping"),
    "production-pipeline": ("🛠️", "Production Pipelines & Toolchains"),
    "limitations": ("🧪", "Limits, Tests & Troubleshooting"),
}

CATEGORY_DISPLAY = {
    "en": {
        "camera-control": "Camera Control & Previs",
        "character-action": "Character & Action Blocking",
        "agentic-mcp": "Agentic Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping",
        "production-pipeline": "Production Pipelines & Toolchains",
        "limitations": "Limits, Tests & Troubleshooting",
    },
    "es": {
        "camera-control": "Camera Control & Previs / Control de cámara y previs",
        "character-action": "Character & Action Blocking / Bloqueo de personajes y acción",
        "agentic-mcp": "Agentic Blender MCP / Blender MCP con agentes",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / Referencias, prompts y entradas múltiples",
        "production-pipeline": "Production Pipelines & Toolchains / Pipelines y herramientas de producción",
        "limitations": "Limits, Tests & Troubleshooting / Límites, pruebas y diagnóstico",
    },
    "pt": {
        "camera-control": "Camera Control & Previs / Controle de câmera e previs",
        "character-action": "Character & Action Blocking / Bloqueio de personagens e ação",
        "agentic-mcp": "Agentic Blender MCP / Blender MCP com agentes",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / Referências, prompts e múltiplas entradas",
        "production-pipeline": "Production Pipelines & Toolchains / Pipelines e ferramentas de produção",
        "limitations": "Limits, Tests & Troubleshooting / Limites, testes e diagnóstico",
    },
    "ja": {
        "camera-control": "Camera Control & Previs / カメラ制御とプリビズ",
        "character-action": "Character & Action Blocking / キャラクターとアクションのブロッキング",
        "agentic-mcp": "Agentic Blender MCP / エージェント型 Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / 参照、プロンプト、複数入力の対応付け",
        "production-pipeline": "Production Pipelines & Toolchains / 制作パイプラインとツールチェーン",
        "limitations": "Limits, Tests & Troubleshooting / 制限、検証、トラブルシュート",
    },
    "ko": {
        "camera-control": "Camera Control & Previs / 카메라 제어와 프리비즈",
        "character-action": "Character & Action Blocking / 캐릭터와 액션 블로킹",
        "agentic-mcp": "Agentic Blender MCP / 에이전트 기반 Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / 레퍼런스, 프롬프트, 다중 입력 매핑",
        "production-pipeline": "Production Pipelines & Toolchains / 제작 파이프라인과 툴체인",
        "limitations": "Limits, Tests & Troubleshooting / 한계, 테스트, 문제 해결",
    },
    "de": {
        "camera-control": "Camera Control & Previs / Kamerasteuerung und Previs",
        "character-action": "Character & Action Blocking / Figuren- und Action-Blocking",
        "agentic-mcp": "Agentic Blender MCP / Agentisches Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / Referenzen, Prompts und Multi-Input-Mapping",
        "production-pipeline": "Production Pipelines & Toolchains / Produktionspipelines und Toolchains",
        "limitations": "Limits, Tests & Troubleshooting / Grenzen, Tests und Fehlersuche",
    },
    "fr": {
        "camera-control": "Camera Control & Previs / Contrôle caméra et prévisualisation",
        "character-action": "Character & Action Blocking / Blocking personnages et action",
        "agentic-mcp": "Agentic Blender MCP / Blender MCP avec agents",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / Références, prompts et entrées multiples",
        "production-pipeline": "Production Pipelines & Toolchains / Pipelines et outils de production",
        "limitations": "Limits, Tests & Troubleshooting / Limites, tests et dépannage",
    },
    "tr": {
        "camera-control": "Camera Control & Previs / Kamera kontrolü ve previs",
        "character-action": "Character & Action Blocking / Karakter ve aksiyon blocking",
        "agentic-mcp": "Agentic Blender MCP / Agent destekli Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / Referans, prompt ve çoklu girdi eşleme",
        "production-pipeline": "Production Pipelines & Toolchains / Üretim pipeline'ları ve araç zinciri",
        "limitations": "Limits, Tests & Troubleshooting / Sınırlar, testler ve sorun giderme",
    },
    "zh-CN": {
        "camera-control": "Camera Control & Previs / 相机控制与预演",
        "character-action": "Character & Action Blocking / 角色与动作 blocking",
        "agentic-mcp": "Agentic Blender MCP / Agent 辅助 Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / 参考、prompt 与多输入映射",
        "production-pipeline": "Production Pipelines & Toolchains / 生产管线与工具链",
        "limitations": "Limits, Tests & Troubleshooting / 限制、测试与排查",
    },
    "zh-TW": {
        "camera-control": "Camera Control & Previs / 相機控制與預演",
        "character-action": "Character & Action Blocking / 角色與動作 blocking",
        "agentic-mcp": "Agentic Blender MCP / Agent 輔助 Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / 參考、prompt 與多輸入映射",
        "production-pipeline": "Production Pipelines & Toolchains / 生產管線與工具鏈",
        "limitations": "Limits, Tests & Troubleshooting / 限制、測試與排查",
    },
    "ru": {
        "camera-control": "Camera Control & Previs / Управление камерой и превиз",
        "character-action": "Character & Action Blocking / Блокинг персонажей и экшена",
        "agentic-mcp": "Agentic Blender MCP / Агентный Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / Референсы, промпты и multi-input mapping",
        "production-pipeline": "Production Pipelines & Toolchains / Производственные пайплайны и инструменты",
        "limitations": "Limits, Tests & Troubleshooting / Ограничения, тесты и разбор ошибок",
    },
}

OVERVIEW_LINES = {
    "en": [
        "**{count} selected Blender + Seedance cases** from public creator posts in the owner-provided source dataset.",
        "Covers camera control, Blender previs, multi-character blocking, action choreography, Blender MCP, Codex/Claude-assisted blockouts, FBX/Mixamo references, ComfyUI/style transfer, and known limitations.",
        "Each case includes the original source, creator attribution, a concise takeaway, evidence type, and publication date.",
        "The public list was rebuilt from the 35-candidate audit plus the requested new links into {count} primary cases.",
        "Use this repo to inspect practical workflows before routing users to the final EvoLink MCP + skill landing page.",
    ],
    "es": [
        "**{count} casos Blender + Seedance seleccionados** a partir de publicaciones públicas de creadores en el dataset proporcionado por el propietario.",
        "Cubre control de cámara, previs en Blender, blocking de varios personajes, coreografía de acción, Blender MCP, blockouts asistidos por Codex/Claude, referencias FBX/Mixamo, ComfyUI/style transfer y límites conocidos.",
        "Cada caso incluye fuente original, atribución al creador, aprendizaje breve, tipo de evidencia y fecha de publicación.",
        "La lista pública se reconstruyó desde la auditoría de 35 candidatos y los nuevos enlaces solicitados hasta {count} casos primarios.",
        "Usa este repo para revisar workflows prácticos antes de enviar usuarios a la landing final de EvoLink MCP + skill.",
    ],
    "pt": [
        "**{count} casos Blender + Seedance selecionados** a partir de posts públicos de criadores no dataset fornecido pelo proprietário.",
        "Cobre controle de câmera, previs no Blender, blocking de múltiplos personagens, coreografia de ação, Blender MCP, blockouts assistidos por Codex/Claude, referências FBX/Mixamo, ComfyUI/style transfer e limites conhecidos.",
        "Cada caso inclui fonte original, crédito ao criador, resumo acionável, tipo de evidência e data de publicação.",
        "A lista pública foi reconstruída a partir da auditoria de 35 candidatos e dos novos links solicitados até {count} casos primários.",
        "Use este repo para avaliar workflows práticos antes de direcionar usuários à landing final de EvoLink MCP + skill.",
    ],
    "ja": [
        "**{count} 件の Blender + Seedance ケース** を、所有者提供の公開クリエイター投稿データから選定しました。",
        "カメラ制御、Blender previs、複数キャラクターのブロッキング、アクション設計、Blender MCP、Codex/Claude 支援 blockout、FBX/Mixamo 参照、ComfyUI/style transfer、既知の制限を扱います。",
        "各ケースには元ソース、作者クレジット、短い要点、証拠タイプ、公開日を含めています。",
        "公開リストは、35 件の監査結果と追加依頼されたリンクから {count} 件の主要ケースとして再構成しました。",
        "最終的な EvoLink MCP + skill landing に誘導する前に、実用 workflow を確認するための repo です。",
    ],
    "ko": [
        "소유자가 제공한 공개 제작자 게시물 데이터에서 **{count}개의 Blender + Seedance 사례**를 선별했습니다.",
        "카메라 제어, Blender 프리비즈, 다중 캐릭터 블로킹, 액션 안무, Blender MCP, Codex/Claude 지원 blockout, FBX/Mixamo 레퍼런스, ComfyUI/style transfer, 알려진 한계를 다룹니다.",
        "각 사례에는 원본 출처, 제작자 표기, 간단한 takeaway, 증거 유형, 게시일이 포함됩니다.",
        "공개 목록은 35개 후보 감사와 요청된 신규 링크를 반영해 {count}개 주요 사례로 재구성했습니다.",
        "최종 EvoLink MCP + skill 랜딩으로 보내기 전에 실제 workflow를 검토하기 위한 repo입니다.",
    ],
    "de": [
        "**{count} ausgewählte Blender + Seedance Fälle** aus öffentlichen Creator-Posts im vom Owner bereitgestellten Datensatz.",
        "Behandelt Kamerasteuerung, Blender-Previs, Multi-Character-Blocking, Action-Choreografie, Blender MCP, Codex/Claude-gestützte Blockouts, FBX/Mixamo-Referenzen, ComfyUI/style transfer und bekannte Grenzen.",
        "Jeder Fall enthält Originalquelle, Creator-Zuordnung, kompaktes Takeaway, Evidenztyp und Veröffentlichungsdatum.",
        "Die öffentliche Liste wurde aus dem 35-Kandidaten-Audit und den angefragten neuen Links zu {count} Primärfällen neu aufgebaut.",
        "Nutze dieses Repo, um praktische Workflows zu prüfen, bevor Nutzer zur finalen EvoLink MCP + Skill Landingpage geführt werden.",
    ],
    "fr": [
        "**{count} cas Blender + Seedance sélectionnés** depuis des publications publiques de créateurs dans le dataset fourni par le propriétaire.",
        "Couvre contrôle caméra, previs Blender, blocking multi-personnages, chorégraphie d'action, Blender MCP, blockouts assistés par Codex/Claude, références FBX/Mixamo, ComfyUI/style transfer et limites connues.",
        "Chaque cas inclut la source originale, l'attribution créateur, un résumé exploitable, le type de preuve et la date de publication.",
        "La liste publique a été reconstruite depuis l'audit des 35 candidats et les nouveaux liens demandés en {count} cas principaux.",
        "Utilisez ce repo pour examiner des workflows pratiques avant de diriger les utilisateurs vers la landing EvoLink MCP + skill finale.",
    ],
    "tr": [
        "Sahibin sağladığı herkese açık creator postlarından **{count} Blender + Seedance vakası** seçildi.",
        "Kamera kontrolü, Blender previs, çok karakterli blocking, aksiyon koreografisi, Blender MCP, Codex/Claude destekli blockout'lar, FBX/Mixamo referansları, ComfyUI/style transfer ve bilinen sınırları kapsar.",
        "Her vaka orijinal kaynak, creator atfı, kısa takeaway, kanıt tipi ve yayın tarihini içerir.",
        "Herkese açık liste, 35 adaylık denetim ve istenen yeni linklerle {count} ana vaka olarak yeniden kuruldu.",
        "Bu repo, kullanıcıları final EvoLink MCP + skill landing sayfasına yönlendirmeden önce pratik workflow'ları incelemek içindir.",
    ],
    "zh-CN": [
        "**{count} 个精选 Blender + Seedance 案例**，来自用户提供数据集中公开创作者帖子。",
        "覆盖相机控制、Blender previs、多角色 blocking、动作编排、Blender MCP、Codex/Claude 辅助 blockout、FBX/Mixamo 参考、ComfyUI/style transfer 和已知限制。",
        "每个案例都包含原始来源、创作者署名、简明 takeaway、证据类型和发布日期。",
        "公开列表基于 35 个候选审计结果和这次新增链接，重建为 {count} 个主案例。",
        "这个仓库用于先展示真实工作流，再把用户引导到最终 EvoLink MCP + skill 落地页。",
    ],
    "zh-TW": [
        "**{count} 個精選 Blender + Seedance 案例**，來自使用者提供資料集中公開創作者貼文。",
        "涵蓋相機控制、Blender previs、多角色 blocking、動作編排、Blender MCP、Codex/Claude 輔助 blockout、FBX/Mixamo 參考、ComfyUI/style transfer 和已知限制。",
        "每個案例都包含原始來源、創作者署名、簡明 takeaway、證據類型和發布日期。",
        "公開列表基於 35 個候選審計結果和這次新增連結，重建為 {count} 個主案例。",
        "這個倉庫用於先展示真實工作流，再把使用者引導到最終 EvoLink MCP + skill 落地頁。",
    ],
    "ru": [
        "**{count} отобранных кейсов Blender + Seedance** из публичных постов авторов в датасете владельца.",
        "Охватывает управление камерой, Blender previs, блокинг нескольких персонажей, постановку экшена, Blender MCP, blockout с Codex/Claude, FBX/Mixamo references, ComfyUI/style transfer и известные ограничения.",
        "Каждый кейс содержит исходный пост, автора, краткий вывод, тип доказательства и дату публикации.",
        "Публичный список пересобран из аудита 35 кандидатов и новых ссылок в {count} основных кейсов.",
        "Этот repo помогает изучить реальные workflows перед переходом к финальной landing page EvoLink MCP + skill.",
    ],
}

SELECTED_SOURCE_INDICES = [
    1,
    2,
    3,
    6,
    7,
    9,
    14,
    19,
    20,
    21,
    23,
    24,
    25,
    28,
    29,
    31,
    32,
]

CASE_LABEL_FOR_SOURCE_INDEX = {
    1: 1,
    2: 2,
    14: 3,
    28: 4,
    32: 5,
    3: 6,
    6: 8,
    19: 9,
    9: 10,
    24: 11,
    7: 13,
    23: 14,
    20: 15,
    21: 16,
    25: 17,
    29: 18,
    31: 20,
}

MEDIA_BY_SOURCE_INDEX = {
    1: ["media/case1.mp4"],
    2: ["media/case2.mp4"],
    14: ["media/case3.mp4"],
    28: ["media/case4.mp4"],
    32: ["media/case5.mp4"],
    3: ["media/case6.mp4"],
    19: ["media/case9.mp4"],
    9: ["media/case10.mp4"],
    24: ["media/case11.mp4"],
    7: ["media/case13.jpg", "media/case13.mp4", "media/case19.mp4"],
    23: ["media/case14.mp4"],
    20: ["media/case15.jpg", "media/case15.mp4"],
    21: ["media/case16.mp4"],
    25: ["media/case17.mp4"],
    29: ["media/case18.mp4"],
    31: ["media/case20.mp4"],
}

VIDEO_SOURCE_ROWS = [
    ("case1", "https://github.com/user-attachments/assets/c56d8da8-6ebf-430b-b012-0a85e28c092b"),
    ("case2", "https://github.com/user-attachments/assets/4bbd421d-dc83-4cae-927d-caa0f7aa143a"),
    ("case3", "https://github.com/user-attachments/assets/987cf30d-de8b-4cf1-809a-5deaea8ceff0"),
    ("case4", "https://github.com/user-attachments/assets/5b39d216-e84a-4372-83e6-a636bcf9d2fe"),
    ("case5", "https://github.com/user-attachments/assets/a6304e6a-d431-4cf7-9dd2-f664594e34c5"),
    ("case6", "https://github.com/user-attachments/assets/8f92ed66-1c9f-4fc1-885e-71240add8f56"),
    ("case8", "https://github.com/user-attachments/assets/598b62bd-246c-4699-8a5c-4735b536c380"),
    ("case9", "https://github.com/user-attachments/assets/e92e6c44-3fef-4690-bce3-85de50ecf547"),
    ("case10", "https://github.com/user-attachments/assets/cff81cc4-0f72-49d8-881f-aee6ded2d5cf"),
    ("case11", "https://github.com/user-attachments/assets/247ccf17-4652-4c11-b8dc-efdba1567707"),
    ("case13", "https://github.com/user-attachments/assets/2dabc892-946a-4879-9af0-0e21386b16a5"),
    ("case14", "https://github.com/user-attachments/assets/3f04e458-a43f-4860-af2b-88eb6dd397cc"),
    ("case15", "https://github.com/user-attachments/assets/e1df0f87-e93e-4339-b25a-a7ac4c4f8c4e"),
    ("case16", "https://github.com/user-attachments/assets/80143b32-352b-4e86-8c1f-85826d940ba7"),
    ("case17", "https://github.com/user-attachments/assets/13ba8e79-0b0a-44b9-be29-9c850bdeb95a"),
    ("case18", "https://github.com/user-attachments/assets/bccdbf9a-b816-403f-ae1f-6e43b1e295a3"),
    ("case19", "https://github.com/user-attachments/assets/222be6cc-82c7-4953-9abe-70618f6d499b"),
    ("case20", "https://github.com/user-attachments/assets/dfa129d8-f06b-4018-a5bb-c1ed9e78d0d3"),
    ("case21", "https://github.com/user-attachments/assets/a254edb3-245d-4bc0-87cc-45bd17e82b99"),
    ("case22", "https://github.com/user-attachments/assets/e9c22c6f-690f-4b3b-984c-a18506580c38"),
    ("case23", "https://github.com/user-attachments/assets/91721f79-eeaf-4309-bc4a-11e8136c6dba"),
    ("case24", "https://github.com/user-attachments/assets/b6a3f37b-ef8c-46c1-ad53-a822797a7c09"),
    ("case25", "https://github.com/user-attachments/assets/d333d2d0-8317-49f0-8815-86db783cb578"),
    ("case26", "https://github.com/user-attachments/assets/e63c102e-11cf-4381-87fe-8cfe0d96702b"),
    ("case27", "https://github.com/user-attachments/assets/71221c71-a7eb-428f-90e5-4a6111aaf890"),
    ("case28", "https://github.com/user-attachments/assets/3ab561b2-ef3e-47a5-b2c4-8378a521e491"),
]
VIDEO_ATTACHMENT_BY_CASE_LABEL = dict(VIDEO_SOURCE_ROWS)
VIDEO_ATTACHMENT_BY_LOCAL_MEDIA = {f"media/{label}.mp4": url for label, url in VIDEO_SOURCE_ROWS}

CATEGORY_FOR_CASE = {
    1: "camera-control",
    2: "camera-control",
    3: "character-action",
    4: "character-action",
    5: "character-action",
    6: "character-action",
    7: "reference-prompt",
    8: "limitations",
    9: "agentic-mcp",
    10: "reference-prompt",
    11: "reference-prompt",
    12: "agentic-mcp",
    13: "agentic-mcp",
    14: "camera-control",
    15: "camera-control",
    16: "camera-control",
    17: "reference-prompt",
    18: "reference-prompt",
    19: "character-action",
    20: "production-pipeline",
    21: "production-pipeline",
    22: "production-pipeline",
    23: "reference-prompt",
    24: "agentic-mcp",
    25: "production-pipeline",
    26: "camera-control",
    27: "agentic-mcp",
    28: "camera-control",
    29: "production-pipeline",
    30: "production-pipeline",
    31: "limitations",
    32: "camera-control",
    33: "limitations",
    34: "agentic-mcp",
    35: "reference-prompt",
}

EN_TITLES = {
    1: "Blender Blockout as Seedance Motion Reference",
    2: "Camera Blocking with Midjourney Start Frame",
    3: "Multi-Character Dialogue with Matched Poses",
    4: "Basic Shapes for Multi-Character Shots",
    5: "Action Choreography from Rough Blender Timing",
    6: "Handheld Follow Camera through Space",
    7: "Reproducible Seedance Prompt with Blender Reference",
    8: "Camera Rhythm Control and Foot-Sliding Limits",
    9: "Codex + Blender MCP Reference Video Workflow",
    10: "Character Mapping from Blocking and Reference Images",
    11: "FBX Animation Export as Seedance Reference",
    12: "No-Click Blender Animation with Agent Assistance",
    13: "One-Prompt Blender MCP Blockout",
    14: "ComfyUI Camera Control with Blender Previs",
    15: "Blender Viewport as Scene Direction",
    16: "Viewport Preview for Character Animation",
    17: "Director Checklist for Camera and Lens Control",
    18: "Action Shot Direction with Blender Camera Planning",
    19: "Camera and Character Blocking for Tactical Action",
    20: "Hermes, Krea, ComfyUI and Blender MCP Stack",
    21: "Blender MCP Viewport to Seedance Style Transfer",
    22: "Seedance Pro Viewport Style Transfer",
    23: "Mixamo Motion as Beginner Blender Reference",
    24: "Codex-Built Architecture and Camera Work",
    25: "Blender Previz to Anime Seedance Render",
    26: "Navigable AI Filmmaking with Claude and Blender",
    27: "Beginner Agent-Assisted HIPHOP Reference Test",
    28: "Viewport Preview to Realistic Start Frame",
    29: "FBX Clay Pass with Claude-Keyframed Camera",
    30: "Two-Night Hybrid Short Film Pipeline",
    31: "Reference-Only Blender Blockout without Start Frame",
    32: "One Reference Video, Multiple Worlds",
    33: "Mixamo Multi-Character Storyboard Experiment",
    34: "Codex MCP Direct Blender Export",
    35: "Composition Reference with Person and Vehicle Refs",
}

EN_TAKEAWAYS = {
    1: "A merged direction workflow: use the full gray-box method from the original case, then push it into action-previs timing, speed, shake, and spatial choreography before Seedance generation.",
    2: "A compact precision-camera recipe: Blender supplies the camera move, Midjourney supplies the start frame, and Seedance follows the motion reference.",
    3: "A dialogue-shot workflow where Blender is used to match character poses and camera motion before Seedance generates the performed scene.",
    5: "An action-previs case showing how rough timing, speed, camera shake, and spatial choreography can be planned in Blender before Seedance renders the shot.",
    6: "A handheld-follow case where Blender controls how a character travels through space and Seedance carries the gritty camera move into the final video.",
    7: "A merged reproducibility and troubleshooting case: the setup spells out the reference-video conditions, while the paired test records where camera/rhythm control worked and foot motion failed.",
    8: "A limitation case: Blender successfully controls camera, rhythm, and subject path, while natural foot motion still needs better handling.",
    9: "An agentic Blender MCP case where Codex builds a simple 3D market, cat motion, camera framing, and an MP4 reference for Seedance.",
    10: "A reference-mapping case that uses Blender blocking plus multiple character and environment references to tell Seedance which figure should become which character.",
    14: "A ComfyUI control case where Blender previz is combined with separate upright and upside-down reference frames to test motion adherence.",
    19: "A tactical blocking case where Blender directs camera orbit, lens choice, cover positions, gunfire beats, and character movement before generation.",
    20: "A multi-tool agent pipeline where Hermes installs and connects Krea, ComfyUI, Blender MCP, and Seedance to produce both image and physical references.",
    21: "A viewport-to-style-transfer case: Blender MCP provides camera and element control, then Seedance/Magnific add texture and lighting.",
    23: "A beginner-friendly motion-source case: use Mixamo motion in Blender as the controllable movement base before sending the reference to Seedance.",
    24: "A Codex-assisted beginner case where architecture and camera work are generated in Blender and then tested as Seedance reference motion.",
    25: "A 3D-previs-to-anime case showing how camera moves and motion can be preserved while Seedance changes the render style.",
    28: "A short viewport-preview tutorial: block out the scene, export the preview, turn the first frame realistic, then provide both references to Seedance.",
    29: "An FBX clay-pass workflow where Blender imports the motion, Claude helps keyframe camera moves, and the rendered pass becomes Seedance reference video.",
    31: "A no-start-frame variant showing that Blender blockout plus detailed environment references can work when the workflow cannot rely on a starter frame.",
    32: "A style/world-variation case where the same Blender reference video drives different generated worlds in Seedance.",
}

EN_NOTES = {
    1: "Merged with former case 7: together these sources show the full gray-box workflow and the action-previs variant with rough timing, speed, shake, and spatial choreography.",
    2: "The source gives a clear three-step workflow and reports that the generated video tracks the Blender camera move closely.",
    3: "The source adds multi-character dialogue and pose matching, making it distinct from single-character camera-control demos.",
    5: "The source focuses on action timing, speed, rough camera shake, and spatial choreography rather than only camera path.",
    6: "The source moves the character through the scene while the camera follows, which makes it useful for handheld movement shots.",
    7: "Merged with former case 19: the pair keeps both the reproducible setup and the limitation note about foot sliding.",
    8: "This is kept as a troubleshooting case because it names what Blender controlled well and where the motion still failed.",
    9: "The author says the test was inspired by another creator, but the described scene, motion, camera, and export process are their own experiment.",
    10: "The source explains how to pair a blocking reference with multiple still references so Seedance maps the moving figures correctly.",
    14: "The case is useful because it combines Blender previz with multiple still references inside a ComfyUI-style control setup.",
    19: "The source shows simultaneous camera and character blocking, which is stronger than a simple camera-only reference.",
    20: "The case demonstrates a broader agent-built creative stack, not just manual Blender previs.",
    21: "This is the stronger techhalla source because it explains the viewport animation and downstream style/lighting step.",
    23: "The source is useful for beginners because it names Mixamo as a practical motion source for Blender reference videos.",
    24: "The post is valuable as a beginner Codex workflow: the user delegates architecture and camera work to Codex before Seedance.",
    25: "The source directly frames the workflow as Blender 3D previz transformed into an anime render while keeping camera motion.",
    28: "The post gives a concise workflow with concrete artifacts: viewport preview, first-frame image, and Seedance reference video. The duplicate case 29 media was removed so the public case shows only one copy of the same video.",
    29: "The source gives a specific FBX-to-clay-pass process and includes camera keyframing before reference export.",
    31: "This case covers an important variant where reference images replace the usual start-frame dependency.",
    32: "The source is useful because it separates motion control from world/style variation using the same reference video.",
}

ZH_TAKEAWAYS = {
    1: "合并后的导演流程：保留原始灰盒方法，再加入动作预演里的时序、速度、抖动和空间调度，最后交给 Seedance 生成。",
    2: "精确运镜的三步配方：Blender 负责相机运动，Midjourney 负责起始帧，Seedance 按参考运动生成视频。",
    3: "多角色对话镜头：先在 Blender 里匹配角色姿势和相机运动，再让 Seedance 生成表演结果。",
    5: "动作戏预演：用 Blender 规划粗略时序、速度、抖动和空间调度，再交给 Seedance 渲染成片。",
    6: "手持跟拍：Blender 控制角色穿越空间和相机跟随，Seedance 把这种粗粝跟拍感带到最终视频。",
    7: "合并后的复现与排查案例：一条写清参考视频条件，另一条记录相机/节奏控制有效但脚步动作仍会失败。",
    8: "限制排查案例：Blender 能控制相机、节奏和移动路径，但自然脚步动作仍然容易出问题。",
    9: "Agentic Blender MCP 案例：Codex 生成简易市场、猫的动作、相机构图，并导出给 Seedance 的 MP4 参考。",
    10: "参考映射案例：用 Blender blocking 加多张角色/环境参考，告诉 Seedance 哪个运动物体对应哪个角色。",
    14: "ComfyUI 控制案例：Blender previz 搭配 upright/upside-down 参考帧，测试 Seedance 的运动遵循能力。",
    19: "战术动作 blocking：在生成前用 Blender 规划相机环绕、镜头、掩体位置、枪火节奏和角色移动。",
    20: "多工具 agent 管线：Hermes 安装并连接 Krea、ComfyUI、Blender MCP 和 Seedance，生成图像与物理参考。",
    21: "Viewport 到风格化案例：Blender MCP 提供相机和元素控制，再用 Seedance/Magnific 加纹理和光照。",
    23: "新手运动来源案例：从 Mixamo 拿动作导入 Blender，作为可控运动基础后再送入 Seedance。",
    24: "Codex 辅助新手案例：建筑和 camera work 由 Codex 在 Blender 中生成，再测试 Seedance 参考运动。",
    25: "3D previz 到动画渲染：用 Seedance 改变画面风格，同时保留 Blender 里的相机运动和动作。",
    28: "Viewport preview 教程：blockout 场景、导出预览、把首帧转成真实图，再把两类参考交给 Seedance。",
    29: "FBX clay pass 流程：Blender 导入动作，Claude 辅助关键帧相机，渲染后的 clay pass 成为 Seedance 参考视频。",
    31: "无起始帧变体：当不能依赖 starter frame 时，用 Blender blockout 加详细环境参考也能工作。",
    32: "同一参考视频生成不同世界：用同一段 Blender reference 锁定运动，再让 Seedance 改变世界和风格。",
}

TYPE_FOR_CATEGORY = {
    "camera-control": "Demo",
    "character-action": "Demo",
    "agentic-mcp": "Integration",
    "reference-prompt": "Tutorial",
    "production-pipeline": "Integration",
    "limitations": "Limit",
}

MANUAL_CASES = [
    {
        "case": 21,
        "source_index": None,
        "id": "2071595581508563168",
        "url": "https://x.com/reidhannaford/status/2071595581508563168",
        "author": "@reidhannaford",
        "author_url": "https://x.com/reidhannaford",
        "date": "2026-06-29",
        "category": "character-action",
        "title": "Ambush Scene Previs Beyond a Simple Camera Move",
        "title_zh": "伏击场景 previs + Seedance 动作调度",
        "evidence_type": "Demo",
        "quality_tier": "strong",
        "source_role": "primary_original",
        "why_selected_zh": "明确把 Midjourney 起始图、Blender blocking/相机动画和 Seedance 组合，用于复杂伏击场景而不只是简单运镜。",
        "reuse_angle_zh": "适合做复杂场景先解决 staging、timing 和 camera movement，再生成镜头的案例。",
        "source_text": "Seedance 2.0 is insane. Blender previs is having a moment in AI filmmaking for a reason. I wanted to see how far I could push the workflow beyond a simple camera move in an ambush scene. The workflow: make a start image in Midjourney, block it out in Blender, animate the camera, feed both to Seedance.",
        "takeaway_en": "An ambush-scene case showing how Blender previs can solve staging, timing, and camera movement before Seedance generates the shot.",
        "takeaway_zh": "伏击场景案例：先用 Blender previs 解决 staging、timing 和 camera movement，再交给 Seedance 生成镜头。",
        "note_en": "Requested as case 21. Kept as a distinct Reid Hannaford example because it pushes the workflow beyond a simple camera move into scene staging.",
        "local_media": ["media/case21.mp4"],
    },
    {
        "case": 22,
        "source_index": None,
        "id": "2071401550845481090",
        "url": "https://x.com/JoshDaws/status/2071401550845481090",
        "author": "@JoshDaws",
        "author_url": "https://x.com/JoshDaws",
        "date": "2026-06-29",
        "category": "agentic-mcp",
        "title": "Claude-Built Blender MCP Previs in Minutes",
        "title_zh": "Claude 用 Blender MCP 几分钟生成 previs",
        "evidence_type": "Integration",
        "quality_tier": "medium",
        "source_role": "primary_original",
        "why_selected_zh": "说明 Claude 通过 Blender MCP 为镜头创建 previs，并强调 2-3 分钟完成。",
        "reuse_angle_zh": "适合做 agent 快速搭建镜头预演的短案例。",
        "source_text": "Yup. Had Claude use Blender MCP to create previs for a shot in the next installment of Mary Sue. Worked like a charm. Took Claude 2-3 minutes to make this.",
        "takeaway_en": "A fast agentic-previs case where Claude uses Blender MCP to build a shot reference in two to three minutes.",
        "takeaway_zh": "快速 agentic previs 案例：Claude 通过 Blender MCP 在 2-3 分钟内搭出镜头参考。",
        "note_en": "Requested as case 22. Kept because it demonstrates speed and agent control rather than manual Blender work.",
        "local_media": ["media/case22.mp4"],
    },
    {
        "case": 23,
        "source_index": None,
        "id": "2071380621214224403",
        "url": "https://x.com/kan_mi_no9/status/2071380621214224403",
        "author": "@kan_mi_no9",
        "author_url": "https://x.com/kan_mi_no9",
        "date": "2026-06-28",
        "category": "reference-prompt",
        "title": "Position-Only Reference Control for a Faster Scene",
        "title_zh": "只保留位置关系的参考控制",
        "evidence_type": "Tutorial",
        "quality_tier": "medium",
        "source_role": "primary_original",
        "why_selected_zh": "说明通过调低参考视频对动作的约束、聚焦位置关系，补回 Seedance 的速度感和动态感。",
        "reuse_angle_zh": "适合做 reference adherence 调参案例。",
        "source_text": "A derivative experiment from a previous split-body test. The author notes that by narrowing the reference degree toward positional relationships, Seedance came closer to the intended speed and image even when the original previs was not fast.",
        "takeaway_en": "A reference-weighting case: keep the reference useful for positions while letting the prompt recover speed and dynamism.",
        "takeaway_zh": "参考权重案例：只让参考视频约束位置关系，再用 prompt 补回速度感和动态感。",
        "note_en": "Requested as case 23. Kept with the paired kan_mi_no9 test as a distinct reference-control variant.",
        "local_media": ["media/case23.mp4"],
    },
    {
        "case": 24,
        "source_index": None,
        "id": "2070617538745229546",
        "url": "https://x.com/gcduncombe/status/2070617538745229546",
        "author": "@gcduncombe",
        "author_url": "https://x.com/gcduncombe",
        "date": "2026-06-26",
        "category": "reference-prompt",
        "title": "Physical Toy Reference Instead of 3D Software",
        "title_zh": "用实体玩具替代 3D 软件做参考",
        "evidence_type": "Demo",
        "quality_tier": "medium",
        "source_role": "primary_original",
        "why_selected_zh": "提出不打开 3D 软件时也可以用玩具拍摄运动/构图参考，作为 Blender+AI render 讨论的替代路径。",
        "reuse_angle_zh": "适合做 physical previs / toy reference 的轻量替代案例。",
        "source_text": "Everyone is talking about Blender + an AI rendering step but if you don't feel like cracking open 3d software, just use your kids' toys.",
        "takeaway_en": "A physical-reference case: use toys as quick motion and staging references when opening Blender is too much overhead.",
        "takeaway_zh": "实体参考案例：当不想打开 Blender 时，用玩具快速拍摄运动和 staging 参考。",
        "note_en": "Requested as case 24. Kept because it expands the reference-video idea beyond software-only previs.",
        "local_media": ["media/case24.mp4"],
    },
    {
        "case": 25,
        "source_index": None,
        "id": "2071002538703479089",
        "url": "https://x.com/tea_story_hoshi/status/2071002538703479089",
        "author": "@tea_story_hoshi",
        "author_url": "https://x.com/tea_story_hoshi",
        "date": "2026-06-27",
        "category": "limitations",
        "title": "Toy Reference Prompt Reinforcement and NG Example",
        "title_zh": "玩具参考 + prompt 补强 + NG 对照",
        "evidence_type": "Limit",
        "quality_tier": "strong",
        "source_role": "primary_original",
        "why_selected_zh": "同时给出成功例和 NG 例：解析参考视频并用 prompt 补强会更自然，直接忠实参考则动作和姿势容易僵硬。",
        "reuse_angle_zh": "适合做 reference video troubleshooting 与 prompt reinforcement 案例。",
        "source_text": "The author uses toy-shot references with Seedance 2 Mini, compares prompt-reinforced outputs against an NG example, and notes that direct reference adherence can make movement and poses feel stiff.",
        "takeaway_en": "A troubleshooting case showing why reference videos often need prompt reinforcement instead of raw imitation.",
        "takeaway_zh": "排查案例：参考视频通常需要 prompt 补强，不能只让模型机械照搬。",
        "note_en": "Requested as case 25. Kept because it includes both working examples and a failed comparison.",
        "local_media": ["media/case25.jpg", "media/case25.mp4"],
    },
    {
        "case": 26,
        "source_index": None,
        "id": "2071168235022827587",
        "url": "https://x.com/kan_mi_no9/status/2071168235022827587",
        "author": "@kan_mi_no9",
        "author_url": "https://x.com/kan_mi_no9",
        "date": "2026-06-28",
        "category": "reference-prompt",
        "title": "Reference Control for a Specific Failed Prompt Scene",
        "title_zh": "用参考控制修复 prompt 反复失败的场景",
        "evidence_type": "Demo",
        "quality_tier": "medium",
        "source_role": "primary_original",
        "why_selected_zh": "说明虽然会损失部分 Seedance 自由运镜和动态，但在必须得到特定画面的场景里很有用。",
        "reuse_angle_zh": "适合做“prompt 失败时用 reference 兜底”的案例。",
        "source_text": "The author notes that reference control can reduce some of Seedance 2.0's camera freedom and dynamism, but it helped in a work scene where prompt-only attempts repeatedly failed.",
        "takeaway_en": "A control fallback case: when prompt-only generation fails, use a reference to force the scene even if some dynamism is reduced.",
        "takeaway_zh": "控制兜底案例：prompt-only 反复失败时，用 reference 强制场景成立，即使会损失部分动态。",
        "note_en": "Requested as case 26. Kept as the practical counterpart to the later kan_mi_no9 variation case.",
        "local_media": ["media/case26.mp4"],
    },
    {
        "case": 27,
        "source_index": None,
        "id": "2070512271391068287",
        "url": "https://x.com/craftcapitallab/status/2070512271391068287",
        "author": "@craftcapitallab",
        "author_url": "https://x.com/craftcapitallab",
        "date": "2026-06-26",
        "category": "reference-prompt",
        "title": "Character Proportion and Simple Background Tips",
        "title_zh": "角色比例与简化背景的稳定性技巧",
        "evidence_type": "Tutorial",
        "quality_tier": "medium",
        "source_role": "primary_original",
        "why_selected_zh": "总结了让参考更稳定的具体技巧：figure 不只调头身，还要让手脚体积贴合角色设计；不需要对齐的背景尽量简单。",
        "reuse_angle_zh": "适合做 Blender/参考视频的稳定性 checklist。",
        "source_text": "The author shares practical tips: match not just body height but arm and leg volume to the character design, and keep backgrounds that do not need matching as simple models.",
        "takeaway_en": "A stability checklist case: match character proportions beyond height and simplify any background that does not need precise alignment.",
        "takeaway_zh": "稳定性 checklist：角色比例不只看头身，还要匹配手脚体积；无须对齐的背景尽量简化。",
        "note_en": "Requested as case 27. Kept because it offers specific, reusable setup advice.",
        "local_media": ["media/case27.mp4"],
    },
    {
        "case": 28,
        "source_index": None,
        "id": "2070577334701473800",
        "url": "https://x.com/fatboypink/status/2070577334701473800",
        "author": "@fatboypink",
        "author_url": "https://x.com/fatboypink",
        "date": "2026-06-26",
        "category": "limitations",
        "title": "Cloth Physics Stress Test with Blender and Seedance",
        "title_zh": "Blender + Seedance 布料物理压力测试",
        "evidence_type": "Limit",
        "quality_tier": "medium",
        "source_role": "primary_original",
        "why_selected_zh": "明确把目标设为测试 Seedance 对 cloth physics 的处理能力，并说明这是较难解决的输出。",
        "reuse_angle_zh": "适合做 cloth physics / complex motion stress test 案例。",
        "source_text": "Another Blender + Seedance production testing how well Seedance handled cloth physics. The author says it was the most challenging output to solve and still has room for exploration.",
        "takeaway_en": "A cloth-physics stress test showing where Blender-guided Seedance can work but still needs iteration for difficult motion.",
        "takeaway_zh": "布料物理压力测试：Blender-guided Seedance 可用，但复杂运动仍需要多轮迭代。",
        "note_en": "Requested as case 28. Kept as a concrete limitation/stress-test case.",
        "local_media": ["media/case28.mp4"],
    },
]

LOCALE = {
    "en": {
        "intro": "Welcome to the Blender + Seedance usecase repository.",
        "value": "We collect real-world Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI, and agent-assisted workflows that creators used to control Seedance video generation.",
        "source": "The current collection is curated from user-provided X/Twitter source data. Each case links to the original post and creator profile.",
        "cta": "The Quick Start below walks users through Blender MCP setup, EvoLink skill installation, API key setup, and running the workflow inside an agent.",
        "overview_note": "The collection favors concrete workflow evidence over hype: source-backed steps, reference-video methods, agent/MCP usage, reproducible constraints, and clearly stated limits.",
        "quick": "Quick Start Workflow",
        "quick_text": "Set up Blender MCP, install EvoLink skills, configure the API key, and run the workflow inside an agent.",
        "pending": "Final Landing Page Pending",
        "pending_body": "The final landing page is still pending. Until then, the Quick Start workflow is the primary conversion path.",
        "menu": "Menu",
        "ack": "Acknowledge",
        "what": "What it shows",
        "case": "Case",
        "type": "Type",
        "date": "Date",
        "section": "Section",
        "cases": "Cases",
        "takeaway_prefix": "Use this case to",
        "notes_prefix": "Source notes",
    },
    "es": {
        "intro": "Repositorio de casos de uso Blender + Seedance.",
        "value": "Reunimos flujos reales de Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI y agentes para controlar la generación de video con Seedance.",
        "source": "La colección actual se deriva de datos X/Twitter proporcionados por el propietario. Cada caso enlaza la publicación original y el perfil del creador.",
        "cta": "El Quick Start de abajo guía la instalación de Blender MCP, las skills de EvoLink, la API key y la ejecución dentro de un agente.",
        "overview_note": "La colección prioriza evidencia concreta: pasos, referencias de video, uso de agentes/MCP, restricciones reproducibles y límites claros.",
        "quick": "Acceso rápido a API",
        "quick_text": "Esta sección conserva la ruta esperada del modelo Seedance reference-to-video hasta que exista la landing final.",
        "pending": "Ruta de conversión pendiente",
        "pending_body": "La landing final sigue pendiente. Sustituye esta sección por el CTA final antes de marcar el repositorio como listo para release.",
        "menu": "Menú",
        "ack": "Agradecimientos",
        "what": "Qué muestra",
        "case": "Caso",
        "type": "Tipo",
        "date": "Fecha",
        "section": "Sección",
        "cases": "Casos",
        "takeaway_prefix": "Usa este caso para",
        "notes_prefix": "Notas de la fuente",
    },
    "pt": {
        "intro": "Repositório de casos de uso Blender + Seedance.",
        "value": "Reunimos fluxos reais com Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI e agentes para controlar a geração de vídeo no Seedance.",
        "source": "A coleção vem dos dados X/Twitter fornecidos pelo proprietário. Cada caso aponta para o post original e o criador.",
        "cta": "O Quick Start abaixo guia a instalação do Blender MCP, das skills EvoLink, da API key e a execução dentro de um agente.",
        "overview_note": "A coleção prioriza evidência concreta: passos, vídeos de referência, uso de agente/MCP, restrições reproduzíveis e limites claros.",
        "quick": "Acesso rápido à API",
        "quick_text": "Esta seção registra o caminho esperado do modelo Seedance reference-to-video até a landing final existir.",
        "pending": "Caminho de conversão pendente",
        "pending_body": "A landing final ainda está pendente. Substitua esta seção pelo CTA final antes de marcar o repositório como pronto para release.",
        "menu": "Menu",
        "ack": "Agradecimentos",
        "what": "O que mostra",
        "case": "Caso",
        "type": "Tipo",
        "date": "Data",
        "section": "Seção",
        "cases": "Casos",
        "takeaway_prefix": "Use este caso para",
        "notes_prefix": "Notas da fonte",
    },
    "ja": {
        "intro": "Blender + Seedance のユースケース集です。",
        "value": "Blender、Blender MCP、viewport、previs、FBX、Mixamo、ComfyUI、agent 支援で Seedance 動画生成を制御する実例を集めています。",
        "source": "現在のコレクションは、所有者提供の X/Twitter データから整理されています。各ケースは元投稿と作者プロフィールにリンクします。",
        "cta": "下の Quick Start で、Blender MCP setup、EvoLink skill、API key、agent 内での実行まで案内します。",
        "overview_note": "このコレクションは宣伝よりも具体的な証拠を優先します。手順、参照動画、agent/MCP 利用、再現条件、明確な制限を重視します。",
        "quick": "API クイックアクセス",
        "quick_text": "最終 landing が提供されるまで、ここには Seedance reference-to-video の想定モデル経路を記録します。",
        "pending": "コンバージョン経路は未確定",
        "pending_body": "最終 landing はまだ未確定です。release-ready と呼ぶ前に、この節を最終 CTA に置き換えてください。",
        "menu": "メニュー",
        "ack": "謝辞",
        "what": "内容",
        "case": "ケース",
        "type": "Type",
        "date": "Date",
        "section": "セクション",
        "cases": "ケース",
        "takeaway_prefix": "このケースは次に使えます:",
        "notes_prefix": "ソースメモ",
    },
    "ko": {
        "intro": "Blender + Seedance 유스케이스 저장소입니다.",
        "value": "Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI, agent 기반 워크플로로 Seedance 비디오 생성을 제어한 실제 사례를 모았습니다.",
        "source": "현재 컬렉션은 소유자가 제공한 X/Twitter 데이터에서 선별했습니다. 각 사례는 원본 게시물과 제작자 프로필로 연결됩니다.",
        "cta": "아래 Quick Start에서 Blender MCP setup, EvoLink skill 설치, API key 설정, 에이전트 안에서 실행하는 흐름을 안내합니다.",
        "overview_note": "이 컬렉션은 과장보다 구체적 근거를 우선합니다: 단계, reference video, agent/MCP 사용, 재현 조건, 명확한 한계.",
        "quick": "API 빠른 접근",
        "quick_text": "최종 landing 이 제공되기 전까지 Seedance reference-to-video 모델 경로를 기록합니다.",
        "pending": "전환 경로 대기 중",
        "pending_body": "최종 landing 은 아직 미정입니다. release-ready 로 표시하기 전에 이 섹션을 최종 CTA 로 교체하세요.",
        "menu": "메뉴",
        "ack": "감사의 말",
        "what": "보여주는 것",
        "case": "사례",
        "type": "Type",
        "date": "Date",
        "section": "섹션",
        "cases": "사례",
        "takeaway_prefix": "이 사례를 활용해",
        "notes_prefix": "소스 메모",
    },
    "de": {
        "intro": "Usecase-Repository für Blender + Seedance.",
        "value": "Wir sammeln reale Workflows mit Blender, Blender MCP, Viewport, Previs, FBX, Mixamo, ComfyUI und Agentensteuerung für Seedance-Videogenerierung.",
        "source": "Die aktuelle Sammlung stammt aus vom Owner bereitgestellten X/Twitter-Daten. Jeder Fall verlinkt Quelle und Creator-Profil.",
        "cta": "Der Quick Start unten führt durch Blender MCP Setup, EvoLink Skill Installation, API key Einrichtung und Ausführung im Agenten.",
        "overview_note": "Die Sammlung bevorzugt konkrete Evidenz: Schritte, Referenzvideos, Agent/MCP-Nutzung, reproduzierbare Bedingungen und klare Grenzen.",
        "quick": "Schneller API-Zugang",
        "quick_text": "Bis zur finalen Landingpage dokumentiert dieser Abschnitt den erwarteten Seedance reference-to-video Modellpfad.",
        "pending": "Conversion-Pfad ausstehend",
        "pending_body": "Die finale Landingpage steht noch aus. Ersetze diesen Abschnitt durch den finalen CTA, bevor das Repository als release-ready gilt.",
        "menu": "Menü",
        "ack": "Danksagung",
        "what": "Was es zeigt",
        "case": "Fall",
        "type": "Typ",
        "date": "Datum",
        "section": "Abschnitt",
        "cases": "Fälle",
        "takeaway_prefix": "Nutze diesen Fall, um",
        "notes_prefix": "Quellnotizen",
    },
    "fr": {
        "intro": "Dépôt de cas d'usage Blender + Seedance.",
        "value": "Nous réunissons des workflows réels avec Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI et agents pour contrôler la génération vidéo Seedance.",
        "source": "La collection actuelle vient des données X/Twitter fournies par le propriétaire. Chaque cas renvoie vers la source et le profil du créateur.",
        "cta": "Le Quick Start ci-dessous couvre le setup Blender MCP, les skills EvoLink, l'API key et l'exécution dans un agent.",
        "overview_note": "La collection privilégie les preuves concrètes: étapes, vidéos de référence, usage agent/MCP, contraintes reproductibles et limites explicites.",
        "quick": "Accès API rapide",
        "quick_text": "Cette section conserve le chemin attendu du modèle Seedance reference-to-video jusqu'à la landing finale.",
        "pending": "Chemin de conversion en attente",
        "pending_body": "La landing finale est encore en attente. Remplacez cette section par le CTA final avant de qualifier le dépôt de release-ready.",
        "menu": "Menu",
        "ack": "Remerciements",
        "what": "Ce que cela montre",
        "case": "Cas",
        "type": "Type",
        "date": "Date",
        "section": "Section",
        "cases": "Cas",
        "takeaway_prefix": "Utilisez ce cas pour",
        "notes_prefix": "Notes de source",
    },
    "tr": {
        "intro": "Blender + Seedance kullanım örnekleri deposu.",
        "value": "Seedance video üretimini kontrol etmek için Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI ve agent destekli gerçek iş akışlarını topluyoruz.",
        "source": "Mevcut koleksiyon, sahibin sağladığı X/Twitter verilerinden seçildi. Her vaka orijinal gönderiye ve yaratıcı profiline bağlanır.",
        "cta": "Aşağıdaki Quick Start, Blender MCP setup, EvoLink skill kurulumu, API key ayarı ve agent içinde çalıştırma akışını gösterir.",
        "overview_note": "Koleksiyon abartı yerine somut kanıtı öne çıkarır: adımlar, referans videolar, agent/MCP kullanımı, yeniden üretilebilir koşullar ve net sınırlar.",
        "quick": "Hızlı API erişimi",
        "quick_text": "Final landing gelene kadar bu bölüm Seedance reference-to-video model yolunu kaydeder.",
        "pending": "Dönüşüm yolu beklemede",
        "pending_body": "Final landing sayfası hâlâ beklemede. Depoyu release-ready saymadan önce bu bölümü final CTA ile değiştirin.",
        "menu": "Menü",
        "ack": "Teşekkür",
        "what": "Ne gösteriyor",
        "case": "Vaka",
        "type": "Tür",
        "date": "Tarih",
        "section": "Bölüm",
        "cases": "Vakalar",
        "takeaway_prefix": "Bu vakayı şunun için kullanın:",
        "notes_prefix": "Kaynak notları",
    },
    "zh-CN": {
        "intro": "Blender + Seedance 使用案例仓库。",
        "value": "这里收集真实的 Blender、Blender MCP、viewport、previs、FBX、Mixamo、ComfyUI 和 agent 辅助工作流，用来控制 Seedance 视频生成。",
        "source": "当前集合来自用户提供的 X/Twitter 精选数据。每个案例都链接到原帖和创作者主页。",
        "cta": "下面的 Quick Start 会引导用户完成 Blender MCP setup、安装 EvoLink skills、配置 API key，并在自己的 agent 里运行。",
        "overview_note": "这个集合优先保留具体证据：步骤、参考视频、agent/MCP 用法、可复现条件和明确限制，而不是空泛宣传。",
        "quick": "快速 API 入口",
        "quick_text": "在最终落地页提供之前，这里记录 Seedance reference-to-video 的预期模型路径。",
        "pending": "转化路径待补齐",
        "pending_body": "最终落地页仍待补齐。把仓库标记为 release-ready 之前，需要把这一节替换成最终 CTA。",
        "menu": "目录",
        "ack": "致谢",
        "what": "展示内容",
        "case": "案例",
        "type": "类型",
        "date": "日期",
        "section": "章节",
        "cases": "案例",
        "takeaway_prefix": "用这个案例来",
        "notes_prefix": "来源笔记",
    },
    "zh-TW": {
        "intro": "Blender + Seedance 使用案例倉庫。",
        "value": "這裡收集真實的 Blender、Blender MCP、viewport、previs、FBX、Mixamo、ComfyUI 和 agent 輔助工作流，用來控制 Seedance 影片生成。",
        "source": "目前集合來自使用者提供的 X/Twitter 精選資料。每個案例都連結到原帖和創作者主頁。",
        "cta": "下面的 Quick Start 會引導使用者完成 Blender MCP setup、安裝 EvoLink skills、配置 API key，並在自己的 agent 裡執行。",
        "overview_note": "這個集合優先保留具體證據：步驟、參考影片、agent/MCP 用法、可重現條件和明確限制，而不是空泛宣傳。",
        "quick": "快速 API 入口",
        "quick_text": "在最終落地頁提供之前，這裡記錄 Seedance reference-to-video 的預期模型路徑。",
        "pending": "轉化路徑待補齊",
        "pending_body": "最終落地頁仍待補齊。把倉庫標記為 release-ready 之前，需要把這一節替換成最終 CTA。",
        "menu": "目錄",
        "ack": "致謝",
        "what": "展示內容",
        "case": "案例",
        "type": "類型",
        "date": "日期",
        "section": "章節",
        "cases": "案例",
        "takeaway_prefix": "用這個案例來",
        "notes_prefix": "來源筆記",
    },
    "ru": {
        "intro": "Репозиторий use cases Blender + Seedance.",
        "value": "Мы собираем реальные workflow с Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI и агентами для управления генерацией видео Seedance.",
        "source": "Текущая коллекция основана на X/Twitter данных, предоставленных владельцем. Каждый кейс ведет к исходному посту и профилю автора.",
        "cta": "Quick Start ниже показывает setup Blender MCP, установку EvoLink skills, настройку API key и запуск внутри агента.",
        "overview_note": "Коллекция ставит конкретные доказательства выше хайпа: шаги, reference video, agent/MCP, воспроизводимые условия и явные ограничения.",
        "quick": "Быстрый доступ к API",
        "quick_text": "До финальной landing page этот раздел фиксирует ожидаемый путь модели Seedance reference-to-video.",
        "pending": "Путь конверсии ожидается",
        "pending_body": "Финальная landing page пока ожидается. Замените этот раздел финальным CTA перед статусом release-ready.",
        "menu": "Меню",
        "ack": "Благодарности",
        "what": "Что показывает",
        "case": "Кейс",
        "type": "Тип",
        "date": "Дата",
        "section": "Раздел",
        "cases": "Кейсы",
        "takeaway_prefix": "Используйте этот кейс, чтобы",
        "notes_prefix": "Заметки источника",
    },
}

QUICK_START = {
    "en": {
        "title": "Quick Start Workflow",
        "intro": "Set up the local Blender control path first, then install the EvoLink skills your agent will call.",
        "mcp_title": "Install Blender MCP",
        "mcp_body": "Follow the official Blender MCP setup guide, open Blender, and make sure your agent can connect to the Blender MCP server before generating references.",
        "setup_label": "Official setup",
        "skill_title": "Install EvoLink skills",
        "skill_body": "Install the Seedance generation skill and the Topaz upscaling skill in the agent workspace.",
        "key_title": "Get an API key",
        "key_body": "Create an EvoLink API key from your account, then expose it to the agent runtime.",
        "run_title": "Run it inside your agent",
        "run_body": "After MCP, skills, and API key are ready, ask your agent to build a Blender blockout, export the reference video, generate with Seedance, and upscale the final clip when needed.",
        "agent_prompt": "Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.",
        "note": "The Blender MCP setup page is the source of truth for Blender-side installation details.",
    },
    "es": {
        "title": "Workflow de inicio rápido",
        "intro": "Primero prepara el control local de Blender; después instala las skills de EvoLink que llamará tu agente.",
        "mcp_title": "Instala Blender MCP",
        "mcp_body": "Sigue la guía oficial de Blender MCP, abre Blender y verifica que tu agente pueda conectarse al servidor Blender MCP antes de generar referencias.",
        "setup_label": "Setup oficial",
        "skill_title": "Instala las skills de EvoLink",
        "skill_body": "Instala la skill de generación Seedance y la skill de escalado Topaz en el workspace del agente.",
        "key_title": "Obtén una API key",
        "key_body": "Crea una API key de EvoLink en tu cuenta y exponla al runtime del agente.",
        "run_title": "Ejecútalo dentro de tu agente",
        "run_body": "Cuando MCP, skills y API key estén listos, pide al agente que construya un blockout en Blender, exporte el video de referencia, genere con Seedance y escale el clip final si hace falta.",
        "agent_prompt": "Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.",
        "note": "La página de setup de Blender MCP es la fuente principal para los detalles de instalación del lado de Blender.",
    },
    "pt": {
        "title": "Workflow de início rápido",
        "intro": "Configure primeiro o controle local do Blender; depois instale as skills EvoLink que o agente vai chamar.",
        "mcp_title": "Instale o Blender MCP",
        "mcp_body": "Siga o guia oficial de setup do Blender MCP, abra o Blender e confirme que o agente consegue se conectar ao servidor Blender MCP antes de gerar referências.",
        "setup_label": "Setup oficial",
        "skill_title": "Instale as skills EvoLink",
        "skill_body": "Instale a skill de geração Seedance e a skill de upscale Topaz no workspace do agente.",
        "key_title": "Obtenha uma API key",
        "key_body": "Crie uma API key da EvoLink na sua conta e exponha essa chave ao runtime do agente.",
        "run_title": "Execute dentro do seu agente",
        "run_body": "Com MCP, skills e API key prontos, peça ao agente para criar um blockout no Blender, exportar o vídeo de referência, gerar com Seedance e fazer upscale do resultado quando necessário.",
        "agent_prompt": "Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.",
        "note": "A página de setup do Blender MCP é a fonte principal para os detalhes de instalação no Blender.",
    },
    "ja": {
        "title": "Quick Start Workflow",
        "intro": "まず Blender を agent から制御できる状態にし、その後 agent が呼び出す EvoLink skill を入れます。",
        "mcp_title": "Blender MCP をインストール",
        "mcp_body": "公式の Blender MCP setup ガイドに従い、Blender を開いて、参照動画を作る前に agent が Blender MCP server に接続できることを確認します。",
        "setup_label": "公式 setup",
        "skill_title": "EvoLink skill をインストール",
        "skill_body": "agent workspace に Seedance 生成 skill と Topaz upscale skill をインストールします。",
        "key_title": "API key を取得",
        "key_body": "EvoLink アカウントで API key を作成し、agent runtime から参照できるようにします。",
        "run_title": "agent 内で実行",
        "run_body": "MCP、skill、API key が揃ったら、Blender blockout の作成、reference video の export、Seedance 生成、必要に応じた Topaz upscale を agent に依頼します。",
        "agent_prompt": "Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.",
        "note": "Blender 側のインストール詳細は Blender MCP setup ページを正とします。",
    },
    "ko": {
        "title": "Quick Start Workflow",
        "intro": "먼저 에이전트가 로컬 Blender를 제어할 수 있게 만들고, 그다음 에이전트가 호출할 EvoLink skill을 설치합니다.",
        "mcp_title": "Blender MCP 설치",
        "mcp_body": "공식 Blender MCP setup 가이드를 따르고, Blender를 연 뒤 레퍼런스를 만들기 전에 에이전트가 Blender MCP server에 연결되는지 확인합니다.",
        "setup_label": "공식 setup",
        "skill_title": "EvoLink skill 설치",
        "skill_body": "에이전트 workspace에 Seedance 생성 skill과 Topaz 업스케일 skill을 설치합니다.",
        "key_title": "API key 받기",
        "key_body": "EvoLink 계정에서 API key를 만들고 에이전트 runtime에서 읽을 수 있게 설정합니다.",
        "run_title": "에이전트 안에서 실행",
        "run_body": "MCP, skill, API key가 준비되면 에이전트에게 Blender blockout 생성, reference video export, Seedance 생성, 필요한 경우 Topaz upscale까지 맡깁니다.",
        "agent_prompt": "Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.",
        "note": "Blender 쪽 설치 세부사항은 Blender MCP setup 페이지를 기준으로 합니다.",
    },
    "de": {
        "title": "Quick Start Workflow",
        "intro": "Richte zuerst die lokale Blender-Steuerung ein, danach installierst du die EvoLink Skills, die dein Agent aufruft.",
        "mcp_title": "Blender MCP installieren",
        "mcp_body": "Folge dem offiziellen Blender MCP Setup, öffne Blender und prüfe vor der Referenzgenerierung, dass dein Agent den Blender MCP Server erreicht.",
        "setup_label": "Offizielles Setup",
        "skill_title": "EvoLink Skills installieren",
        "skill_body": "Installiere den Seedance-Generierungsskill und den Topaz-Upscaling-Skill im Agent-Workspace.",
        "key_title": "API key holen",
        "key_body": "Erstelle in deinem EvoLink Account einen API key und stelle ihn der Agent Runtime bereit.",
        "run_title": "Im Agent ausführen",
        "run_body": "Wenn MCP, Skills und API key bereit sind, lässt du den Agent ein Blender Blockout bauen, das Reference Video exportieren, mit Seedance generieren und bei Bedarf mit Topaz hochskalieren.",
        "agent_prompt": "Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.",
        "note": "Die Blender MCP Setup-Seite bleibt die maßgebliche Quelle für Blender-seitige Installationsdetails.",
    },
    "fr": {
        "title": "Workflow de démarrage rapide",
        "intro": "Configurez d'abord le contrôle local de Blender, puis installez les skills EvoLink que votre agent appellera.",
        "mcp_title": "Installer Blender MCP",
        "mcp_body": "Suivez le guide officiel Blender MCP, ouvrez Blender et vérifiez que votre agent peut se connecter au serveur Blender MCP avant de générer des références.",
        "setup_label": "Setup officiel",
        "skill_title": "Installer les skills EvoLink",
        "skill_body": "Installez la skill de génération Seedance et la skill d'upscale Topaz dans le workspace de l'agent.",
        "key_title": "Obtenir une API key",
        "key_body": "Créez une API key EvoLink depuis votre compte, puis exposez-la au runtime de l'agent.",
        "run_title": "Lancer dans votre agent",
        "run_body": "Une fois MCP, skills et API key prêts, demandez à l'agent de créer un blockout Blender, d'exporter la vidéo de référence, de générer avec Seedance et d'upscaler le clip final si nécessaire.",
        "agent_prompt": "Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.",
        "note": "La page de setup Blender MCP reste la source de vérité pour les détails d'installation côté Blender.",
    },
    "tr": {
        "title": "Hızlı başlangıç workflow'u",
        "intro": "Önce yerel Blender kontrol yolunu kurun, ardından agent'ın çağıracağı EvoLink skill'lerini yükleyin.",
        "mcp_title": "Blender MCP kurulumu",
        "mcp_body": "Resmi Blender MCP setup rehberini izleyin, Blender'ı açın ve referans üretmeden önce agent'ın Blender MCP server'a bağlanabildiğini doğrulayın.",
        "setup_label": "Resmi setup",
        "skill_title": "EvoLink skill'lerini kurun",
        "skill_body": "Agent workspace içinde Seedance üretim skill'ini ve Topaz upscale skill'ini kurun.",
        "key_title": "API key alın",
        "key_body": "EvoLink hesabınızdan bir API key oluşturun ve agent runtime'a tanıtın.",
        "run_title": "Agent içinde çalıştırın",
        "run_body": "MCP, skill'ler ve API key hazır olduğunda agent'tan Blender blockout oluşturmasını, reference video export etmesini, Seedance ile üretmesini ve gerekirse Topaz ile upscale yapmasını isteyin.",
        "agent_prompt": "Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.",
        "note": "Blender tarafındaki kurulum ayrıntıları için Blender MCP setup sayfası esas kaynaktır.",
    },
    "zh-CN": {
        "title": "Quick Start 工作流",
        "intro": "先把本地 Blender 控制链路搭好，再安装 agent 会调用的 EvoLink skills。",
        "mcp_title": "安装 Blender MCP",
        "mcp_body": "按照官方 Blender MCP setup 页面完成配置，打开 Blender，并在生成参考视频之前确认 agent 能连接到 Blender MCP server。",
        "setup_label": "官方 setup",
        "skill_title": "安装 EvoLink skills",
        "skill_body": "在 agent workspace 里安装 Seedance 生成 skill 和 Topaz 视频放大 skill。",
        "key_title": "获取 API key",
        "key_body": "在 EvoLink 账号里创建 API key，然后把它暴露给 agent runtime。",
        "run_title": "在自己的 agent 里运行",
        "run_body": "MCP、skills 和 API key 都准备好之后，就可以让 agent 创建 Blender blockout、导出参考视频、调用 Seedance 生成，并在需要时用 Topaz 放大最终视频。",
        "agent_prompt": "Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.",
        "note": "Blender 侧安装细节以 Blender MCP setup 页面为准。",
    },
    "zh-TW": {
        "title": "Quick Start 工作流",
        "intro": "先把本地 Blender 控制鏈路搭好，再安裝 agent 會呼叫的 EvoLink skills。",
        "mcp_title": "安裝 Blender MCP",
        "mcp_body": "按照官方 Blender MCP setup 頁面完成配置，開啟 Blender，並在生成參考影片之前確認 agent 能連接到 Blender MCP server。",
        "setup_label": "官方 setup",
        "skill_title": "安裝 EvoLink skills",
        "skill_body": "在 agent workspace 裡安裝 Seedance 生成 skill 和 Topaz 影片放大 skill。",
        "key_title": "取得 API key",
        "key_body": "在 EvoLink 帳號裡建立 API key，然後把它暴露給 agent runtime。",
        "run_title": "在自己的 agent 裡執行",
        "run_body": "MCP、skills 和 API key 都準備好之後，就可以讓 agent 建立 Blender blockout、匯出參考影片、呼叫 Seedance 生成，並在需要時用 Topaz 放大最終影片。",
        "agent_prompt": "Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.",
        "note": "Blender 側安裝細節以 Blender MCP setup 頁面為準。",
    },
    "ru": {
        "title": "Quick Start Workflow",
        "intro": "Сначала настройте локальное управление Blender, затем установите EvoLink skills, которые будет вызывать агент.",
        "mcp_title": "Установить Blender MCP",
        "mcp_body": "Следуйте официальному setup Blender MCP, откройте Blender и проверьте, что агент подключается к Blender MCP server до генерации references.",
        "setup_label": "Официальный setup",
        "skill_title": "Установить EvoLink skills",
        "skill_body": "Установите skill для генерации Seedance и skill для Topaz upscale в workspace агента.",
        "key_title": "Получить API key",
        "key_body": "Создайте API key в аккаунте EvoLink и передайте его в runtime агента.",
        "run_title": "Запустить внутри агента",
        "run_body": "Когда MCP, skills и API key готовы, попросите агента создать Blender blockout, экспортировать reference video, сгенерировать результат через Seedance и при необходимости улучшить финальный клип через Topaz.",
        "agent_prompt": "Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.",
        "note": "Страница Blender MCP setup остается главным источником деталей установки со стороны Blender.",
    },
}


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def date_only(value: str) -> str:
    return value[:10]


def zh_tw(text: str) -> str:
    replacements = {
        "预": "預",
        "帧": "幀",
        "参考": "參考",
        "视频": "影片",
        "导": "導",
        "现": "現",
        "复": "複",
        "语": "語",
        "条": "條",
        "输": "輸",
        "个": "個",
        "对": "對",
        "话": "話",
        "镜": "鏡",
        "场": "場",
        "实": "實",
        "际": "際",
        "验": "驗",
        "发": "發",
        "动": "動",
        "节": "節",
        "问": "問",
        "题": "題",
        "连": "連",
        "试": "試",
        "猫": "貓",
        "鱼": "魚",
        "简": "簡",
        "写": "寫",
        "图": "圖",
        "摄": "攝",
        "览": "覽",
        "转": "轉",
        "构": "構",
        "组": "組",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return text


def local_case_title(item: dict, index: int, lang: str) -> str:
    if lang == "zh-CN":
        return item.get("use_case_title_zh") or EN_TITLES[index]
    if lang == "zh-TW":
        return zh_tw(item.get("use_case_title_zh") or EN_TITLES[index])
    return EN_TITLES[index]


def usage_takeaway(item: dict, index: int, lang: str) -> str:
    if lang == "en":
        return EN_TAKEAWAYS[index]
    if lang in {"zh-CN", "zh-TW"}:
        text = ZH_TAKEAWAYS[index]
        return zh_tw(text) if lang == "zh-TW" else text
    return EN_TAKEAWAYS[index]


def source_notes(item: dict, index: int, lang: str) -> str:
    why = clean(item.get("why_selected_zh", ""))
    reuse = clean(item.get("reuse_angle_zh", ""))
    note = EN_NOTES[index]
    if lang == "zh-CN":
        return f"- {LOCALE[lang]['notes_prefix']}：{why}\n- 复用角度：{reuse}"
    if lang == "zh-TW":
        return f"- {LOCALE[lang]['notes_prefix']}：{zh_tw(why)}\n- 複用角度：{zh_tw(reuse)}"
    return (
        f"- {LOCALE[lang]['notes_prefix']}: {note}\n"
        f"- Audit status: kept after manual duplicate and originality review."
    )


def valid_media_links(paths: list[str]) -> list[str]:
    return [path for path in paths if (ROOT / path).exists()]


def record_title(record: dict, lang: str) -> str:
    if lang == "zh-CN":
        return record.get("title_zh") or record["title"]
    if lang == "zh-TW":
        return zh_tw(record.get("title_zh") or record["title"])
    return record["title"]


def record_takeaway(record: dict, lang: str) -> str:
    if lang == "zh-CN":
        return record.get("takeaway_zh") or record.get("takeaway_en") or record["title"]
    if lang == "zh-TW":
        return zh_tw(record.get("takeaway_zh") or record.get("takeaway_en") or record["title"])
    return record.get("takeaway_en") or record["title"]


def record_notes(record: dict, lang: str) -> str:
    if lang == "zh-CN":
        why = clean(record.get("why_selected_zh", ""))
        reuse = clean(record.get("reuse_angle_zh", ""))
        lines = []
        if why:
            lines.append(f"- {LOCALE[lang]['notes_prefix']}：{why}")
        if reuse:
            lines.append(f"- 复用角度：{reuse}")
        return "\n".join(lines)
    if lang == "zh-TW":
        why = clean(record.get("why_selected_zh", ""))
        reuse = clean(record.get("reuse_angle_zh", ""))
        lines = []
        if why:
            lines.append(f"- {LOCALE[lang]['notes_prefix']}：{zh_tw(why)}")
        if reuse:
            lines.append(f"- 複用角度：{zh_tw(reuse)}")
        return "\n".join(lines)
    note = record.get("note_en") or "Kept after manual duplicate and originality review."
    return (
        f"- {LOCALE[lang]['notes_prefix']}: {note}\n"
        f"- Audit status: kept after manual duplicate and originality review."
    )


def media_notes(record: dict, lang: str) -> str:
    links = record.get("local_media", [])
    preview_label = {
        "en": "Video preview",
        "es": "Vista previa de video",
        "pt": "Prévia do vídeo",
        "ja": "動画プレビュー",
        "ko": "비디오 미리보기",
        "de": "Videovorschau",
        "fr": "Aperçu vidéo",
        "tr": "Video önizleme",
        "zh-CN": "视频预览",
        "zh-TW": "影片預覽",
        "ru": "Предпросмотр видео",
    }[lang]
    video_urls = [VIDEO_ATTACHMENT_BY_LOCAL_MEDIA[path] for path in links if path in VIDEO_ATTACHMENT_BY_LOCAL_MEDIA]
    case_url = VIDEO_ATTACHMENT_BY_CASE_LABEL.get(f"case{record['case']}")
    if case_url and case_url not in video_urls:
        video_urls.append(case_url)
    if not video_urls:
        return ""
    parts = []
    parts.append(f"- {preview_label}:")
    parts.append("")
    for url in video_urls:
        parts.append(url)
        parts.append("")
    return "\n".join(parts).rstrip()


def author_link(item: dict) -> str:
    username = item["author"]["username"]
    return f"https://x.com/{username}"


def curated_records(items: list[dict]) -> list[dict]:
    records = []
    for source_idx in SELECTED_SOURCE_INDICES:
        item = items[source_idx - 1]
        cat = CATEGORY_FOR_CASE[source_idx]
        records.append(
            {
                "case": CASE_LABEL_FOR_SOURCE_INDEX[source_idx],
                "source_index": source_idx,
                "id": item["id"],
                "url": item["url"],
                "author": f"@{item['author']['username']}",
                "author_url": author_link(item),
                "date": date_only(item["created_at_iso"]),
                "category": cat,
                "category_name": CATEGORY_META[cat][1],
                "title": EN_TITLES[source_idx],
                "title_zh": item.get("use_case_title_zh"),
                "evidence_type": TYPE_FOR_CATEGORY[cat],
                "quality_tier": item.get("tier"),
                "source_role": item.get("source_role"),
                "why_selected_zh": item.get("why_selected_zh"),
                "reuse_angle_zh": item.get("reuse_angle_zh"),
                "source_text": item.get("text"),
                "takeaway_en": EN_TAKEAWAYS[source_idx],
                "takeaway_zh": ZH_TAKEAWAYS[source_idx],
                "note_en": EN_NOTES[source_idx],
                "local_media": valid_media_links(MEDIA_BY_SOURCE_INDEX.get(source_idx, [])),
            }
        )
    records.extend(MANUAL_CASES)
    for record in records:
        record["category_name"] = CATEGORY_META[record["category"]][1]
    return sorted(records, key=lambda record: record["case"])


def video_source_records(records: list[dict]) -> list[dict]:
    media_to_case = {}
    public_case_labels = {record["case"] for record in records}
    for record in records:
        for rel in record.get("local_media", []):
            media_to_case[rel] = record["case"]
    out = []
    for label, attachment_url in VIDEO_SOURCE_ROWS:
        case_number = int(label.removeprefix("case"))
        local_media_candidate = f"media/{label}.mp4"
        local_media = local_media_candidate if (ROOT / local_media_candidate).exists() else None
        public_case = media_to_case.get(local_media_candidate)
        if public_case is None and case_number in public_case_labels:
            public_case = case_number
        if public_case == case_number:
            usage = "standalone_public_case" if local_media else "direct_preview_only"
        elif public_case is None:
            usage = "source_video_only"
        else:
            usage = "merged_or_deduplicated_media"
        out.append(
            {
                "case_label": label,
                "attachment_url": attachment_url,
                "local_media": local_media,
                "public_case": public_case,
                "usage": usage,
            }
        )
    return out


def render_badges(img_path: str) -> str:
    return f"""<div align="center">

<a href="{CTA_ANCHOR}"><img src="{img_path}" alt="Blender + Seedance usecase repository banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Use on EvoLink](https://img.shields.io/badge/Use_on-EvoLink-black)]({CTA_ANCHOR})
[![MCP + Skill](https://img.shields.io/badge/MCP_%2B_Skill-Pending-orange)]({CTA_ANCHOR})
[![Agent Workflow](https://img.shields.io/badge/Agent_Workflow-Pending-blue)]({CTA_ANCHOR})

{LANG_BADGES}

</div>"""


def render_intro(labels: dict) -> str:
    return f"""## 🍌 Introduction

{labels["intro"]}

**{labels["value"]}**

{labels["source"]}

{labels["cta"]}"""


def category_display(cat: str, lang: str) -> str:
    return CATEGORY_DISPLAY.get(lang, CATEGORY_DISPLAY["en"])[cat]


def render_overview(labels: dict, records: list[dict], lang: str) -> str:
    bullets = "\n".join(f"- {line.format(count=len(records))}" for line in OVERVIEW_LINES[lang])
    return f"""## 📊 Overview

{bullets}

> [!NOTE]
> {labels["overview_note"]}"""


def render_quick(labels: dict, lang: str) -> str:
    quick = QUICK_START[lang]
    return f"""<a id="quick-start"></a>
## ⚡ {quick["title"]}

{quick["intro"]}

### 1. {quick["mcp_title"]}

{quick["mcp_body"]}

- {quick["setup_label"]}: [Blender MCP setup](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

### 2. {quick["skill_title"]}

{quick["skill_body"]}

```bash
npm i evolink-seedance
npm i evolink-topaz-video-upscale
```

### 3. {quick["key_title"]}

{quick["key_body"]}

```bash
export EVOLINK_API_KEY="<your-evolink-api-key>"
```

### 4. {quick["run_title"]}

{quick["run_body"]}

```text
{quick["agent_prompt"]}
```

> [!NOTE]
> {quick["note"]}"""


def grouped_records(records: list[dict]) -> dict[str, list[dict]]:
    grouped = defaultdict(list)
    for record in records:
        grouped[record["category"]].append(record)
    return dict(grouped)


def case_labels_summary(recs: list[dict]) -> str:
    labels = [str(rec["case"]) for rec in recs]
    return "Case " + ", ".join(labels)


def render_menu(labels: dict, records: list[dict], lang: str) -> str:
    grouped = grouped_records(records)
    lines = [
        f"## 📑 {labels['menu']}",
        "",
        f"| {labels['section']} | {labels['cases']} |",
        "|---|---|",
    ]
    for cat, recs in grouped.items():
        emoji, name = CATEGORY_META[cat]
        display = category_display(cat, lang)
        lines.append(f"| [{emoji} {display}](#{slug(name)}) | {case_labels_summary(recs)} |")
    lines.append(f"| [🙏 {labels['ack']}](#acknowledge) | Credits and correction policy |")
    lines.append("")
    for cat, recs in grouped.items():
        emoji, name = CATEGORY_META[cat]
        display = category_display(cat, lang)
        lines.extend(
            [
                f'<a id="{slug(name)}"></a>',
                f"### {emoji} {display}",
                "",
                f"| {labels['case']} | {labels['what']} | {labels['type']} |",
                "|---|---|---|",
            ]
        )
        for rec in recs:
            title = record_title(rec, lang)
            lines.append(f"| [{title}](#case-{rec['case']}) | {record_takeaway(rec, lang).strip('*')} | {rec['evidence_type']} |")
        lines.append("")
    return "\n".join(lines).rstrip()


_SOURCE_ITEMS_CACHE = None


def source_items() -> list[dict]:
    global _SOURCE_ITEMS_CACHE
    if _SOURCE_ITEMS_CACHE is None:
        _SOURCE_ITEMS_CACHE = json.loads(SOURCE.read_text())["items"]
    return _SOURCE_ITEMS_CACHE


def render_cases(labels: dict, items: list[dict], lang: str) -> str:
    grouped = grouped_records(curated_records(items))
    chunks = []
    for cat, recs in grouped.items():
        emoji, name = CATEGORY_META[cat]
        display = category_display(cat, lang)
        chunks.append(f'<a id="{slug(name)}-cases"></a>')
        chunks.append(f"## {emoji} {display}")
        chunks.append("")
        for rec in recs:
            idx = rec["case"]
            title = record_title(rec, lang)
            chunks.extend(
                [
                    f'<a id="case-{idx}"></a>',
                    f"### Case {idx}: [{title}]({rec['url']}) (by [{rec['author']}]({rec['author_url']}))",
                    "",
                    f"**{record_takeaway(rec, lang)}**",
                    "",
                    record_notes(rec, lang),
                    media_notes(rec, lang),
                    "",
                    f"{labels['type']}: {rec['evidence_type']} | {labels['date']}: {rec['date']}",
                    "",
                    "---",
                    "",
                ]
            )
    return "\n".join(chunks).rstrip()


def render_ack(labels: dict, records: list[dict]) -> str:
    creators = []
    seen = set()
    for record in records:
        if record["author"] not in seen:
            seen.add(record["author"])
            creators.append(f"- [{record['author']}]({record['author_url']})")
    return f"""<a id="acknowledge"></a>
## 🙏 {labels["ack"]}

This repository was inspired by creators who publicly shared Blender + Seedance workflows, tests, prompts, reference videos, and production notes.

{chr(10).join(creators)}

*We cannot guarantee that every case is attributed to the original creator. If anything needs to be corrected, please contact us and we will update it.*

If you have more interesting usage cases to share, open an issue or pull request and help expand the EvoLink usecase library.

[![Star History Chart](https://api.star-history.com/svg?repos={OWNER}/{REPO}&type=Date)](https://www.star-history.com/#{OWNER}/{REPO}&Date)"""


def render_readme(lang: str, filename: str, img_path: str, items: list[dict], records: list[dict]) -> str:
    labels = LOCALE[lang]
    parts = [
        render_badges(img_path),
        render_intro(labels),
        render_overview(labels, records, lang),
        render_quick(labels, lang),
        render_menu(labels, records, lang),
        render_cases(labels, items, lang),
        render_ack(labels, records),
        "",
    ]
    return "\n\n".join(parts)


def render_curated_md(records: list[dict]) -> str:
    lines = [
        "# Blender + Seedance Curated Use Cases",
        "",
        f"Generated: {datetime.utcnow().replace(microsecond=0).isoformat()}Z",
        f"Cases: {len(records)}",
        "",
        "| Case | Title | Source | Author | Category | Type | Date |",
        "|---|---|---|---|---|---|---|",
    ]
    for record in records:
        lines.append(
            f"| {record['case']} | {record['title']} | [source]({record['url']}) | [{record['author']}]({record['author_url']}) | {record['category_name']} | {record['evidence_type']} | {record['date']} |"
        )
    lines.append("")
    return "\n".join(lines)


def write_banner(path: Path, lang_name: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if BANNER_SOURCE.exists():
        if path.resolve() == BANNER_SOURCE.resolve():
            return
        Image.open(BANNER_SOURCE).convert("RGB").save(path)
        return
    img = Image.new("RGB", (1520, 760), "#111827")
    draw = ImageDraw.Draw(img)
    for y in range(760):
        r = int(17 + y * 0.05)
        g = int(24 + y * 0.04)
        b = int(39 + y * 0.08)
        draw.line((0, y, 1520, y), fill=(r, g, b))
    draw.rectangle((86, 86, 1434, 674), outline="#38bdf8", width=4)
    draw.rectangle((116, 116, 1404, 644), outline="#f97316", width=2)
    try:
        font_big = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 78)
        font_mid = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
        font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 30)
    except Exception:
        font_big = font_mid = font_small = ImageFont.load_default()
    draw.text((150, 205), "Blender + Seedance", fill="#f8fafc", font=font_big)
    draw.text((154, 315), "Curated use cases for agent-guided video workflows", fill="#bae6fd", font=font_mid)
    draw.text((154, 395), f"{lang_name} edition · MCP · Skill · Agent workflow", fill="#fed7aa", font=font_small)
    draw.text((154, 505), "Previs · Viewport · FBX · Mixamo · ComfyUI · Blender MCP", fill="#e5e7eb", font=font_small)
    img.save(path)


def write_static_files(records: list[dict]) -> None:
    (ROOT / ".gitignore").write_text(
        "\n".join(
            [
                ".DS_Store",
                "__pycache__/",
                "*.pyc",
                ".env",
                ".env.*",
                "node_modules/",
                ".codex/",
                "data/x-search/raw/",
                "data/x-search/*/raw/",
                "",
            ]
        )
    )
    (ROOT / "LICENSE").write_text(
        textwrap.dedent(
            """\
            Creative Commons Attribution 4.0 International

            This repository contains curated summaries and links to public source posts.
            Source posts, images, videos, trademarks, and creator materials remain owned by their respective creators.

            You are free to share and adapt this curated repository content with attribution to EvoLink and the original source creators where applicable.
            """
        )
    )
    (ROOT / "CONTRIBUTING.md").write_text(
        textwrap.dedent(
            """\
            # Contributing

            Contributions should add source-backed Blender + Seedance cases only.

            Required metadata:

            - Original source URL
            - Creator handle and profile URL
            - Publication date when available
            - Evidence type: Demo, Tutorial, Evaluation, Integration, Benchmark, or Limit
            - A concise usage takeaway
            - Source-grounded notes without invented prompts or results

            Do not add raw private exports, unpublished media, or copied long post text.
            """
        )
    )
    (ROOT / "docs" / "maintenance.md").write_text(
        textwrap.dedent(
            f"""\
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

            - Selected public cases: {len(records)}
            - Owner-provided video rows: {len(VIDEO_SOURCE_ROWS)}
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
            - Direct GitHub attachment video URLs when the owner-provided video map exposes playable previews
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
            """
        )
    )
    (ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md").write_text(
        textwrap.dedent(
            """\
            ## Source-backed case checklist

            - [ ] Original source URL is included.
            - [ ] Creator profile is included.
            - [ ] Date is present or explicitly unavailable.
            - [ ] Evidence type is one of Demo, Tutorial, Evaluation, Integration, Benchmark, or Limit.
            - [ ] No prompt, result, benchmark, price, or API claim is invented.

            ## Localization checklist

            - [ ] All 11 README files keep the same case count.
            - [ ] All case anchors remain `#case-x`.
            - [ ] Source URLs and creator URLs match the English source.

            ## Validation

            - [ ] `python3 scripts/verify_repo.py`
            - [ ] `git diff --check`
            """
        )
    )


def write_verify_script(records: list[dict]) -> None:
    script = f'''#!/usr/bin/env python3
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FILES = {[filename for _, filename, _, _ in LANGS]!r}
EXPECTED_CASES = {len(records)}
EXPECTED_IMAGES = {sorted({img for _, _, _, img in LANGS})!r}
EXPECTED_VIDEO_LABELS = {[label for label, _ in VIDEO_SOURCE_ROWS]!r}

def fail(msg):
    raise SystemExit(f"FAIL: {{msg}}")

curated = json.loads((ROOT / "blender-seedance-usecase-curated.json").read_text())
if curated["metadata"].get("selected_count") != EXPECTED_CASES:
    fail("curated selected_count does not match README case count")
expected_labels = [str(item["case"]) for item in curated["items"]]
expected_label_set = set(expected_labels)

for file in FILES:
    p = ROOT / file
    if not p.exists():
        fail(f"missing {{file}}")
    text = p.read_text()
    anchors = re.findall(r'^<a id="case-([0-9]+)"></a>', text, re.M)
    heads = re.findall(r'^### Case ([0-9]+): \\[', text, re.M)
    if len(anchors) != EXPECTED_CASES:
        fail(f"{{file}} has {{len(anchors)}} anchors, expected {{EXPECTED_CASES}}")
    if anchors != heads:
        fail(f"{{file}} anchors and case headings differ")
    if len(set(anchors)) != len(anchors):
        fail(f"{{file}} contains duplicate case anchors")
    if set(anchors) != expected_label_set:
        fail(f"{{file}} anchors do not match curated case labels")
    if "## 📊" not in text or "## ⚡" not in text or "## 📑" not in text or "## 🙏" not in text:
        fail(f"{{file}} missing required usecase sections")
    if text.count("| Date: ") + text.count("| Fecha: ") + text.count("| Data: ") + text.count("| Datum: ") + text.count("| Tarih: ") + text.count("| 日期: ") + text.count("| Дата: ") < EXPECTED_CASES:
        fail(f"{{file}} missing Type/Date metadata lines")

for img in EXPECTED_IMAGES:
    if not (ROOT / img).exists():
        fail(f"missing {{img}}")

for required in ["LICENSE", "CONTRIBUTING.md", "docs/maintenance.md", ".github/PULL_REQUEST_TEMPLATE.md", "blender-seedance-usecase-curated.json", "blender-seedance-usecase-curated.md", "data/usecase-video-sources.json", "images/banner.png"]:
    if not (ROOT / required).exists():
        fail(f"missing {{required}}")

video_sources = json.loads((ROOT / "data" / "usecase-video-sources.json").read_text())
if video_sources["metadata"].get("source_rows") != len(EXPECTED_VIDEO_LABELS):
    fail("video source row count does not match expected workbook rows")
video_labels = [row["case_label"] for row in video_sources["items"]]
if video_labels != EXPECTED_VIDEO_LABELS:
    fail("video source labels do not match expected workbook order")
if len(set(video_labels)) != len(video_labels):
    fail("video source labels contain duplicates")
for row in video_sources["items"]:
    rel = row.get("local_media")
    if rel is not None and not (ROOT / rel).exists():
        fail(f"missing video source local media {{rel}}")
    if not row.get("attachment_url", "").startswith("https://github.com/user-attachments/assets/"):
        fail(f"unexpected attachment URL for {{row.get('case_label')}}")

media_paths = []
for item in curated["items"]:
    for rel in item.get("local_media", []):
        media_paths.append(rel)
        if not (ROOT / rel).exists():
            fail(f"missing local media {{rel}}")

for file in FILES:
    text = (ROOT / file).read_text()
    for row in video_sources["items"]:
        if row["attachment_url"] not in text:
            fail(f"{{file}} missing direct video attachment URL {{row['case_label']}}")

print(f"PASS: {{len(FILES)}} README files, {{EXPECTED_CASES}} cases each, {{len(media_paths)}} media files linked, {{len(video_sources['items'])}} direct video URLs embedded")
'''
    path = ROOT / "scripts" / "verify_repo.py"
    path.write_text(script)
    path.chmod(0o755)


def main() -> None:
    data = json.loads(SOURCE.read_text())
    items = data["items"]
    records = curated_records(items)
    video_records = video_source_records(records)
    for _, _, lang_name, img in LANGS:
        write_banner(ROOT / img, lang_name)
    for lang, filename, _, img in LANGS:
        (ROOT / filename).write_text(render_readme(lang, filename, img, items, records))
    curated = {
        "metadata": {
            "generated_at": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
            "source": str(SOURCE.relative_to(ROOT)),
            "repo": REPO,
            "selected_count": len(records),
            "tier_counts": dict(Counter(record["quality_tier"] for record in records)),
            "category_counts": dict(Counter(record["category"] for record in records)),
            "cta_status": "quick-start workflow published; final landing page still pending",
            "publication_status": "existing target repository; push to cheercheung/Awesome-Blender-Seedance-Workflow-Usecases approved after local verification; no new repository creation approved",
            "audit": "docs/usecase-originality-audit.md",
            "video_source_map": "data/usecase-video-sources.json",
        },
        "items": records,
    }
    (ROOT / "blender-seedance-usecase-curated.json").write_text(json.dumps(curated, ensure_ascii=False, indent=2) + "\n")
    video_sources = {
        "metadata": {
            "generated_at": curated["metadata"]["generated_at"],
            "source_workbook": "Book1.xlsx",
            "source_rows": len(video_records),
            "localization_policy": "README files render owner-provided GitHub attachment URLs as direct video previews and keep repository-local media files as backups.",
        },
        "items": video_records,
    }
    (ROOT / "data" / "usecase-video-sources.json").write_text(json.dumps(video_sources, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "blender-seedance-usecase-curated.md").write_text(render_curated_md(records))
    write_static_files(records)
    write_verify_script(records)


if __name__ == "__main__":
    main()
