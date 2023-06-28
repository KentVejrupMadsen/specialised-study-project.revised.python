#!/usr/bin/env python
from ssp.logic.templates        \
    import                      \
    ABC,                        \
    abstractmethod

from HardenedSteel.facades      \
    import is_integer_zero

from HardenedSteel.objects      \
    import CounterObject


class Token(ABC):
    def __init__(
        self,
        value: str | None
    ):
        self.word: str = value

        self.hash: int | None = None
        self.length: int | None = None
        self.iterator: CounterObject | None = None

        self.on_change_event()

    def __del__(self):
        del                 \
            self.word,      \
            self.hash,      \
            self.length,    \
            self.iterator

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

    def get_iterator(self) -> CounterObject:
        if self.is_iterator_none():
            self.set_iterator(
                CounterObject()
            )
        return self.iterator

    def is_iterator_none(self) -> bool:
        return self.iterator is None

    def set_iterator(
            self,
            value: CounterObject
    ):
        self.iterator = value

    def on_change_event(self) -> None:
        self.refresh_length()
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
                self.get_word()
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

    def is_hash_the_same_as(
            self,
            hash_by: int
    ) -> bool:
        return self.get_hash() == hash_by

    def is_word_the_same_as(
            self,
            word: str
    ) -> bool:
        return self.get_word() == word

    def is_length_of_word_same_as(
        self,
        size: int
    ):
        return self.get_length() == size

    def __eq__(
        self,
        other
    ):
        if self.is_instance_of_implementation(
            other=other
        ):
            return True

        if is_instance_of_token(other):
            if self.is_hash_the_same_as(
                other.get_hash()
            ):
                return self.is_word_the_same_as(
                    other.get_word()
                )

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

        if self.is_hash_the_same_as(
                hash_of_other
        ):
            length_of_other: int = len(
                value
            )
            if self.is_length_of_word_same_as(
                    length_of_other
            ):
                return self.is_word_the_same_as(
                    value
                )

        return False

    def __str__(self) -> str:
        return str(
            self.get_word()
        )

    def __len__(self) -> int:
        return int(
            self.get_length()
        )

    def __hash__(self) -> int:
        return self.get_hash()

    def __int__(self) -> int:
        return int(
            self.get_length()
        )

    def __iter__(self):
        self.get_iterator().reset()
        return self

    def __next__(self):
        self.get_iterator().increment()

        if self.get_iteration_index() < len(self):
            return self.get_iteration_index()
        else:
            raise StopIteration

    def get_iteration_index(self):
        return self.get_iterator().previous()


def is_instance_of_token(
    value
) -> bool:
    return isinstance(
        value,
        Token
    )


def is_instance_of_string(
    value
) -> bool:
    return isinstance(
        value,
        str
    )
