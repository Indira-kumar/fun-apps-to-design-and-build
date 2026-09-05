from abc import ABC, abstractmethod
from .model import *
from .services import *

class TranslationAdapter(ABC):
    @abstractmethod
    def get_supported_languages(self):
        raise NotImplementedError()
    
    @abstractmethod
    def translate(self):
        raise NotImplementedError()


class MicrosoftTranslationAdapter(TranslationAdapter):
    def __init__(self):
        self.translate_api = MicrosoftTranslateApi()

    def get_supported_languages(self):
        return self.translate_api.get_supported_languages()

    def translate(self, request: TranslationRequest):
        return self.translate_api.translate(request.text, request.source_language, request.target_language)



class GoogleTranslationAdapter(TranslationAdapter):
    def __init__(self):
        self.google_translate_api = GoogleTranslateApi()

    def get_supported_languages(self):
        return self.google_translate_api.get_languages()

    def translate(self, request: TranslationRequest):
        return self.google_translate_api.convert(request.text, request.source_language, request.target_language, 1.0)

