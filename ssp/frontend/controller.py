#!/usr/bin/env python
from ssp.frontend   \
    import          \
    Environment,    \
    DataSet


class Controller:
    def __init__(self):
        self.environment = Environment()
        self.dataset: DataSet | None = None

    def __del__(self):
        del                   \
            self.environment, \
            self.dataset

    def execute(self):
        pass

    def get_environment(self) -> Environment:
        return self.environment

    def set_environment(
            self,
            value: Environment
    ) -> None:
        self.environment = value

    def get_dataset(self) -> None | DataSet:
        return self.dataset

    def set_dataset(
            self,
            value: None | DataSet
    ) -> None:
        self.dataset = value
