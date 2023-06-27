#!/usr/bin/env python
from ssp.logic.structures   \
    import                  \
    Word

from HardenedSteel.globals  \
    import get_integer_one


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

    def __del__(self):
        del                 \
            self.word,      \
            self.counter,   \
            self.hash

