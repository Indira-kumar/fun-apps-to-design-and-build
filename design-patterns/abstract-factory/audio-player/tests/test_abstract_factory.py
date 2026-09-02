import unittest
from config import *


class TestAudioFactory(unittest.TestCase):

    def test_methods(self):
        flac_factory = FLACAudioFactory()
        methods = [
            "supports_format",
            "create_audio_player",
            "create_audio_decoder",
            "create_audio_processor",
        ]
        for method in methods:
            self.assertTrue(
                hasattr(flac_factory, method),
                f"If the abstract factory is correctly implemented, AudioFactory should have a method named {method}.",
            )

    def test_flac_audio_factory(self):
        flac_factory = FLACAudioFactory()

        # Check supported format
        self.assertEqual(
            flac_factory.supports_format(),
            MediaFormat.FLAC,
            "If the factory supports FLAC format, it should return MediaFormat.FLAC.",
        )

        # Create mock data
        volume = 50
        playback_rate = 1.0
        audio_data = b"Some audio data"

        # Create objects using the factory
        audio_player = flac_factory.create_audio_player(volume, playback_rate)
        audio_decoder = flac_factory.create_audio_decoder(audio_data)
        audio_processor = flac_factory.create_audio_processor(audio_data)

        # Check types of created objects
        self.assertIsInstance(
            audio_player,
            AudioPlayer,
            "If the create_audio_player method is called, it should return an object of type AudioPlayer.",
        )
        self.assertIsInstance(
            audio_decoder,
            AudioDecoder,
            "If the create_audio_decoder method is called, it should return an object of type AudioDecoder.",
        )
        self.assertIsInstance(
            audio_processor,
            AudioProcessor,
            "If the create_audio_processor method is called, it should return an object of type AudioProcessor.",
        )

    def test_mp3_audio_factory(self):
        mp3_factory = MP3AudioFactory()

        # Check supported format
        self.assertEqual(
            mp3_factory.supports_format(),
            MediaFormat.MP3,
            "If the factory supports MP3 format, it should return MediaFormat.MP3.",
        )

        # Create mock data
        volume = 70
        playback_rate = 1.5
        audio_data = b"Some other audio data"

        # Create objects using the factory
        audio_player = mp3_factory.create_audio_player(volume, playback_rate)
        audio_decoder = mp3_factory.create_audio_decoder(audio_data)
        audio_processor = mp3_factory.create_audio_processor(audio_data)

        # Check types of created objects
        self.assertIsInstance(
            audio_player,
            AudioPlayer,
            "If the create_audio_player method is called, it should return an object of type AudioPlayer.",
        )
        self.assertIsInstance(
            audio_decoder,
            AudioDecoder,
            "If the create_audio_decoder method is called, it should return an object of type AudioDecoder.",
        )
        self.assertIsInstance(
            audio_processor,
            AudioProcessor,
            "If the create_audio_processor method is called, it should return an object of type AudioProcessor.",
        )


if __name__ == "__main__":
    unittest.main()
