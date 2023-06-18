#!/usr/bin/env python
from ssp.dataset.tokens \
    import TokenWord

from ssp.variables \
    import get_zero


class TokenFactory:
    def __init__(self):
        self.corpus: list | None = None

    def retrieve_at(
            self,
            index: int
    ) -> TokenWord:
        return self.corpus[index]

    def corpus_range(self):
        return range(
            len(
                self
            )
        )

    def insert(
            self,
            value: str
    ) -> None:
        self.__initialise__()

        created_object = TokenWord(
            value
        )

        self.corpus.append(
            created_object
        )

    def search_for_token(
            self,
            search_value: str
    ) -> TokenWord | None:
        self.__initialise__()

        if self.is_corpus_empty():
            return None

        for index in self.corpus_range():
            token: TokenWord = self.retrieve_at(index)

            if str(token) == search_value:
                return token

    def delete(
            self,
            token_value: str
    ) -> None:
        self.__initialise__()

        if self.is_corpus_empty():
            return None

        delete_position: int | None = None

        for index in self.corpus_range():
            token: TokenWord = self.retrieve_at(index)

            if str(token) == token_value:
                delete_position = index
                break

        if not (delete_position is None):
            self.corpus.pop(
                delete_position
            )

    def is_corpus_empty(self) -> bool:
        return \
            self.is_corpus_none() \
            or \
            len(self) == get_zero()

    def is_corpus_none(self) -> bool:
        return self.corpus is None

    def get_corpus(self) -> list | None:
        return self.corpus

    def empty_corpus(self) -> None:
        self.set_corpus(
            []
        )

    def set_corpus(
            self,
            value: list | None
    ):
        self.corpus = value

    def __len__(self):
        self.__initialise__()

        return len(
            self.corpus
        )

    def __initialise__(self):
        if self.is_corpus_none():
            self.empty_corpus()


singleton: TokenFactory | None = None


def set_singleton_token_factory(
        value: TokenFactory
) -> None:
    global singleton
    singleton = value


def get_singleton_token_factory() -> TokenFactory:
    global singleton

    if singleton is None:
        set_singleton_token_factory(
            TokenFactory()
        )

    return singleton
