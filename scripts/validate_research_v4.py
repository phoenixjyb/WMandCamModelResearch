#!/usr/bin/env python3
"""Validate v4 research-source structure, records and frozen-version integrity.

This is not a fact checker, model benchmark, licensing check, translation
certification or rendered-publication quality check. Uses only the stdlib.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import subprocess
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REL = Path('docs/spatial-world-model-white-paper/v4.0')
BASE = 'ac2fbf5e354e439e0a31a9e425f433dcdc360555'
EXPECTED_SOURCES = {f'P{i:02d}' for i in range(1, 39)}
EXPECTED_RESULTS = ({f'D{i:02d}' for i in range(1, 11)} |
                    {f'S{i:02d}' for i in range(1, 5)} |
                    {f'H{i:02d}' for i in range(1, 7)})
FROZEN = [
    'docs/camera-aware-video-generation/research-report/v1.0/',
    'docs/spatial-world-model-white-paper/v1.0/',
    'docs/spatial-world-model-white-paper/v2.0/',
    'docs/spatial-world-model-white-paper/v3.0/',
]
REQUIRED = [
    'README.md', 'en/WHITE_PAPER.md', 'zh-CN/WHITE_PAPER.md',
    'slides/DECK_EN.md', 'slides/DECK_CN.md', 'SOURCE_REGISTRY.csv',
    'LITERATURE_COVERAGE.csv', 'RESULTS.csv', 'ATLAS_COMPARISON.md',
    'EXPERIMENTS.md', 'ARCHITECTURE.md', 'ROADMAP.md', 'REVIEW_METHOD.md',
    'OPEN_EVIDENCE_GAPS.csv', 'RECONCILIATION.md', 'VERSION_MANIFEST.json',
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding='utf-8-sig', newline='') as handle:
        rows = list(csv.DictReader(handle))
    require(bool(rows), f'Empty CSV: {path}')
    require(all(None not in row and all(v is not None for v in row.values())
                for row in rows), f'Malformed CSV: {path}')
    return rows


def check_numbering(text: str, expected: int, slide: bool = False) -> None:
    pattern = r'^# Slide (\d{2})\s' if slide else r'^## (\d+)\.'
    numbers = [int(n) for n in re.findall(pattern, text, flags=re.M)]
    require(numbers == list(range(1, expected + 1)),
            f'Incorrect {"slide" if slide else "section"} numbering: {numbers}')


def check_citations(text: str, known: set[str]) -> None:
    found = set(re.findall(r'\bP\d{2}\b', text))
    for first, last in re.findall(r'\bP(\d{2})[–-]P(\d{2})\b', text):
        require(int(first) <= int(last), 'Reversed source range')
        found.update(f'P{i:02d}' for i in range(int(first), int(last) + 1))
    require(found <= known, f'Unknown source IDs: {sorted(found - known)}')


def check_sources(rows: list[dict[str, str]]) -> set[str]:
    ids = [r['id'] for r in rows]
    require(len(ids) == len(set(ids)), 'Duplicate source ID')
    require(set(ids) == EXPECTED_SOURCES, 'Unexpected active source set')
    for row in rows:
        require(row['reproduced'] == 'false', 'Unsupported reproduction status')
        require(row['review_scope'].strip() != '', 'Missing review scope')
        require(row['qualification'].strip() != '', 'Missing source qualification')
        url = urlsplit(row['url'])
        require(url.scheme == 'https' and bool(url.netloc), 'Invalid source URL')
        require(date.fromisoformat(row['checked_on']) <= date(2026, 9, 6),
                'Source date exceeds evidence cut-off')
    return set(ids)


def check_results(rows: list[dict[str, str]], known: set[str]) -> None:
    ids = [r['result_id'] for r in rows]
    require(len(ids) == len(set(ids)), 'Duplicate result ID')
    require(set(ids) == EXPECTED_RESULTS, 'Unexpected result-row set')
    groups: dict[str, tuple[str, ...]] = {}
    for row in rows:
        require(row['source_id'] in known, 'Unknown result source')
        require(row['source_id'] in {'P05', 'P07', 'P08'},
                'Unregistered numerical protocol; update evidence specification')
        value = float(row['value'])
        require(math.isfinite(value) and value >= 0, 'Invalid numerical value')
        require(row['reproduced'] == 'false', 'Literature row is not our reproduction')
        require(row['direction'] in {'higher', 'lower'}, 'Invalid metric direction')
        for key in ('unit', 'input_regime', 'alignment', 'caveat', 'locator'):
            require(bool(row[key].strip()), f'Missing result field: {key}')
        signature = tuple(row[k] for k in
                          ('source_id', 'locator', 'dataset', 'metric', 'unit', 'direction'))
        group = row['comparison_group']
        if group in groups:
            require(groups[group] == signature, f'Incompatible group: {group}')
        groups[group] = signature
        if row['unit'] == 'source_native':
            require(row['alignment'] == 'not_fully_resolved_here',
                    'Source-native excerpt requires unresolved-protocol qualification')


def check_coverage(rows: list[dict[str, str]], known: set[str]) -> None:
    require(len(rows) >= 25, 'Coverage ledger unexpectedly truncated')
    for row in rows:
        ids = set(row['source_ids'].split())
        require(ids <= known | {'INHERITED_V3'}, 'Unknown coverage source')
        require(bool(row['review_depth']) and bool(row['next_evidence']),
                'Coverage without depth or remaining evidence')
    named = {r['work'] for r in rows}
    require({'Pi3X posed', 'Pi3', 'VGGT-Omega 1B', 'Depth Anything 3',
             'MapAnything'} <= named, 'Missing Atlas reconstruction comparator')


def check_links(text: str, source: Path, root: Path) -> None:
    root = root.resolve()
    for target in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', text):
        target = target.strip()
        parsed = urlsplit(target)
        if parsed.scheme:
            require(parsed.scheme == 'https' and bool(parsed.netloc),
                    f'Unsupported link: {target}')
            continue
        require(not parsed.netloc, f'Protocol-relative link: {target}')
        if not parsed.path:
            continue
        resolved = (source.parent / unquote(parsed.path)).resolve()
        require(resolved.is_relative_to(root), f'Link escapes repository: {target}')
        require(resolved.exists(), f'Missing local link in {source.name}: {target}')


def check_manifest(manifest: dict) -> None:
    require(manifest['version'] == '4.0', 'Wrong version')
    require(manifest['main_sections_each'] == 18, 'Wrong section count')
    require(manifest['slides_each'] == 24, 'Wrong slide count')
    require(manifest['active_source_records'] == 38, 'Wrong active source count')
    require(manifest['literature_result_rows'] == 20, 'Wrong result count')
    require(manifest['source_counts_overlap'] is True, 'Source counts must not be summed')
    require(manifest['predecessor_commit'] == BASE, 'Wrong predecessor')
    require(manifest['frozen_prefixes'] == FROZEN, 'Frozen scope changed')
    for key in ('model_benchmarks', 'robot_benchmarks', 'rendered_publication_qa'):
        require(manifest[key] == 'not_run', f'Unsupported completion: {key}')
    for key in ('atlas_graphical_numeric_transcription', 'original_v2_byte_import'):
        require(manifest[key] == 'pending', f'Unsupported closure: {key}')
    require(manifest['tracks'] == ['native_spatial_foundation_research',
                                   'recomo_embodiment'], 'Dual-track scope changed')


def ensure_frozen(changes: str) -> None:
    require(not changes.strip(), f'Frozen directory changes detected:\n{changes}')


def validate(root: Path = ROOT, base: str = BASE, check_git: bool = True) -> dict:
    root = root.resolve()
    folder = root / REL
    for relative in REQUIRED:
        path = folder / relative
        require(path.is_file() and path.stat().st_size > 0, f'Missing file: {path}')
    manifest = json.loads((folder / 'VERSION_MANIFEST.json').read_text(encoding='utf-8'))
    check_manifest(manifest)
    sources = read_csv(folder / 'SOURCE_REGISTRY.csv')
    known = check_sources(sources)
    results = read_csv(folder / 'RESULTS.csv')
    check_results(results, known)
    coverage = read_csv(folder / 'LITERATURE_COVERAGE.csv')
    check_coverage(coverage, known)
    gaps = read_csv(folder / 'OPEN_EVIDENCE_GAPS.csv')
    require(len({r['gap_id'] for r in gaps}) == len(gaps) == 12, 'Gap ledger mismatch')
    for language in ('en', 'zh-CN'):
        text = (folder / language / 'WHITE_PAPER.md').read_text(encoding='utf-8')
        check_numbering(text, 18)
        require(len(text) > 10000, 'Paper unexpectedly truncated')
    for name in ('DECK_EN.md', 'DECK_CN.md'):
        check_numbering((folder / 'slides' / name).read_text(encoding='utf-8'), 24, slide=True)
    for path in folder.rglob('*.md'):
        text = path.read_text(encoding='utf-8')
        check_citations(text, known)
        check_links(text, path, root)
    for name in ('README.md', 'CHANGELOG_v4.0.md'):
        path = root / name
        check_links(path.read_text(encoding='utf-8'), path, root)
    for experiment in manifest['experiments']:
        text = (folder / 'EXPERIMENTS.md').read_text(encoding='utf-8')
        require(re.search(r'^## \d+\. ' + re.escape(experiment) + r'\b', text, re.M)
                is not None, f'Missing experiment: {experiment}')
    if check_git:
        subprocess.run(['git', 'rev-parse', '--verify', base + '^{commit}'], cwd=root,
                       check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        changes = subprocess.check_output(
            ['git', 'diff', '--name-status', base, 'HEAD', '--', *FROZEN],
            cwd=root, text=True)
        ensure_frozen(changes)
    hashes = {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
              for path in sorted(folder.rglob('*')) if path.is_file()}
    return {
        'structural_validation': 'passed', 'version': '4.0', 'languages': 2,
        'main_sections_each': 18, 'slides_each': 24, 'active_source_records': len(sources),
        'literature_result_rows': len(results), 'coverage_rows': len(coverage),
        'frozen_paths': 'unchanged' if check_git else 'not_checked_in_unit_test',
        'frozen_comparison_base': base, 'model_benchmarks': 'not_run',
        'robot_benchmarks': 'not_run', 'rendered_publication_qa': 'not_run',
        'original_v2_byte_import': 'pending', 'source_sha256': hashes,
        'scope': 'Structure and provenance boundaries only; not scientific certification',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', default=BASE)
    args = parser.parse_args()
    print(json.dumps(validate(base=args.base), indent=2, ensure_ascii=False))
