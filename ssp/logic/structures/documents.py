#!/usr/bin/env python
from ssp.logic              \
    import BagOfWords

from ssp.logic.objects      \
    import                  \
    DocumentToken

from HardenedSteel.objects  \
    import CounterObject

from HardenedSteel.facades  \
    import is_integer_zero

from HardenedSteel.globals  \
    import get_integer_zero


class Document(
    BagOfWords
):
    def __init__(self):
        super().__init__()
        self.iterator: CounterObject | None = None
        self.tokens: list | None = None

    def __del__(self):
        super().__del__()
        del                 \
            self.tokens,    \
            self.iterator

    def __repr__(self) -> str:
        return str(
            dict(
                {
                    'tokens': self.get_tokens()
                }
            )
        )

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
            is_integer_zero(
                len(self)
            )
        )

    def is_iterator_none(self) -> bool:
        return self.iterator is None

    def is_document_token_in_set(
        self,
        is_in_set: DocumentToken
    ) -> bool:
        for index in iter(self):
            selected_token: DocumentToken = self.get_token_by_index(index)
            if is_in_set == selected_token:
                return True
        return False

    def exist_string_as_token_in_set(
        self,
        value: str
    ) -> bool:
        for index in iter(self):
            element = self.get_token_by_index(index)
            if element == value:
                return True
        return False

    def increase_token_counter(
        self,
        token: str
    ):
        for index in iter(self):
            selected = self.get_token_by_index(index)
            if selected == token:
                selected.increment_of_counter()

    def on_event_found_token(
            self,
            token: str
    ) -> None:
        if not self.is_empty():
            if self.exist_string_as_token_in_set(token):
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

    def insert_token(
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
        self.insert_token(
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
