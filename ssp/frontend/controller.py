#!/usr/bin/env python
from ssp.frontend.environment \
    import Environment


class Controller:
    def __init__(self):
        self.environment = Environment()

    def get_environment(self) -> Environment:
        return self.environment

    def set_environment(
            self,
            value: Environment
    ) -> None:
        self.environment = value
