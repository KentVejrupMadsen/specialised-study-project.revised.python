import os


class Dataset:
    def __init__(self):
        self.path = ''

    def set_path(self, newPath):
        self.path = newPath

    def get_path(self):
        return self.path

    def exists_current_path(self):
        return os.path.exists(self.path)

