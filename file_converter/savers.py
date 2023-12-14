from abc import ABC, abstractmethod

class SaverManager:
    def __init__(self):
        self._savers = {}
    

    def register_saver(self, type, saver):
        self._savers[type] = saver

    
    def get_saver(self, type):
        saver = self._savers[type]
        if not saver:
             raise ValueError(f"{format} type saver isn't registered.")
        return saver()
    

class Saver(ABC):
    def __init__(self):
        pass


    @abstractmethod
    def save(self):
        raise NotImplementedError
    

class FileSaver(Saver):
    def save(self, filepath, data):
        with open(filepath, 'a', encoding='utf8') as filename:
            filename.write(str(data))


saver_manager = SaverManager()
saver_manager.register_saver('file', FileSaver)