from ssp.logic.structures   \
    import                  \
    DocumentToken,          \
    CounterObject

from HardenedSteel.globals  \
    import get_integer_zero


class Document:
    def __init__(self):
        self.iterator: CounterObject | None = None
        self.tokens: list | None = None

    def __del__(self):
        del                 \
            self.tokens,    \
            self.iterator

    def get_iterator(self) -> CounterObject:
        if self.is_iterator_none():
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

    def exist_token(
            self,
            value: DocumentToken
    ) -> bool:

        return False

    def exist_token_by(
            self,
            name: str
    ) -> bool:
        hashed_label: int = hash(name)

        for index in iter(self):
            token = self.retrieve_token_at(index)

            if hashed_label == token.get_hash():
                if name == token.get_word():
                    return True

        return False

    def add_token(
            self,
            value: DocumentToken
    ) -> None:
        self.get_tokens().append(
            value
        )

    def create_token(
            self,
            value: str
    ) -> None:
        self.add_token(
            DocumentToken(
                value
            )
        )

    def remove_token_at(
            self,
            index: int
    ):
        pass

    def retrieve_token_at(
            self,
            index: int
    ) -> DocumentToken:
        return self.get_tokens()[index]

    def get_tokens(self) -> list:
        if self.is_tokens_none():
            self.tokens = list()

        return self.tokens

    def set_tokens(
            self,
            value: list
    ) -> None:
        self.tokens = value

    def is_tokens_none(self) -> bool:
        return self.tokens is None

    def __iter__(self):
        if self.is_iterator_none():
            self.set_iterator(
                CounterObject()
            )
        else:
            self.get_iterator().reset()

        return self

    def __next__(self) -> int:
        self.get_iterator().increment()

        if int(self.get_iterator()) < len(self.get_tokens()):
            return self.get_iterator().previous()
        else:
            raise StopIteration

    def __int__(self):
        if self.is_tokens_none():
            return get_integer_zero()

        return len(
            self.tokens
        )
