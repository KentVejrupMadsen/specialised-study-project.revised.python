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

        self.buffer: str | None = None

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

    def get_buffer(self) -> None | str:
        return self.buffer

    def set_buffer(
            self,
            value: str | None
    ) -> None:
        self.buffer = value

    def load_line(self) -> str:
        line = self.get_object().readline()
        self.set_buffer(
            line
        )

        if not line:
            self.set_is_loaded(
                True
            )

        return self.get_buffer()

    def is_line_empty(self) -> bool:
        if self.get_buffer() is None:
            return True

        if self.get_buffer().isspace():
            return True

        if(
            not (self.__buffer_contains_letters())
            and
            not (self.__buffer_contains_numbers())
        ):
            return True

        return False

    # TODO: remove and make more effective later
    def __buffer_contains_letters(self) -> bool:
        if self.get_buffer() is None:
            return False

        for character in self.get_buffer():
            integer_representation: int = ord(character)

            if(
                ord('a') <= integer_representation
                and
                integer_representation >= ord('z')
            ):
                return True

            if(
                ord('A') <= integer_representation
                and
                integer_representation >= ord('Z')
            ):
                return True

        return False

    # TODO: remove and make more effective later
    def __buffer_contains_numbers(self) -> bool:
        if self.get_buffer() is None:
            return False

        for character in self.get_buffer():
            integer_representation: int = ord(character)

            if(
                ord('0') <= integer_representation
                and
                integer_representation >= ord('9')
            ):
                return True

        return False

    def close(self) -> None:
        if not self.is_object_none():
            self.object.close()

    def reset(self):
        self.set_is_loaded(False)
        self.set_buffer(None)

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
