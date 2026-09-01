from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


# COMPLETE THIS CLASS
@dataclass
class AudioPlayer(ABC):
    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def set_volume(self, volume: int):
        pass

    @abstractmethod
    def supports_type(self):
        pass

class MediaFormat(Enum):
    MP3 = "mp3"
    WAV = "wav"
    FLAC = "flac"


@dataclass
class FLACPlayer(AudioPlayer):
    volume: int
    playBackRate: float

    def play(self):
        print("Playing FLAC audio")

    def pause(self):
        print("Pausing FLAC audio")

    def stop(self):
        print("Stopping FLAC audio")

    def set_volume(self, volume: int):
        if 0 <= volume <= 100:
            self.volume = volume
            print("Volume set to", volume)
        else:
            print("Invalid volume level")

    def supports_type(self):
        return MediaFormat.FLAC


@dataclass
class MP3Player(AudioPlayer):
    volume: int
    playBackRate: float

    def play(self):
        print("Playing MP3 audio")

    def pause(self):
        print("Pausing MP3 audio")

    def stop(self):
        print("Stopping MP3 audio")

    def set_volume(self, volume: int):
        if 0 <= volume <= 100:
            self.volume = volume
            print("Volume set to", volume)
        else:
            print("Invalid volume level")

    def supports_type(self):
        return MediaFormat.MP3


@dataclass
class WAVPlayer(AudioPlayer):
    volume: int
    playBackRate: float

    def play(self):
        print("Playing WAV audio")

    def pause(self):
        print("Pausing WAV audio")

    def stop(self):
        print("Stopping WAV audio")

    def set_volume(self, volume: int):
        if 0 <= volume <= 100:
            self.volume = volume
            print("Volume set to", volume)
        else:
            print("Invalid volume level")

    def supports_type(self):
        return MediaFormat.WAV
