from os.path \
    import isfile


class DatasetDocument:
    def __init__(
            self,
            location: str
    ):
        self.location: str | None = None
        self.hash: int | None = None

        self.loaded: bool = False

        self.set_location(
            location
        )

    def __repr__(self) -> str:
        return str(
            self.as_dictionary()
        )

    def __del__(self) -> None:
        del                 \
            self.location,  \
            self.loaded,    \
            self.hash

    def __hash__(self) -> int:
        return self.get_hash()

    def set_hash(
            self,
            value: int
    ):
        self.hash = value

    def get_hash(self) -> int:
        if self.hash is None:
            self.update_hash()

        return self.hash

    def update_hash(self):
        self.set_hash(
            hash(
                self.location
            )
        )

    def as_dictionary(self) -> dict:
        return {
            'location': self.get_location(),
            'loaded': self.is_loaded()
        }

    def exist_file(self) -> None:
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
