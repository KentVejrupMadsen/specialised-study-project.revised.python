class CorpusPreprocessor:
    def __init__(
            self,
            encoding: str = 'utf-8',
            normalise: bool = False
    ):
        self.encoding: str = encoding
        self.normalisation: bool = normalise

        self.token_set: list | None = None

    def __del__(self):
        pass

    def open_stream(self):
        pass

    def stream(self) -> None:
        pass

    def close_stream(self):
        pass

    def get_token_set(self) -> list | None:
        return self.token_set

    def set_token_set(self, value: list) -> None:
        self.token_set = value

    def reset_token_set(self) -> None:
        self.token_set = None

    def is_token_set_none(self) -> bool:
        return self.token_set is None
