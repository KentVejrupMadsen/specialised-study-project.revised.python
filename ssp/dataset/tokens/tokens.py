class TokenWord:
    def __init__(
            self,
            word: str
    ):
        self.word = word

    def get_word(self) -> str:
        return self.word

    def set_word(
            self,
            value: str
    ) -> None:
        self.word = value

    def __str__(self):
        return self.get_word()

