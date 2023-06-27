#!/usr/bin/env python
from ssp.logic.templates        \
    import                      \
    ABC,                        \
    abstractmethod

from HardenedSteel.facades      \
    import is_integer_zero


class Token(ABC):
    def __init__(
        self,
        value: str | None
    ):
        self.word: str = value
        self.hash: int | None = None
        self.length: int | None = None

        self.on_change_event()

    def __del__(self):
        del                 \
            self.word,      \
            self.hash,      \
            self.length

    def get_length(self) -> int:
        if self.is_length_none():
            self.refresh_length()
        return self.length

    def set_length(
            self,
            value: int
    ) -> None:
        self.length = value

    def is_length_none(self) -> bool:
        return self.length is None

    def get_word(self) -> str:
        return self.word

    def set_word(
        self,
        value: str
    ) -> None:
        self.word = value
        self.on_change_event()

    def get_hash(self) -> int:
        return self.hash

    def set_hash(
        self,
        value: int
    ) -> None:
        self.hash = value

    def on_change_event(self) -> None:
        self.refresh_hash()

    def refresh_hash(self) -> None:
        self.set_hash(
            hash(
                self.get_word()
            )
        )

    def refresh_length(self) -> None:
        self.set_length(
            len(
                self
            )
        )

    def is_string_empty(self) -> bool:
        if is_integer_zero(
            len(self)
        ):
            return True
        return self.get_word().isspace()

    def is_hash_none(self) -> bool:
        return self.hash is None

    def is_word_none(self) -> bool:
        return self.word is None

    @abstractmethod
    def is_instance_of_implementation(
            self,
            other
    ):
        return False

    def __eq__(
        self,
        other
    ):
        if self.is_instance_of_implementation(
            other=other
        ):
            return True

        if is_instance_of_token(other):
            result_of_hash: bool = self.get_hash() == other.get_hash()
            if result_of_hash:
                result_of_hash = self.get_word() == other.get_word()
                return result_of_hash

        if is_instance_of_string(other):
            return self.is_equal_to_string(
                other
            )

        return False

    def is_equal_to_string(
            self,
            value: str
    ) -> bool:
        hash_of_other: int = hash(
            value.lower()
        )
        result_of_hash: bool = self.get_hash() == hash_of_other
        if result_of_hash:
            length_of_other: int = len(
                value
            )
            is_equal_length: bool = (length_of_other == len(self))
            if is_equal_length:
                return value == str(self)
        return False

    def __str__(self):
        return str(
            self.get_word()
        )

    def __len__(self):
        return len(
            self.get_word()
        )

    def __hash__(self) -> int:
        return self.get_hash()

    def __int__(self):
        return int(
            self.word
        )


def is_instance_of_token(
        value
) -> bool:
    return isinstance(
        value,
        Token
    )


def is_instance_of_string(value) -> bool:
    return isinstance(
        value,
        str
    )
