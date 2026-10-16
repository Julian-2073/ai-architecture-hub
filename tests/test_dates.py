"""A date recorded in UTC+08 stays valid when the reader runs on UTC."""
from datetime import date, datetime, timezone
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('date_kb',ROOT/'scripts/kb.py')
kb=importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb)


class RecordingDateTests(unittest.TestCase):
    def test_same_instant_crosses_recording_midnight(self):
        instant=datetime(2026,10,16,17,32,tzinfo=timezone.utc)
        self.assertEqual(kb.catalog_today({'date_utc_offset':'+08:00'},instant),date(2026,10,17))
        self.assertEqual(kb.catalog_today({'date_utc_offset':'-08:00'},instant),date(2026,10,16))

    def test_invalid_recording_offset_is_rejected(self):
        for value in ('+24:00','+08:60','Asia/Shanghai',8,None):
            if value is None:continue # Missing offset intentionally supports legacy catalogs.
            with self.subTest(value=value),self.assertRaises(ValueError):
                kb.catalog_today({'date_utc_offset':value})

    def test_naive_instant_is_rejected(self):
        with self.assertRaises(ValueError):
            kb.catalog_today({'date_utc_offset':'+08:00'},datetime(2026,10,16,17,32))

    def test_genuinely_future_record_still_warns(self):
        data=kb.load(ROOT)
        data['records'][0]['reviewed_at']='2999-01-01'
        report=kb.validate(ROOT,data)
        self.assertTrue(report['ok'],report)
        self.assertTrue(any('2999-01-01' in w for w in report['warnings']))


if __name__=='__main__':unittest.main(verbosity=2)
