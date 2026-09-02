from dataclasses import dataclass
from abc import ABC, abstractmethod
from .model import MediaFormat


@dataclass
class AudioPlayer(ABC):
    volume: int
    playback_rate: float

    @abstractmethod
    def supports_format(self) -> MediaFormat:
        pass

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def pause(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    def set_volume(self, volume: int) -> None:
        if 0 <= volume <= 100:
            self.volume = volume
            print(f"Volume set to {volume}")
        else:
            print("Invalid volume level")


@dataclass
class MP3AudioPlayer(AudioPlayer):
    def play(self) -> None:
        print("Playing MP3 audio")

    def pause(self) -> None:
        print("Pausing MP3 audio")

    def stop(self) -> None:
        print("Stopping MP3 audio")

    def supports_format(self) -> MediaFormat:
        return MediaFormat.MP3


@dataclass
class FLACAudioPlayer(AudioPlayer):
    def play(self) -> None:
        print("Playing FLAC audio")

    def pause(self) -> None:
        print("Pausing FLAC audio")

    def stop(self) -> None:
        print("Stopping FLAC audio")

    def supports_format(self) -> MediaFormat:
        return MediaFormat.FLAC
