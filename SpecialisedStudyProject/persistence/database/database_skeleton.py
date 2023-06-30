from abc            \
    import          \
    ABC,            \
    abstractmethod


class DatabaseTemplate(ABC):
    def __init__(
        self,
        database_handler
    ):
        self.handler = database_handler

    def __del__(
        self
    ):
        del self.handler

    def is_handler_none(
        self
    ) -> bool:
        return self.handler is None

    def is_handler_instantiated(
        self
    ) -> bool:
        return not self.is_handler_none()

    def get_handler(
        self
    ):
        return self.handler

    def set_handler(
        self,
        value
    ):
        self.handler = value

    @abstractmethod
    def get_cursor(self):
        raise NotImplemented

