from hw5.media_file.playable import Playable

class Audio(Playable):
    def __init__(self, name, format, size, created, owner, codec, bitrate, length, sampling_rate):
        super().__init__(name, format, size, created, owner)
        self.codec = codec
        self.bitrate = bitrate
        self.length = length
        self.sampling_rate = sampling_rate
    
    def convert_to_mp3(name, bitrate, sampling_rate):
        #переконвернирует файл с указанными новым именем, битрейтом и частотой дискретизации
        return
    
    

