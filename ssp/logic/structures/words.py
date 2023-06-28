#!/usr/bin/env python
from ssp.logic.structures   \
    import                  \
    Token

from HardenedSteel.globals  \
    import get_integer_one

from HardenedSteel.objects  \
    import CounterObject


class Word(Token):
    def __init__(
        self,
        word: str,
        instances: int = get_integer_one()
    ):
        super().__init__(
            value=word
        )

        self.counter = CounterObject(
            start_value=instances
        )

    def __del__(self):
        super().__del__()
        del self.counter

    def get_counter(self) -> CounterObject:
        return self.counter

    def set_counter(
            self,
            value: CounterObject
    ) -> None:
        self.counter = value

    def reset_counter(self) -> None:
        self.get_counter().reset()

    def set_value_of_counter_to(
            self,
            value: int
    ):
        self.get_counter().set_value(
            value
        )

    def increment_of_counter(self):
        self.get_counter().increment()

    def decrement_of_counter(self):
        self.get_counter().decrement()

    def __int__(self):
        return int(
            self.get_counter()
        )

    def is_instance_of_implementation(
            self,
            other
    ):
        if is_instance_of_word(other):
            other_word_token: Word = other
            if other_word_token.get_hash() == self.get_hash():
                if other_word_token.get_length() == self.get_length():
                    if other_word_token.get_word() == self.get_word():
                        return True
        return False


def is_instance_of_word(
        value
) -> bool:
    return isinstance(
        value,
        Word
    )
