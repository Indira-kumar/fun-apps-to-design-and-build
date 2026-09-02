from abc import ABC, abstractmethod
from .model import MediaFormat
from .decoder import MP3AudioDecoder, FLACAudioDecoder, AudioDecoder
from .player import MP3AudioPlayer, FLACAudioPlayer, AudioPlayer
from .processor import MP3AudioProcessor, FLACAudioProcessor, AudioProcessor

class AudioFactory(ABC):

    @abstractmethod
    def create_audio_player(self, volume, playback_rate) -> AudioPlayer:
        pass

    @abstractmethod
    def create_audio_decoder(self, audio_data) -> AudioDecoder:
        pass

    @abstractmethod
    def create_audio_processor(self, audio_data) -> AudioProcessor:
        pass

    @abstractmethod
    def supports_format(self):
        pass

class MP3AudioFactory(AudioFactory):

    def create_audio_player(self, volume, playback_rate) -> AudioPlayer:
        return MP3AudioPlayer(volume, playback_rate)

    def create_audio_decoder(self, audio_data) -> AudioDecoder:
        return MP3AudioDecoder(audio_data)

    def create_audio_processor(self, audio_data) -> AudioProcessor:
        return MP3AudioProcessor(audio_data)

    def supports_format(self):
        return MediaFormat.MP3

class FLACAudioFactory(AudioFactory):

    def create_audio_player(self, volume, playback_rate) -> AudioPlayer:
        return FLACAudioPlayer(volume, playback_rate)

    def create_audio_decoder(self, audio_data):
        return FLACAudioDecoder(audio_data)

    def create_audio_processor(self, audio_data):
        return FLACAudioProcessor(audio_data)

    def supports_format(self):
        return MediaFormat.FLAC