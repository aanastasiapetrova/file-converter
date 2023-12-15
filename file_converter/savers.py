from abc import ABC, abstractmethod


class SaverManager:
    """Saver factory class to manage savers classes."""

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
    """Abstract saver's interface."""

    def __init__(self):
        pass

    @abstractmethod
    def save(self):
        raise NotImplementedError


class FileSaver(Saver):
    """Saver to file class realization."""

    def save(self, filepath, data):
        with open(filepath, "w", encoding="utf8") as filename:
            filename.write(str(data))


saver_manager = SaverManager()
saver_manager.register_saver("file", FileSaver)
