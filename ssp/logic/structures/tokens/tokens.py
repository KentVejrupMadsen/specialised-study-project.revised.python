#!/usr/bin/env python
class TokenWord:
    def __init__(
            self,
            word: str
    ):
        self.word: str = word
        self.hash: int | None = None

    def __del__(self):
        del \
            self.word, \
            self.hash

    def __hash__(self):
        return self.hash

    def same_as_by_string(
            self,
            value: str
    ) -> bool:
        return str(self.word) == value

    def same_as(
            self,
            value
    ):
        if is_instance_of_token_word(
            value
        ):
            return are_tokens_the_same(
                self,
                value
            )

    def set_hash(
            self,
            value: int
    ) -> None:
        self.hash = value

    def get_hash(self) -> int:
        if self.hash is None:
            self.set_hash(
                hash(
                    self.word
                )
            )

        return self.hash

    def get_word(
            self
    ) -> str:
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


def are_tokens_the_same(
        value_a: TokenWord,
        value_b: TokenWord
) -> bool:
    if value_a.get_hash() == value_b.get_hash():
        if value_a.get_word() == value_b.get_word():
            return True

    return False


def is_instance_of_token_word(
        input_object
) -> bool:
    return isinstance(
        input_object,
        TokenWord
    )
