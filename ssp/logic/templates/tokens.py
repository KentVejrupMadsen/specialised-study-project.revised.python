#!/usr/bin/env python
from ssp.logic.templates    \
    import                  \
    ABC,                    \
    abstractmethod


class Token(ABC):
    def __init__(
        self,
        value: str
    ):
        self.word: str = value
        self.hash: int | None = None

    def __del__(self):
        del             \
            self.word,  \
            self.hash

    def get_word(self) -> str:
        return self.word

    def set_word(
        self,
        value: str
    ) -> None:
        self.word = value
        self.refresh_hash()

    def get_hash(self) -> int:
        if self.is_hash_none():
            self.refresh_hash()

        return self.hash

    def set_hash(
        self,
        value: int
    ) -> None:
        self.hash = value

    def refresh_hash(self):
        self.set_hash(
            hash(
                self.word
            )
        )

    def is_hash_none(self) -> bool:
        return self.hash is None

    @abstractmethod
    def is_instance_of_implementation(self, other):
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
            result: bool = self.get_hash() == other.get_hash()
            if result:
                result = self.get_word() == other.get_word()
                return result

        if is_instance_of_string(other):
            hash_of_other: int = hash(
                str(
                    other
                ).lower()
            )
            result: bool = self.get_hash() == hash_of_other
            if result:
                result = self.get_word() == other
                return result

        return False

    def __str__(self):
        return self.get_word()

    def __hash__(self) -> int:
        return self.get_hash()

    def __int__(self):
        return int(
            self.word
        )


def is_instance_of_token(value) -> bool:
    return isinstance(
        value,
        Token
    )


def is_instance_of_string(value) -> bool:
    return isinstance(
        value,
        str
    )
