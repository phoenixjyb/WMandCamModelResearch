from __future__ import annotations
import csv
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate_research_v3 import EXPECTED_SOURCES, source_ids, check_sections, check_references, check_links, check_dispositions, check_release
from restore_original_v2_sources import verify

class ResearchValidationTests(unittest.TestCase):
    def test_all_sources(self):
        text = '\n'.join(f'| {i} | entry | Paper |' for i in sorted(EXPECTED_SOURCES))
        self.assertEqual(source_ids(text), EXPECTED_SOURCES)

    def test_duplicate_source_rejected(self):
        text = '\n'.join(f'| {i} | entry | Paper |' for i in sorted(EXPECTED_SOURCES))
        with self.assertRaises(ValueError): source_ids(text + '\n| R01 | duplicate | Paper |')

    def test_sections_match(self):
        check_sections('\n'.join(f'## {i}. Title' for i in range(1, 15)))

    def test_missing_section_rejected(self):
        with self.assertRaises(ValueError): check_sections('## 1. Only one')

    def test_reference_identity(self):
        check_references('See [R01, N35].', EXPECTED_SOURCES)
        with self.assertRaises(ValueError): check_references('See [N99].', EXPECTED_SOURCES)

    def test_local_and_external_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root/'target.md').write_text('ok\n')
            doc = root/'source.md'; doc.write_text('[valid](target.md) [web](https://example.org/)\n')
            check_links(doc, root)
            doc.write_text('[missing](not-here.md)\n')
            with self.assertRaises(ValueError): check_links(doc, root)

    def test_sandbox_and_escape_links_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); doc = root/'source.md'
            for text in ('[bad](sandbox:/mnt/data/x.md)', '[bad](../x.md)'):
                doc.write_text(text)
                with self.assertRaises(ValueError): check_links(doc, root)

    def test_disposition_coverage(self):
        buffer = io.StringIO(); writer = csv.writer(buffer)
        writer.writerow(['audit_id','editorial_disposition','sections','remaining_validation'])
        for i in range(1,39): writer.writerow([f'A{i:02}','revised','1;14','not_run'])
        check_dispositions(buffer.getvalue())
        with self.assertRaises(ValueError): check_dispositions(buffer.getvalue().rsplit('\n',2)[0])

    def test_release_does_not_invent_measurements(self):
        card = {'model_execution_status':'not_run','evaluation':{k:'not_run' for k in ('E0','E1','E2','E3')},
                'runtime':{k:None for k in ('peak_device_gib','time_to_first_usable_preview_s','end_to_end_s')}}
        check_release(card); card['runtime']['peak_device_gib'] = 24
        with self.assertRaises(ValueError): check_release(card)

    def test_wrong_originals_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'fake.md'; p.write_text('not an original')
            with self.assertRaises(ValueError): verify(p,p)

if __name__ == '__main__': unittest.main()
