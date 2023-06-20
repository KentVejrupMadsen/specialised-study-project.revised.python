#!/usr/bin/env python
from ssp.variables \
    import get_zero

from ssp.logic.structures.factories \
    import TokenWord


class TokenFactory:
    def __init__(self):
        self.corpus: list | None = None
        self.size_of_corpus: int = 0

    def __del__(self):
        del \
            self.corpus, \
            self.size_of_corpus

    def get_size_of_corpus(self) -> int:
        return self.size_of_corpus

    def set_size_of_corpus(
            self,
            value: int
    ) -> None:
        self.size_of_corpus = value

    def calculate_size_of_corpus(self) -> None:
        self.set_size_of_corpus(
            len(
                self.corpus
            )
        )

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
    ) -> None | TokenWord:
        self.__initialise__()

        created_object = TokenWord(
            value
        )

        self.corpus.append(
            created_object
        )

        self.calculate_size_of_corpus()

        return created_object

    def search_for_token(
            self,
            search_value: str
    ) -> TokenWord | None:
        self.__initialise__()

        if self.is_corpus_empty():
            return None

        for index in self.corpus_range():
            token: TokenWord = self.retrieve_at(
                index
            )

            if token.same_as_by_string(
                    search_value
            ):
                return token

        return None

    def delete(
            self,
            token_value: str
    ) -> None:
        self.__initialise__()

        if self.is_corpus_empty():
            return None

        delete_position: int | None = None

        for index in self.corpus_range():
            currently_selected_token: TokenWord = self.retrieve_at(
                index
            )

            if currently_selected_token.same_as_by_string(
                    token_value
            ):
                delete_position = index
                break

        if not (delete_position is None):
            self.corpus.pop(
                delete_position
            )
            self.calculate_size_of_corpus()

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
        return self.size_of_corpus

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
