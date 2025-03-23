from hw5.media_file.media_file import MediaFile

class Playable(MediaFile):
    def __init__(self, path, format, size, created, owner):
        super().__init__(path, format, size, created, owner)

    def play():
        #запускает воспроизведение приложением по умолчанию
        return

    def trim(start_time, end_time):
        #выполняет обрезку файла
        return