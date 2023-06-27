from ssp.logic.templates    \
    import BagOfWords

from ssp.logic.structures   \
    import                  \
    DocumentToken,          \
    CounterObject

from HardenedSteel.globals  \
    import get_integer_zero


class Document(BagOfWords):
    def __init__(self):
        super().__init__()
        self.iterator: CounterObject | None = None
        self.tokens: list | None = None

    def __del__(self):
        super().__del__()
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

    def is_empty(self) -> bool:
        return bool(
            self.is_tokens_none()
            or
            len(self) == get_integer_zero()
        )

    def is_iterator_none(self) -> bool:
        return self.iterator is None

    def exist_token(
            self,
            value: DocumentToken
    ) -> bool:
        return False

    def exist_token_by_string(
            self,
            value: str
    ) -> bool:
        input_var_hash: int = hash(value)

        for index in iter(self):
            element = self.get_token_by_index(index)

            if input_var_hash == element.get_hash():
                if value == element.get_word():
                    return True

        return False

    def increase_token_counter(
            self,
            token: str
    ):
        hashed_token: int = hash(token)

        for index in iter(self):
            selected = self.get_token_by_index(index)

            if selected.get_hash() == hashed_token:
                if selected.get_word() == token:
                    selected.get_counter().increment()

    def on_event_found_token(
            self,
            token: str
    ) -> None:
        if not self.is_empty():
            if self.exist_token_by_string(token):
                self.increase_token_counter(token)
            else:
                self.create_token(
                    token
                )
        else:
            self.create_token(
                token
            )

    def exist_token_by(
            self,
            name: str
    ) -> bool:
        hashed_label: int = hash(name)

        for index in iter(self):
            token = self.get_token_by_index(index)

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
        self.get_tokens().remove(
            index
        )

    def get_token_by_index(
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

        if self.get_iterator().previous() < len(self):
            return self.get_iterator().previous()
        else:
            raise StopIteration

    def __len__(self) -> int:
        if self.is_tokens_none():
            return get_integer_zero()

        return len(
            self.tokens
        )
