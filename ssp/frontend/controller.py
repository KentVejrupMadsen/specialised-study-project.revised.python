#!/usr/bin/env python
from ssp.frontend                   \
    import                          \
    Environment,                    \
    WorkQueue


class Controller:
    def __init__(self):
        self.environment = Environment()
        self.queue: WorkQueue | None = WorkQueue()

    def __del__(self):
        del                   \
            self.environment, \
            self.queue

    def initialise(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def clean(self) -> None:
        pass

    def get_environment(self) -> Environment:
        return self.environment

    def set_environment(
            self,
            value: Environment
    ) -> None:
        self.environment = value

    def get_queue(self) -> WorkQueue:
        return self.queue

    def set_queue(
            self,
            value: WorkQueue
    ) -> None:
        self.queue = value
