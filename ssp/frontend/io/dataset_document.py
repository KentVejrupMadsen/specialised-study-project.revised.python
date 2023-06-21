from os.path \
    import isfile


class DatasetDocument:
    def __init__(
            self,
            location: str
    ):
        self.location: str | None = None
        self.loaded: bool = False

        self.set_location(
            location
        )

    def __repr__(self) -> str:
        return str(
            self.as_dictionary()
        )

    def __del__(self):
        del \
            self.location, \
            self.loaded

    def as_dictionary(self):
        return {
            'location': self.get_location(),
            'loaded': self.is_loaded()
        }

    def exist_file(self):
        if not isfile(
                self.get_location()
        ):
            raise Exception(
                'File not found'
            )

    def get_location(self) -> str:
        return self.location

    def set_location(
            self,
            value: str
    ) -> None:
        self.location = value
        self.exist_file()

    def is_loaded(self) -> bool:
        return self.loaded

    def set_is_loaded(
            self,
            value: bool
    ) -> None:
        self.loaded = value
