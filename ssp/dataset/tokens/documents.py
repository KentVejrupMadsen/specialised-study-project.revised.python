from ssp.dataset \
    import CounterObject

from ssp.dataset.tokens \
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

    def set_word(
            self,
            token: TokenWord
    ):
        self.word = token

    def get_word(self) -> TokenWord:
        return self.word
