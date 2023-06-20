from ssp.logic.structures \
    import Word


class CategoryToken(Word):
    def __init__(
        self,
        word: str,
        instances: int = 1
    ):
        super().__init__(
            word=word,
            instances=instances
        )
