from abc \
    import ABC


class FunctionClass(ABC):
    def __init__(self):
        self.result = None

    def execute(self):
        pass

    def get_result(self) -> None | float:
        return self.result

    def set_result(
            self,
            value: float | None
    ) -> None:
        self.result = value
