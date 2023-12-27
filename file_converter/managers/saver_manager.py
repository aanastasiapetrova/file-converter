from file_converter.savers.file_saver import FileSaver


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


saver_manager = SaverManager()
saver_manager.register_saver("file", FileSaver)
