#!/usr/bin/env python3
"""Structural checks only; not factual, archival-completeness or model validation."""
from __future__ import annotations
import argparse
import csv
import io
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
V3 = Path('docs/spatial-world-model-white-paper/v3.0')
FROZEN = ('docs/camera-aware-video-generation/research-report/v1.0',
          'docs/spatial-world-model-white-paper/v1.0',
          'docs/spatial-world-model-white-paper/v2.0')
EXPECTED_SOURCES = {f'R{i:02}' for i in range(1, 37)} | {f'N{i:02}' for i in range(1, 36)}

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)

def source_ids(text: str) -> set[str]:
    ids = re.findall(r'^\| ([RN]\d{2}) \|', text, re.M)
    require(len(ids) == len(set(ids)), 'Duplicate source identifiers')
    require(set(ids) == EXPECTED_SOURCES, 'Expected exactly R01-R36 and N01-N35')
    return set(ids)

def check_sections(text: str) -> None:
    sections = [int(x) for x in re.findall(r'^## (\d+)\.', text, re.M)]
    require(sections == list(range(1, 15)), 'Expected ordered main sections 1-14')

def check_references(text: str, ids: set[str]) -> None:
    unknown = set(re.findall(r'\b[RN]\d{2}\b', text)) - ids
    require(not unknown, f'Unknown references: {sorted(unknown)}')

def check_links(path: Path, root: Path) -> None:
    text = path.read_text(encoding='utf-8')
    for target in re.findall(r'!?\[[^\]\n]+\]\(([^\s)]+)\)', text):
        parsed = urlsplit(target)
        if parsed.scheme:
            require(parsed.scheme in ('https', 'http', 'mailto'), f'Unsupported link: {target}')
            continue
        if not parsed.path:
            continue
        dest = (path.parent / unquote(parsed.path)).resolve()
        require(dest.is_relative_to(root.resolve()), f'Link escapes repository: {target}')
        require(dest.exists(), f'Broken local link in {path}: {target}')

def check_dispositions(text: str) -> None:
    rows = list(csv.DictReader(io.StringIO(text)))
    require(len(rows) == 38, 'Expected 38 audit rows')
    require({r['audit_id'] for r in rows} == {f'A{i:02}' for i in range(1, 39)}, 'Audit ID coverage')
    for row in rows:
        require(bool(row['editorial_disposition']) and bool(row['remaining_validation']), 'Missing disposition or caveat')
        require(all(1 <= int(s) <= 14 for s in row['sections'].split(';')), 'Invalid section mapping')

def check_release(card: dict) -> None:
    require(card['model_execution_status'] == 'not_run', 'Template must not claim execution')
    require(all(card['evaluation'][k] == 'not_run' for k in ('E0','E1','E2','E3')), 'Template must not claim passed gates')
    for key in ('peak_device_gib', 'time_to_first_usable_preview_s', 'end_to_end_s'):
        require(card['runtime'][key] is None, 'Template contains unmeasured runtime value')

def check_frozen(root: Path, base: str) -> None:
    def git(*args: str) -> bytes:
        return subprocess.check_output(['git', *args], cwd=root)
    previous = git('ls-tree', '-r', '--full-tree', base, '--', *FROZEN)
    current = git('ls-tree', '-r', '--full-tree', 'HEAD', '--', *FROZEN)
    require(bool(previous), 'Frozen baseline missing or empty')
    require(previous == current, 'Frozen repository content differs from baseline')
    require(not git('diff', '--name-only', 'HEAD', '--', *FROZEN).strip(), 'Frozen worktree modified')
    require(not git('ls-files', '--others', '--exclude-standard', '--', *FROZEN).strip(), 'Untracked files under frozen paths')

def validate(root: Path, base: str) -> dict:
    directory = root / V3
    manifest = json.loads((directory / 'VERSION_MANIFEST.json').read_text())
    require(manifest['version'] == '3.0', 'Wrong version')
    require(manifest['model_benchmarks_reproduced'] is False, 'Empirical scope changed')
    require(manifest['original_v2_byte_import_complete'] is False, 'Archive status requires explicit separate verification')
    require(base == manifest['base_commit'], 'Baseline differs from recorded freeze')
    ids = source_ids((directory / 'SOURCE_REGISTRY.md').read_text())
    for lang in ('en', 'zh-CN'):
        text = (directory / lang / 'WHITE_PAPER.md').read_text(encoding='utf-8')
        check_sections(text)
        check_references(text, ids)
    for path in directory.rglob('*.md'):
        text = path.read_text(encoding='utf-8')
        require(text.endswith('\n'), f'Missing final newline: {path}')
        require('\ufffd' not in text and '\ue200' not in text, f'Bad text or UI citation token: {path}')
        check_links(path, root)
    check_dispositions((directory / 'AUDIT_DISPOSITIONS.csv').read_text())
    check_release(json.loads((directory / 'RELEASE_CARD_TEMPLATE.json').read_text()))
    check_frozen(root, base)
    return {'structural_validation': 'passed', 'languages': 2, 'main_sections_each': 14,
            'source_ids': len(ids), 'audit_dispositions': 38, 'frozen_paths': 'unchanged',
            'model_benchmarks': 'not_run', 'original_byte_import': 'pending',
            'rendered_publication_qa': 'not_run'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', required=True)
    args = parser.parse_args()
    print(json.dumps(validate(ROOT, args.base), ensure_ascii=False, indent=2))
