from ssp.dataset.tokens \
    import TokenWord

from ssp.variables \
    import get_zero


class TokenFactory:
    def __init__(self):
        self.corpus: list | None = None

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
            token: str
    ):
        self.__initialise__()

        pass

    def get_corpus(self) -> list | None:
        return self.corpus

    def set_corpus(
            self,
            value: list | None
    ):
        self.corpus = value

    def __len__(self):
        self.__initialise__()
        return len(self.corpus)

    def __initialise__(self):
        if self.__corpus_is_none():
            self.set_corpus([])

    def __corpus_is_none(self):
        return self.get_corpus() is None


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