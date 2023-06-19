#!/usr/bin/env python
from ssp.logic.structures \
    import CounterObject

from ssp.logic.tokens \
    import TokenWord


class DocumentToken:
    def __init__(
            self,
            token_name: str
    ):
        self.word = TokenWord(
            token_name
        )

        self.counter = CounterObject()

    def increase(
            self,
            value: int
    ) -> int:
        self.counter.increase(
            value
        )

        return int(
            self.counter
        )

    def increment(self) -> int:
        self.counter.increment()

        return int(
            self.counter
        )

    def decrease(
            self,
            value: int
    ) -> int:
        self.counter.decrease(
            value
        )

        return int(
            self.counter
        )

    def decrement(self) -> int:
        self.counter.decrement()

        return int(
            self.counter
        )

    def set_counter_value(
            self,
            size: int
    ) -> int:
        self.counter.set_value(
            size
        )

        return int(
            self.counter
        )

    def get_counter_value(self) -> int:
        return int(
            self.counter
        )

    def set_word(
            self,
            token: TokenWord
    ):
        self.word = token

    def get_word(self) -> TokenWord:
        return self.word

    def get_counter(self) -> CounterObject:
        return self.counter

    def set_counter(
            self,
            value: CounterObject
    ) -> None:
        self.counter = value

    def __str__(self) -> str:
        return str(
            self.get_word()
        )

    def __int__(self) -> int:
        return int(
            self.counter
        )