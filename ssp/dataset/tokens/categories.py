from ssp.dataset \
    import CounterObject

from ssp.dataset.tokens \
    import TokenWord


class CategoryToken:
    def __init__(
            self,
            token_name: str
    ):
        self.word = TokenWord(
            token_name
        )

        self.counter = CounterObject()

    def increment(self) -> int:
        self.counter.increment()

        return int(
            self.counter
        )

    def increase(
            self,
            value
    ) -> int:
        self.counter.increase(
            value
        )

        return int(
            self.counter
        )

    def decrease(
            self,
            value
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

    def get_word(self) -> TokenWord:
        return self.word

    def set_word(
            self,
            value: TokenWord
    ) -> None:
        self.word = value

    def get_counter(self) -> CounterObject:
        return self.counter

    def set_counter(
            self,
            value: CounterObject
    ) -> None:
        self.counter = value
