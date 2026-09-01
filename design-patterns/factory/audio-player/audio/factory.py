from .products import MediaFormat, FLACPlayer, MP3Player, WAVPlayer

class AudioPlayerFactory:
    _registry = {
        MediaFormat.FLAC: FLACPlayer,
        MediaFormat.MP3: MP3Player,
        MediaFormat.WAV: WAVPlayer,
    }

    @classmethod
    def create_audio_player(cls, type: MediaFormat, volume, playBackRate):
        try:
            audio_player_cls = cls._registry[type]
        except KeyError:
            raise ValueError('Unsupported format: ', type)
        return audio_player_cls(volume, playBackRate)
