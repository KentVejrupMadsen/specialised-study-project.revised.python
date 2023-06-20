from ssp.variables \
    import get_one

from ssp.logic.structures \
    import Word


class CategoryToken(Word):
    def __init__(
        self,
        word: str,
        instances: int = get_one()
    ):
        super().__init__(
            word=word,
            instances=instances
        )
