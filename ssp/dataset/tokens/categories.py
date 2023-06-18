from ssp.dataset \
    import CounterObject

from ssp.dataset.tokens \
    import TokenWord


class CategoryToken:
    def __init__(
            self,
            token_name: str
    ):
        self.word = TokenWord(token_name)
        self.counter = CounterObject()

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
