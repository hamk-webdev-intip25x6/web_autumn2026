from contextlib import redirect_stdout
from io import StringIO
import tempfile
import unittest
from pathlib import Path

from json_file_example import load_dictionary, save_dictionary


class DictionaryJsonFileTests(unittest.TestCase):
    def setUp(self):
        self.temp_directory = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp_directory.name)

    def tearDown(self):
        self.temp_directory.cleanup()

    def test_save_and_load_dictionary_with_arabic_and_simplified_chinese(self):
        expected = {
            "arabic": "مرحبا بالعالم",
            "simplified_chinese": "你好，世界",
            "nested": {"message": "混合文字"},
        }
        path = self.directory / "unicode.json"

        self.assertTrue(save_dictionary(path, expected))

        self.assertEqual(load_dictionary(path), expected)
        self.assertIn("مرحبا", path.read_text(encoding="utf-8"))
        self.assertIn("你好", path.read_text(encoding="utf-8"))

    def test_load_dictionary_rejects_corrupted_json(self):
        path = self.directory / "corrupted.json"
        path.write_text('{"name": "missing closing brace"', encoding="utf-8")

        with redirect_stdout(StringIO()) as output:
            self.assertIsNone(load_dictionary(path))
        self.assertIn("contains invalid JSON", output.getvalue())

    def test_load_dictionary_rejects_non_dictionary_json(self):
        path = self.directory / "list.json"
        path.write_text('["not", "a", "dictionary"]', encoding="utf-8")

        with redirect_stdout(StringIO()) as output:
            self.assertIsNone(load_dictionary(path))
        self.assertIn("contain a dictionary", output.getvalue())

    def test_load_dictionary_rejects_invalid_utf8(self):
        path = self.directory / "invalid-utf8.json"
        path.write_bytes(b'{"message": "\xff"}')

        with redirect_stdout(StringIO()) as output:
            self.assertIsNone(load_dictionary(path))
        self.assertIn("not valid UTF-8", output.getvalue())

    def test_load_dictionary_reports_missing_file(self):
        with redirect_stdout(StringIO()) as output:
            self.assertIsNone(load_dictionary(self.directory / "does-not-exist.json"))
        self.assertIn("was not found", output.getvalue())

    def test_save_dictionary_rejects_non_dictionary_input(self):
        with redirect_stdout(StringIO()) as output:
            self.assertFalse(
                save_dictionary(
                    self.directory / "invalid.json", ["not", "a", "dictionary"]
                )
            )
        self.assertIn("cannot be serialized", output.getvalue())

    def test_save_dictionary_rejects_non_serializable_values(self):
        path = self.directory / "invalid.json"
        path.write_text('{"existing": true}\n', encoding="utf-8")

        with redirect_stdout(StringIO()) as output:
            self.assertFalse(save_dictionary(path, {"value": object()}))
        self.assertIn("cannot be serialized", output.getvalue())

        self.assertEqual(path.read_text(encoding="utf-8"), '{"existing": true}\n')

    def test_save_dictionary_reports_missing_parent_directory(self):
        path = self.directory / "missing" / "dictionary.json"

        with redirect_stdout(StringIO()) as output:
            self.assertFalse(save_dictionary(path, {"value": 1}))
        self.assertIn("parent directory", output.getvalue())

    def test_path_must_be_path_like(self):
        with redirect_stdout(StringIO()) as load_output:
            self.assertIsNone(load_dictionary(42))
        with redirect_stdout(StringIO()) as save_output:
            self.assertFalse(save_dictionary(42, {}))
        self.assertIn("invalid path", load_output.getvalue())
        self.assertIn("invalid path", save_output.getvalue())


if __name__ == "__main__":
    unittest.main()
