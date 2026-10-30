import tempfile
import unittest
from pathlib import Path

from validate import validate_csv


class CsvValidationTests(unittest.TestCase):
    def check_csv(self, content):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.csv'
            path.write_text(content, encoding='utf-8')
            validate_csv(path, ['id', 'what'])

    def test_quoted_commas_and_newlines_are_valid(self):
        self.check_csv('id,what\nA1,"Walking, then talking"\nA2,"Two\nlines"\n')

    def test_wrong_row_width_is_rejected(self):
        for content in ['id,what\nA1\n', 'id,what\nA1,walking,extra\n']:
            with self.subTest(content=content):
                with self.assertRaisesRegex(ValueError, 'width'):
                    self.check_csv(content)

    def test_duplicate_ids_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'duplicate ID'):
            self.check_csv('id,what\nA1,walking\n A1 ,talking\n')

    def test_empty_ids_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'empty ID'):
            self.check_csv('id,what\n ,walking\n')

    def test_required_header_order_is_checked(self):
        with self.assertRaisesRegex(ValueError, 'header'):
            self.check_csv('what,id\nwalking,A1\n')


if __name__ == '__main__':
    unittest.main()
