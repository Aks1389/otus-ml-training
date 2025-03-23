from abc import ABC

class MediaFile(ABC):
    def __init__(self, path, format, size, created, owner):
        self.path = path
        self.format = format
        self.size = size
        self.created = created
        self.owner = owner

    def create(name):
        #создает файл с указанным именем
        return
    
    def update(name, *args):
        #обновляет в файле с именем name перечисленные атрибуты
        return
    
    def info(name):
        #возвращает словарь со всеми атрибутами файла
        return

    def get_name():
        #Возвращает имя файла путем извлечения его из пути к файлу
        return