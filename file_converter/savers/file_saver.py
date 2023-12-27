from file_converter.savers.base_saver import Saver


class FileSaver(Saver):
    """Saver to file class realization."""

    def save(self, filepath, data):
        with open(filepath, "w", encoding="utf8") as filename:
            filename.write(str(data))
