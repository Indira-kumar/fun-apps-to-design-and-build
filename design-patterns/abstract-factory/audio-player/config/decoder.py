from dataclasses import dataclass
from abc import ABC, abstractmethod
from .model import MediaFormat

@dataclass
class AudioDecoder(ABC):
    audio_data: bytes

    @abstractmethod
    def supports_format(self) -> MediaFormat:
        pass

    @abstractmethod
    def decode(self) -> bytes:
        pass


@dataclass
class MP3AudioDecoder(AudioDecoder):
    def supports_format(self) -> MediaFormat:
        return MediaFormat.MP3

    def decode(self) -> bytes:
        # Implement MP3 decoding logic
        print("Decoding MP3 audio data...")
        # Decoding process
        return self.audio_data


@dataclass
class FLACAudioDecoder(AudioDecoder):
    def supports_format(self) -> MediaFormat:
        return MediaFormat.FLAC

    def decode(self) -> bytes:
        # Implement FLAC decoding logic
        print("Decoding FLAC audio data...")
        # Decoding process
        return self.audio_data