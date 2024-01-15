# from file_converter.savers.file_saver import FileSaver


class SaverManager:
    """Saver factory class to manage savers classes."""

    def __init__(self):
        self._savers = {}

    def register(self, type, saver):
        self._savers[type] = saver

    def get(self, type):
        saver = self._savers[type]
        if not saver:
            raise ValueError(f"{format} type saver isn't registered.")
        return saver()


savers_manager = SaverManager()
# saver_manager.register("file", FileSaver)
