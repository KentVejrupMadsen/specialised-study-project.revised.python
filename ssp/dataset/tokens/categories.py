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

