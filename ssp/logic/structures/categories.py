from ssp.logic.templates    \
    import BagOfWords

from ssp.logic.structures   \
    import CategoryToken

from HardenedSteel.objects  \
    import CounterObject


class Category(BagOfWords):
    def __init__(
            self,
            category_name: str
    ):
        super().__init__()
        self.category_name: str = category_name
        self.tokens: list | None = None
        self.iterator: CounterObject | None = None

    def __del__(self):
        super().__del__()
        del                         \
            self.category_name,     \
            self.tokens

    def get_name(self) -> str:
        return self.category_name

    def set_name(
            self,
            value: str
    ) -> None:
        self.category_name = value

    def get_tokens(self) -> list:
        if self.is_tokens_none():
            self.set_tokens(
                list()
            )
        return self.tokens

    def set_tokens(
            self,
            value: list
    ) -> None:
        self.tokens = value

    def is_tokens_none(self) -> bool:
        return self.tokens is None

    def on_event_found_token(
            self,
            token: str
    ):
        pass

    def get_iterator(self) -> CounterObject:
        if self.is_tokens_none():
            self.set_iterator(
                CounterObject()
            )
        return self.iterator

    def set_iterator(
            self,
            value: CounterObject
    ) -> None:
        self.iterator = value

    def is_iterator_none(self) -> bool:
        return self.iterator is None

    def __iter__(self):
        if self.is_tokens_none():
            self.set_iterator(
                CounterObject()
            )
        else:
            self.get_iterator().reset()

        return self

    def __next__(self) -> int:
        if self.get_iterator().previous() < len(self):
            self.get_iterator().increment()
            return self.get_iterator().previous()
        else:
            raise StopIteration

    def __len__(self) -> int:
        return len(
            self.get_tokens()
        )
