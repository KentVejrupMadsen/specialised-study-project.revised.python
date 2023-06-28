from abc            \
    import          \
    ABC,            \
    abstractmethod


class OnFire(ABC):
    def __init__(self):
        self.handler = None
        self.debug: bool = False

    def __del__(self):
        del                 \
            self.handler,   \
            self.debug

    def get_is_debugging(self) -> bool:
        return self.debug

    def set_is_debugging(
            self,
            value: bool
    ) -> None:
        self.debug = value

    def is_not_debugging(self) -> bool:
        return not self.debug

    def debug_by_default(self) -> None:
        self.set_is_debugging(
            True
        )

    @abstractmethod
    def found_token(
            self,
            value: str
    ):
        pass

    def is_handler_none(self) -> bool:
        return self.handler is None

    def get_handler(self):
        return self.handler

    def set_handler(
            self,
            value
    ) -> None:
        self.handler = value
