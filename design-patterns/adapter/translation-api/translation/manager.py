from .model import GoogleTranslationRequest
from .services import *


class TranslationManager:
    def __init__(self):
        self.google_translate_api = GoogleTranslateApi()
        self.microsoft_translate_api = MicrosoftTranslateApi()

    def translate(
        self, text: str, source_language: str, target_language: str, provider: str
    ) -> str:
        if provider == "google":
            request = GoogleTranslationRequest(
                text, source_language, target_language, 0.8
            )
            return self.google_translate_api.convert(request)
        elif provider == "microsoft":
            return self.microsoft_translate_api.translate(
                text, source_language, target_language
            )
        else:
            raise ValueError("Invalid provider")
