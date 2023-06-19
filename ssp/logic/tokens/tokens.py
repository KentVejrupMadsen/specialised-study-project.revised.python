#!/usr/bin/env python
class TokenWord:
    def __init__(
            self,
            word: str
    ):
        self.word: str = word

    def get_word(self) -> str:
        return self.word

    def set_word(
            self,
            value: str
    ) -> None:
        self.word = value

    def __str__(self) -> str:
        return str(
            self.get_word()
        )

    def __len__(self) -> int:
        return len(
            self.get_word()
        )

