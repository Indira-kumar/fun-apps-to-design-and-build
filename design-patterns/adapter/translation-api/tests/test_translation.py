import unittest
from unittest.mock import MagicMock
import inspect

from translation import *


class TranslationAdapterTest(unittest.TestCase):
    def test_methods(self):
        adapter_class = TranslationAdapter
        methods = inspect.getmembers(adapter_class, predicate=inspect.isfunction)

        self.assertTrue(
            len(methods) >= 2,
            "If the adapter class is implemented correctly, there should be at least 2 methods.",
        )

        translate_method = sum(
            1 for name, _ in methods if name.startswith("translate")
        )
        get_supported_languages_method = sum(
            1 for name, _ in methods if name.startswith("get_supported_languages")
        )

        self.assertEqual(
            1,
            translate_method,
            "If the adapter class is implemented correctly, there should be 1 method called translate for translating text which accepts a TranslationRequest and returns a string.",
        )
        self.assertEqual(
            1,
            get_supported_languages_method,
            "If the adapter class is implemented correctly, there should be 1 method called get_supported_languages for getting the supported languages which accepts no parameters and returns a list of strings.",
        )


class TestMicrosoftTranslationAdapter(unittest.TestCase):
    def setUp(self):
        self.mock_translate_api = MagicMock(spec=MicrosoftTranslateApi)
        self.adapter = MicrosoftTranslationAdapter()
        self.adapter.translate_api = self.mock_translate_api

    def test_translate(self):
        request = TranslationRequest(
            text="Hello", source_language="en", target_language="fr"
        )
        self.mock_translate_api.translate.return_value = "Bonjour"
        translated_text = self.adapter.translate(request)
        self.assertEqual(translated_text, "Bonjour")

    def test_get_supported_languages(self):
        self.mock_translate_api.get_supported_languages.return_value = ["fr", "es", "de"]
        supported_languages = self.adapter.get_supported_languages()
        self.assertEqual(supported_languages, ["fr", "es", "de"])


class TestGoogleTranslationAdapter(unittest.TestCase):
    def setUp(self):
        self.mock_google_translate_api = MagicMock(spec=GoogleTranslateApi)
        self.adapter = GoogleTranslationAdapter()
        self.adapter.google_translate_api = self.mock_google_translate_api

    def test_translate(self):
        request = TranslationRequest(
            text="Hello", source_language="en", target_language="fr"
        )
        self.mock_google_translate_api.convert.return_value = "Bonjour"
        translated_text = self.adapter.translate(request)
        self.assertEqual(translated_text, "Bonjour")

    def test_get_supported_languages(self):
        self.mock_google_translate_api.get_languages.return_value = ["fr", "es", "de"]
        supported_languages = self.adapter.get_supported_languages()
        self.assertEqual(supported_languages, ["fr", "es", "de"])


if __name__ == "__main__":
    unittest.main()