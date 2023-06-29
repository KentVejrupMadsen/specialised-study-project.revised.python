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

    def __del__(self) -> None:
        del self.token

