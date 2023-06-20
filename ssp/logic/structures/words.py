from ssp.variables \
    import get_one

from ssp.logic.structures\
    import \
    Token, \
    CounterObject


class Word(Token):
    def __init__(
        self,
        word: str,
        instances: int = get_one()
    ):
        super().__init__(
            value=word
        )

        self.counter = CounterObject(
            start_value=instances
        )

    def get_counter(self) -> CounterObject:
        return self.counter

    def set_counter(
            self,
            value: CounterObject
    ) -> None:
        self.counter = value
