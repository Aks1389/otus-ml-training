from hw5.media_file.media_file import MediaFile

class Photo(MediaFile):
    def __init__(self, path, format, size, created, owner, resolution, bit_depth):
        super().__init__(path, format, size, created, owner)
        self.resolution = resolution
        self.bit_depth = bit_depth

    def print():
        #отправляет фото на печать
        return
    
    def crop(point_a_x, point_a_y, point_b_x, point_b_y):
        #обрезать фото по области с заданными двумя точками
        return
    
    def scale(percent):
        #меняет размер изображения на заданный процент
        return
