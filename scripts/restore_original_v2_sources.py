#!/usr/bin/env python3
"""Verify original v2 attachments; optionally preserve exact bytes outside frozen paths."""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'original_v2_EN.md': '263c31369b11ac8bfadc9b7c7c47d229404e94e5db896b222b247eb683dbf530',
    'original_v2_CN.md': '18863b6004b48938d67e256a217d2a5b7d194858cb400c7fcde5977650f69089',
}

def verify(en: Path, zh: Path) -> dict[str, bytes]:
    data = {'original_v2_EN.md': en.read_bytes(), 'original_v2_CN.md': zh.read_bytes()}
    for name, content in data.items():
        if hashlib.sha256(content).hexdigest() != EXPECTED[name]:
            raise ValueError(f'Original source hash mismatch: {name}; nothing written')
    return data

def preserve(data: dict[str, bytes], destination: Path) -> None:
    if set(data) != set(EXPECTED):
        raise ValueError('Both original sources are required')
    for name, content in data.items():
        if hashlib.sha256(content).hexdigest() != EXPECTED[name]:
            raise ValueError(f'Hash mismatch: {name}')
    if destination.is_symlink():
        raise ValueError('Archive destination cannot be a symlink')
    for name, content in data.items():
        target = destination / name
        if target.is_symlink() or (target.exists() and target.read_bytes() != content):
            raise ValueError(f'Refusing to overwrite different archive: {target}')
    destination.mkdir(parents=True, exist_ok=True)
    for name, content in data.items():
        target = destination / name
        if not target.exists():
            with target.open('xb') as handle:
                handle.write(content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--en', type=Path, required=True)
    parser.add_argument('--zh', type=Path, required=True)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    verified = verify(args.en, args.zh)
    if args.write:
        preserve(verified, ROOT / 'archives/conversation-v2.0')
        print('Preserved exact original bytes in archives/conversation-v2.0; commit and verify remotely separately.')
    else:
        print('Both original source hashes match. Dry run: no files written.')
