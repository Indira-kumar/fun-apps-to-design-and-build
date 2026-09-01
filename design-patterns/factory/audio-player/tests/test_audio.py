import unittest
from audio import *


class TestAudioPlayer(unittest.TestCase):
    def setUp(self):
        self.player = FLACPlayer(50, 1.0)

    def test_inheritance(self):
        self.assertIsInstance(
            self.player,
            AudioPlayer,
            "If there is a common parent AudioPlayer class, the FLACPlayer class should inherit from it",
        )

    def test_fields(self):
        self.assertTrue(
            hasattr(self.player, "volume"),
            "If there is a common parent AudioPlayer class, it should have a volume field",
        )
        self.assertTrue(
            hasattr(self.player, "playBackRate"),
            "If there is a common parent AudioPlayer class, it should have a playBackRate field",
        )

    def test_methods(self):
        self.assertTrue(
            hasattr(self.player, "play"),
            "If there is a common parent AudioPlayer class, it should have a play method",
        )
        self.assertTrue(
            hasattr(self.player, "pause"),
            "If there is a common parent AudioPlayer class, it should have a pause method",
        )
        self.assertTrue(
            hasattr(self.player, "stop"),
            "If there is a common parent AudioPlayer class, it should have a stop method",
        )
        self.assertTrue(
            hasattr(self.player, "supports_type"),
            "If there is a common parent AudioPlayer class, it should have a supports_type method",
        )

    def test_type_check(self):
        self.assertIsInstance(
            self.player.volume,
            int,
            "If there is a common parent AudioPlayer class, the volume field should be an int",
        )
        self.assertIsInstance(
            self.player.playBackRate,
            float,
            "If there is a common parent AudioPlayer class, the playBackRate field should be a float",
        )


class TestAudioPlayerFactory(unittest.TestCase):
    def test_create_mp3_player(self):
        mp3_player = AudioPlayerFactory.create_audio_player(MediaFormat.MP3, 50, 1.0)
        self.assertIsInstance(
            mp3_player,
            MP3Player,
            "If the requested format is MP3, the factory should return an MP3Player",
        )

    def test_create_wav_player(self):
        wav_player = AudioPlayerFactory.create_audio_player(MediaFormat.WAV, 50, 1.0)
        self.assertIsInstance(
            wav_player,
            WAVPlayer,
            "If the requested format is WAV, the factory should return a WAVPlayer",
        )

    def test_create_flac_player(self):
        flac_player = AudioPlayerFactory.create_audio_player(MediaFormat.FLAC, 50, 1.0)
        self.assertIsInstance(
            flac_player,
            FLACPlayer,
            "If the requested format is FLAC, the factory should return a FLACPlayer",
        )


if __name__ == "__main__":
    unittest.main()
