#!/usr/bin/env python
class Command:
    def __init__(
            self,
            queue: str
    ):
        self.queue_command = queue

    def __del__(self):
        del self.queue_command

    def get_queue_command(self) -> str:
        return self.queue_command

    def set_queue_command(
            self,
            value: str
    ) -> None:
        self.queue_command = value
