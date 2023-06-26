#!/usr/bin/env python
from ssp.persistence                \
    import                          \
    TextIOBase,                     \
    isfile,                         \
    ascii_lowercase_begin,          \
    ascii_lowercase_end,            \
    ascii_uppercase_begin,          \
    ascii_uppercase_end,            \
    get_ascii_number_range_start,   \
    get_ascii_number_range_end,     \
    raise_file_not_found


def detect_is_character_in_uppercase_letter_range(
        character: chr
) -> bool:
    character_index: int = ord(character)

    if(
        (ascii_uppercase_begin <= character_index)
        and
        (character_index >= ascii_uppercase_end)
    ):
        return True

    return False


def detect_is_character_in_lowercase_letter_range(
        character: chr
) -> bool:
    character_index: int = ord(character)

    if(
        (ascii_lowercase_begin <= character_index)
        and
        (character_index >= ascii_lowercase_end)
    ):
        return True

    return False


def detect_is_character_in_number_range(
        character: chr
) -> bool:
    character_index: int = ord(character)

    if(
        (get_ascii_number_range_start() <= character_index)
        and
        (character_index >= get_ascii_number_range_end())
    ):
        return True

    return False


class DatasetDocumentStream:
    def __init__(
            self,
            location: str
    ):
        self.location: str | None = None
        self.hash: int | None = None

        self.object: TextIOBase | None = None

        self.loaded: bool = False

        self.set_location(
            location
        )

        self.normalise: bool = False

        self.buffer: str | None = None

    def is_to_normalise(self) -> bool:
        return self.normalise

    def set_is_to_normalise(
            self,
            value: bool
    ) -> None:
        self.normalise = value

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
                'rt',
                encoding='utf8',
                errors='ignore'
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
        if self.is_object_none():
            self.open()

        line = self.get_object().readline()
        self.set_buffer(
            line
        )

        if not line:
            self.set_is_loaded(
                True
            )

        return self.___output_line(
            self.get_buffer()
        )

    def ___output_line(
            self,
            line: str
    ):
        if self.is_to_normalise():
            return line.lower()
        else:
            return line

    def is_line_empty(self) -> bool:
        if self.get_buffer() is None:
            return True

        if self.get_buffer().isspace():
            return True

        if not self.has_line_valid_characters():
            return True

        return False

    # makes sure that the line in the buffer has valid character values in it.
    def has_line_valid_characters(self) -> bool:
        for character in self.get_buffer():
            if detect_is_character_in_uppercase_letter_range(
                character
            ):
                return True

            if detect_is_character_in_lowercase_letter_range(
                character
            ):
                return True

            if detect_is_character_in_number_range(
                character
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

    def get_object(self) -> TextIOBase:
        if self.is_object_none():
            self.open()

        return self.object

    def set_object(
            self,
            value
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
            raise_file_not_found()

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

    def is_not_loaded(self) -> bool:
        return not(
            self.is_loaded()
        )

    def set_is_loaded(
            self,
            value: bool
    ) -> None:
        self.loaded = value
