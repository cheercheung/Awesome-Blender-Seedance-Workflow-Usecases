#!/usr/bin/env python3
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FILES = ['README.md', 'README_es.md', 'README_pt.md', 'README_ja.md', 'README_ko.md', 'README_de.md', 'README_fr.md', 'README_tr.md', 'README_zh-TW.md', 'README_zh-CN.md', 'README_ru.md']
EXPECTED_CASES = 25
EXPECTED_IMAGES = ['images/banner.png']
EXPECTED_VIDEO_LABELS = ['case1', 'case2', 'case3', 'case4', 'case5', 'case6', 'case8', 'case9', 'case10', 'case11', 'case13', 'case14', 'case15', 'case16', 'case17', 'case18', 'case19', 'case20', 'case21', 'case22', 'case23', 'case24', 'case25', 'case26', 'case27', 'case28']

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
    if ".github/ISSUE_TEMPLATE/use-case.yml" not in text or ".github/PULL_REQUEST_TEMPLATE.md" not in text:
        fail(f"{file} missing issue or PR template links")

for img in EXPECTED_IMAGES:
    if not (ROOT / img).exists():
        fail(f"missing {img}")

for required in ["LICENSE", "CONTRIBUTING.md", "docs/maintenance.md", ".github/PULL_REQUEST_TEMPLATE.md", ".github/ISSUE_TEMPLATE/config.yml", ".github/ISSUE_TEMPLATE/use-case.yml", "blender-seedance-usecase-curated.json", "data/usecase-video-sources.json", "images/banner.png"]:
    if not (ROOT / required).exists():
        fail(f"missing {required}")

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
        fail(f"missing video source local media {rel}")
    if not row.get("attachment_url", "").startswith("https://github.com/user-attachments/assets/"):
        fail(f"unexpected attachment URL for {row.get('case_label')}")

media_paths = []
for item in curated["items"]:
    for rel in item.get("local_media", []):
        media_paths.append(rel)
        if not (ROOT / rel).exists():
            fail(f"missing local media {rel}")

for file in FILES:
    text = (ROOT / file).read_text()
    for row in video_sources["items"]:
        if row["attachment_url"] not in text:
            fail(f"{file} missing direct video attachment URL {row['case_label']}")

print(f"PASS: {len(FILES)} README files, {EXPECTED_CASES} cases each, {len(media_paths)} media files linked, {len(video_sources['items'])} direct video URLs embedded")
