from ssp.logic.tokens \
    import \
    DocumentToken, \
    TokenWord

from ssp.variables \
    import is_int_zero

from ssp.logic.structures.factories \
    import \
    get_singleton_token_factory, \
    TokenFactory

class CorpusPreprocessor:
    def __init__(
            self,
            encoding: str = 'utf-8',
            normalise: bool = True
    ):
        self.encoding: str = encoding
        self.normalisation: bool = normalise

        self.token_set: list | None = None
        self.debugging: bool = True

        self.token_factory: TokenFactory = get_singleton_token_factory()

    def __del__(self):
        del                     \
            self.encoding,      \
            self.normalisation, \
            self.token_set

    def open_stream(self):
        self.initialise_token_set()

    def stream(
            self,
            input_stream: str
    ) -> None:
        tokens = input_stream.split()

        if not is_int_zero(
                len(
                    tokens
                )
        ):
            self.iterate_tokens_from_stream(
                tokens
            )

    def get_token_factory(self) -> TokenFactory:
        return self.token_factory

    def iterate_tokens_from_stream(
            self,
            tokens: list
    ):
        factory = self.get_token_factory()

        for token \
                in tokens:
            current_token: str = self.normalisation_of_token(
                token
            )

            search = factory.search_for_token(
                current_token
            )

            search_is_none: bool = search is None

            if search_is_none:
                search = factory.insert(
                    current_token
                )

                self.token_set.append(
                    DocumentToken(
                        word=search,
                        counter_value=1
                    )
                )

            if not search_is_none:
                self.search_in_list(
                    search
                )

    def get_token_by_index(self, index: int) -> DocumentToken:
        return self.get_token_set()[index]


    def search_in_list(
            self,
            word: TokenWord
    ):
        if not is_int_zero(
                len(
                    self.get_token_set()
                )
        ):
            is_found: bool = False

            for index in self.range_of_set():
                current_selection = self.get_token_by_index(
                    index=index
                )

                if current_selection.get_word() == word:
                    current_selection.increment()
                    is_found: bool = True
                    break

            if not is_found:
                self.token_set.append(
                    DocumentToken(
                        word=word,
                        counter_value=1
                    )
                )

        else:
            self.token_set.append(
                DocumentToken(
                    word=word,
                    counter_value=1
                )
            )


    def normalisation_of_token(
            self,
            token: str
    ):
        if self.is_to_normalise_tokens():
            return token.lower()

        return token

    def show_status(self):
        if self.is_debugging():
            pass

    def close_stream(self):
        self.show_status()
        self.reset_token_set()

    def is_to_normalise_tokens(self) -> bool:
        return self.normalisation

    def get_token_set(self) -> list | None:
        return self.token_set

    def set_token_set(
            self,
            value: list
    ) -> None:
        self.token_set = value

    def reset_token_set(self) -> None:
        self.token_set = None

    def initialise_token_set(self) -> None:
        self.token_set = []

    def is_token_set_none(self) -> bool:
        return self.token_set is None

    def is_debugging(self) -> bool:
        return self.debugging

    def set_is_debugging(
            self,
            value: bool
    ) -> None:
        self.debugging = value

    def __len__(self) -> int:
        if self.is_token_set_none():
            return 0

        return len(
            self.token_set
        )

    def range_of_set(self):
        return range(
            len(self)
        )