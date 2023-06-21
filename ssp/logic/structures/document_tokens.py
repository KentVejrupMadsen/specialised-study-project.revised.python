from ssp.variables \
    import get_one

from ssp.logic.structures \
    import Word


class DocumentToken(Word):
    def __init(
        self,
        word: str,
        instances: int = get_one()
    ):
        super().__init__(
            word=word,
            instances=instances
        )

    def __del__(self):
        del                 \
            self.word,      \
            self.counter,   \
            self.hash

