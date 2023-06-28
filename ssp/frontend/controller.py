#!/usr/bin/env python
from ssp.frontend                   \
    import                          \
    Environment


class Controller:
    def __init__(self):
        self.environment = Environment()

    def __del__(self):
        del                   \
            self.environment

    def initialise(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def get_environment(self) -> Environment:
        return self.environment

    def set_environment(
            self,
            value: Environment
    ) -> None:
        self.environment = value

