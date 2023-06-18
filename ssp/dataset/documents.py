#!/usr/bin/env python
class Document:
    def __init__(
            self,
            location: str
    ):
        self.file_location: str = location
        self.file_object = None

    def __del__(self):
        self.done()

    def open(self):
        self.set_file_object(
            open(
                self.file_location,
                'r'
            )
        )

    def done(self):
        if not(self.get_file_object() is None):
            self.get_file_object().close()

    def get_file_location(self) -> str:
        return self.file_location

    def set_file_location(
            self,
            location: str
    ) -> None:
        self.file_location = location

    def get_file_object(self):
        return self.file_object

    def set_file_object(self, value) -> None:
        self.file_object = value
