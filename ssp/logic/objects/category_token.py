#!/usr/bin/env python
from ssp.logic.objects      \
    import                  \
    Word

from HardenedSteel.globals  \
    import                  \
    get_integer_one


class CategoryToken(
    Word
):
    def __init__(
        self,
        word: str,
        instances: int = get_integer_one(),
        normalise: bool = True
    ):
        super().__init__(
            word=word,
            instances=instances,
            normalise=normalise
        )

        self.on_event_normalise()

    def __del__(self):
        super().__del__()

    def __repr__(self):
        return str(
            dict(
                {
                    'word': self.get_word(),
                    'instances': int(
                        self.get_counter()
                    ),
                    'hash': self.get_hash(),
                    'length': self.get_length()
                }
            )
        )

    def __dir__(self) -> list:
        result: list = super().__dir__()
        return result


