from abc            \
    import          \
    ABC,            \
    abstractmethod


class Word(ABC):
    def __init__(
        self,
        value: str
    ) -> None:
        self.token: str = value
        self.length: int | None = None

    def is_length_none(self) -> bool:
        return self.length is None

    def get_length(self) -> int:
        if self.is_length_none():
            self.set_length(
                len(
                    self.token
                )
            )

        return self.length

    def set_length(
        self,
        value: int
    ) -> None:
        self.length = value

    def __del__(self) -> None:
        del             \
            self.token, \
            self.length

    def __len__(self) -> int:
        return self.get_length()
