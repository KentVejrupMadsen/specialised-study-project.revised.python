from ssp.logic.structures \
    import Word


class DocumentToken(Word):
    def __init(
            self,
            word: str,
            instances: int = 1
    ):
        super().__init__(
            word=word,
            instances=instances
        )
