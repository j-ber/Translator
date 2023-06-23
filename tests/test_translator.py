import unittest
from translator import translate_english_to_french, translate_french_to_english

class TranslationTestCase(unittest.TestCase):

    def test_french_to_english_equal(self):
        french_text = "Bonjour, comment ça va ?"
        expected_english_translation = "Hi, how are you?"
        actual_english_translation = translate_french_to_english(french_text)
        self.assertEqual(actual_english_translation, expected_english_translation)

    def test_french_to_english_not_equal(self):
        french_text = "Bonjour, comment ça va ?"
        expected_english_translation = "Hello, how are you?"
        actual_english_translation = translate_french_to_english(french_text)
        self.assertNotEqual(actual_english_translation, expected_english_translation)

    def test_english_to_french_equal(self):
        english_text = "Hi, how are you?"
        expected_french_translation = "Bonjour, comment ça va ?"
        actual_french_translation = translate_english_to_french(english_text)
        self.assertEqual(actual_french_translation, expected_french_translation)

    def test_english_to_french_not_equal(self):
        english_text = "Hello, how are you?"
        expected_french_translation = "Salut, comment ça va ?"
        actual_french_translation = translate_english_to_french(english_text)
        self.assertNotEqual(actual_french_translation, expected_french_translation)

if __name__ == '__main__':
    unittest.main()
