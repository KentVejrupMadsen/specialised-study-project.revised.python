from io \
    import TextIOWrapper

from ssp.adhoc          \
    import isfile


class DatasetDocument:
    def __init__(
            self,
            location: str
    ):
        self.location: str | None = None
        self.hash: int | None = None

        self.object: TextIOWrapper | None = None

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

        self.close()

    def __hash__(self) -> int:
        return self.get_hash()

    def open(self) -> None:
        self.set_object(
            open(
                self.get_location(),
                'rt'
            )
        )

    def load_line(self) -> str:
        line = self.get_object().readline()

        if not line:
            self.set_is_loaded(
                True
            )

        return line

    def close(self) -> None:
        if not self.is_object_none():
            self.object.close()

    def is_object_none(self) -> bool:
        return self.object is None

    def get_object(self) -> TextIOWrapper:
        if self.is_object_none():
            self.open()

        return self.object

    def set_object(
            self,
            value: TextIOWrapper
    ) -> None:
        self.object = value

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
