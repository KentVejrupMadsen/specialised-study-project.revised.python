#!/usr/bin/env python
from ssp.frontend                   \
    import                          \
    Environment,                    \
    WorkQueue

from ssp.frontend.processes         \
    import DebuggableAction


is_debugging: bool = True


def get_is_debugging() -> bool:
    global is_debugging
    return is_debugging


class Controller:
    def __init__(self):
        self.environment = Environment()
        self.queue: WorkQueue | None = WorkQueue()

    def __del__(self):
        del                   \
            self.environment, \
            self.queue

    def initialise(self) -> None:
        if get_is_debugging():
            self.get_queue().insert_action_process(
                DebuggableAction()
            )

    def execute(self) -> None:
        while not self.get_queue().is_complete():
            self.get_queue().cycle()

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
