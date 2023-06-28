#!/usr/bin/env python
from ssp.frontend                   \
    import                          \
    Environment,                    \
    WorkQueue,                      \
    get_is_debugging

from ssp.frontend.processes         \
    import DebuggableAction


class Controller:
    def __init__(self):
        self.environment = Environment()
        self.queue: WorkQueue | None = None

    def __del__(self):
        del                   \
            self.environment, \
            self.queue

    def initialise(self) -> None:
        if get_is_debugging():
            self.get_queue().insert_action_process(
                DebuggableAction(
                    self.get_queue()
                )
            )

        return None

    def execute(self) -> None:
        while not self.get_queue().is_complete():
            self.get_queue().cycle()
        return None

    def clean(self) -> None:
        return None

    def get_environment(self) -> Environment:
        return self.environment

    def set_environment(
            self,
            value: Environment
    ) -> None:
        self.environment = value

    def is_queue_none(self) -> bool:
        return self.queue is None

    def get_queue(self) -> WorkQueue:
        if self.is_queue_none():
            self.set_queue(
                WorkQueue()
            )
        return self.queue

    def set_queue(
            self,
            value: WorkQueue
    ) -> None:
        if value.is_parent_none():
            value.set_parent(self)
        self.queue = value
