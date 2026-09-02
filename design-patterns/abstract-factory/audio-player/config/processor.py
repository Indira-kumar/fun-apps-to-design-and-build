from dataclasses import dataclass
from abc import ABC, abstractmethod
from .model import MediaFormat


@dataclass
class AudioProcessor(ABC):
    audio_data: bytes

    @abstractmethod
    def supports_format(self) -> MediaFormat:
        pass

    @abstractmethod
    def process(self) -> bytes:
        pass


@dataclass
class MP3AudioProcessor(AudioProcessor):
    def supports_format(self) -> MediaFormat:
        return MediaFormat.MP3

    def process(self) -> bytes:
        # Implement MP3 audio processing logic
        print("Processing MP3 audio data...")
        # Processing process
        return self.audio_data


@dataclass
class FLACAudioProcessor(AudioProcessor):
    def supports_format(self) -> MediaFormat:
        return MediaFormat.FLAC

    def process(self) -> bytes:
        # Implement FLAC audio processing logic
        print("Processing FLAC audio data...")
        # Processing process
        return self.audio_data
