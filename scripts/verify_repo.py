#!/usr/bin/env python3
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FILES = ['README.md', 'README_es.md', 'README_pt.md', 'README_ja.md', 'README_ko.md', 'README_de.md', 'README_fr.md', 'README_tr.md', 'README_zh-TW.md', 'README_zh-CN.md', 'README_ru.md']
EXPECTED_CASES = 25
EXPECTED_IMAGES = ['images/en.png', 'images/es.png', 'images/pt.png', 'images/ja.png', 'images/ko.png', 'images/de.png', 'images/fr.png', 'images/tr.png', 'images/zh-tw.png', 'images/zh.png', 'images/ru.png']

def fail(msg):
    raise SystemExit(f"FAIL: {msg}")

curated = json.loads((ROOT / "blender-seedance-usecase-curated.json").read_text())
if curated["metadata"].get("selected_count") != EXPECTED_CASES:
    fail("curated selected_count does not match README case count")
expected_labels = [str(item["case"]) for item in curated["items"]]
expected_label_set = set(expected_labels)

for file in FILES:
    p = ROOT / file
    if not p.exists():
        fail(f"missing {file}")
    text = p.read_text()
    anchors = re.findall(r'^<a id="case-([0-9]+)"></a>', text, re.M)
    heads = re.findall(r'^### Case ([0-9]+): \[', text, re.M)
    if len(anchors) != EXPECTED_CASES:
        fail(f"{file} has {len(anchors)} anchors, expected {EXPECTED_CASES}")
    if anchors != heads:
        fail(f"{file} anchors and case headings differ")
    if len(set(anchors)) != len(anchors):
        fail(f"{file} contains duplicate case anchors")
    if set(anchors) != expected_label_set:
        fail(f"{file} anchors do not match curated case labels")
    if "## 📊" not in text or "## ⚡" not in text or "## 📑" not in text or "## 🙏" not in text:
        fail(f"{file} missing required usecase sections")
    if text.count("| Date: ") + text.count("| Fecha: ") + text.count("| Data: ") + text.count("| Datum: ") + text.count("| Tarih: ") + text.count("| 日期: ") + text.count("| Дата: ") < EXPECTED_CASES:
        fail(f"{file} missing Type/Date metadata lines")

for img in EXPECTED_IMAGES:
    if not (ROOT / img).exists():
        fail(f"missing {img}")

for required in ["LICENSE", "CONTRIBUTING.md", "docs/maintenance.md", ".github/PULL_REQUEST_TEMPLATE.md", "blender-seedance-usecase-curated.json", "blender-seedance-usecase-curated.md"]:
    if not (ROOT / required).exists():
        fail(f"missing {required}")

media_paths = []
for item in curated["items"]:
    for rel in item.get("local_media", []):
        media_paths.append(rel)
        if not (ROOT / rel).exists():
            fail(f"missing local media {rel}")

for file in FILES:
    text = (ROOT / file).read_text()
    for rel in media_paths:
        if rel not in text:
            fail(f"{file} missing local media link {rel}")

print(f"PASS: {len(FILES)} README files, {EXPECTED_CASES} cases each, {len(media_paths)} media files linked")
