#!/usr/bin/env python
from ssp.logic.templates \
    import ABC, abstractmethod


class FunctionClass(ABC):
    def __init__(self):
        self.result = None

    @abstractmethod
    def compute(self) -> None:
        pass

    def get_result(self) -> None | float:
        return self.result

    def set_result(
            self,
            value: float | None
    ) -> None:
        self.result = value
