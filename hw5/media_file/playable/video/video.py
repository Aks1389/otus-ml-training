from hw5.media_file.playable.playable import Playable

class Video(Playable):
    def __init__(self, path, format, size, created, owner, length, resolution, video_codec, audio_codec):
        super().__init__(path, format, size, created, owner)
        self.length = length
        self.resolution = resolution
        self.video_codec = video_codec
        self.audio_codec = audio_codec

    def convert_to_mkv(name, resolution, audio_bitrate, video_bitrate):
        #конвертирует файл с заданными параметрами
        return
    
    def extract_audio_track(name):
        #извлекает аудио трек в отдельный файл c именем name
        return
    
    def extract_video_track(name):
        #извлекает видео трек в отдельный файл c именем name
        return

    
    