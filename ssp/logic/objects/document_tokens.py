#!/usr/bin/env python
from ssp.logic.objects      \
    import                  \
    Word

from HardenedSteel.globals  \
    import                  \
    get_integer_one


class DocumentToken(Word):
    def __init__(
        self,
        word: str,
        instances: int = get_integer_one()
    ):
        super().__init__(
            word=word,
            instances=instances
        )

        self.set_is_to_normalise(
            True
        )

    def __del__(self):
        super().__del__()

    def __repr__(self):
        return str(
            dir(self)
        )

    def __dir__(self) -> list:
        result: list = super().__dir__()
        return result
