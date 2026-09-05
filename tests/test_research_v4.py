"""Positive and negative controls for documentation validation, not model tests."""
from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import validate_research_v4 as v4


class V4ValidationTests(unittest.TestCase):
    def setUp(self):
        self.folder = ROOT / v4.REL
        self.sources = v4.read_csv(self.folder / 'SOURCE_REGISTRY.csv')
        self.results = v4.read_csv(self.folder / 'RESULTS.csv')
        self.manifest = json.loads((self.folder / 'VERSION_MANIFEST.json').read_text())

    def test_complete_source_stack(self):
        result = v4.validate(ROOT, check_git=False)
        self.assertEqual(result['literature_result_rows'], 20)
        self.assertEqual(result['active_source_records'], 38)

    def test_missing_section_rejected(self):
        with self.assertRaises(ValueError):
            v4.check_numbering('## 1. First\n## 3. Third', 3)

    def test_duplicate_slide_rejected(self):
        with self.assertRaises(ValueError):
            v4.check_numbering('# Slide 01 A\n# Slide 01 B', 2, slide=True)

    def test_citation_range(self):
        v4.check_citations('[P01–P05,P38]', v4.EXPECTED_SOURCES)
        with self.assertRaises(ValueError):
            v4.check_citations('[P38–P40]', v4.EXPECTED_SOURCES)

    def test_unknown_citation_rejected(self):
        with self.assertRaises(ValueError):
            v4.check_citations('Evidence [P99]', v4.EXPECTED_SOURCES)

    def test_duplicate_source_rejected(self):
        with self.assertRaises(ValueError):
            v4.check_sources(self.sources + [copy.deepcopy(self.sources[0])])

    def test_invented_reproduction_rejected(self):
        self.sources[0]['reproduced'] = 'true'
        with self.assertRaises(ValueError):
            v4.check_sources(self.sources)

    def test_nan_result_rejected(self):
        self.results[0]['value'] = 'nan'
        with self.assertRaises(ValueError):
            v4.check_results(self.results, v4.EXPECTED_SOURCES)

    def test_result_caveat_required(self):
        self.results[0]['caveat'] = ''
        with self.assertRaises(ValueError):
            v4.check_results(self.results, v4.EXPECTED_SOURCES)

    def test_incompatible_units_rejected(self):
        self.results[1]['unit'] = 'metres'
        with self.assertRaises(ValueError):
            v4.check_results(self.results, v4.EXPECTED_SOURCES)

    def test_atlas_numeric_invention_rejected(self):
        self.results[0]['source_id'] = 'P01'
        with self.assertRaises(ValueError):
            v4.check_results(self.results, v4.EXPECTED_SOURCES)

    def test_false_completion_rejected(self):
        self.manifest['model_benchmarks'] = 'passed'
        with self.assertRaises(ValueError):
            v4.check_manifest(self.manifest)

    def test_source_count_conflation_rejected(self):
        self.manifest['source_counts_overlap'] = False
        with self.assertRaises(ValueError):
            v4.check_manifest(self.manifest)

    def test_unknown_coverage_source_rejected(self):
        rows = v4.read_csv(self.folder / 'LITERATURE_COVERAGE.csv')
        rows[0]['source_ids'] = 'P99'
        with self.assertRaises(ValueError):
            v4.check_coverage(rows, v4.EXPECTED_SOURCES)

    def test_links_validated(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / 'page.md'
            (root / 'target.md').write_text('target')
            v4.check_links('[OK](target.md) [web](https://example.org)', page, root)
            for bad in ('[bad](missing.md)', '[bad](../escape.md)',
                        '[bad](sandbox:/mnt/data/x)', '[bad](//example.org/x)'):
                with self.subTest(bad=bad), self.assertRaises(ValueError):
                    v4.check_links(bad, page, root)

    def test_frozen_diff_rejected(self):
        v4.ensure_frozen('')
        with self.assertRaises(ValueError):
            v4.ensure_frozen('M\tdocs/spatial-world-model-white-paper/v2.0/en/x.md\n')

    def test_multibyte_size_is_not_english_character_count(self):
        v4.check_paper_size('文' * 4000)
        v4.check_paper_size('a' * 11000)
        with self.assertRaises(ValueError):
            v4.check_paper_size('文' * 100)


if __name__ == '__main__':
    unittest.main()
