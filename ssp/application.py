#!/usr/bin/env python
from ssp \
    import Controller


class Application:
    def __init__(self):
        self.controller = Controller()

    def initialise(self):
        pass

    def execute(self):
        pass

    def garbage_collection(self):
        pass

    def run(self):
        self.initialise()
        self.execute()
        self.garbage_collection()

    def get_controller(self) -> None | Controller:
        return self.controller

    def set_controller(
            self,
            value: Controller | None
    ):
        self.controller = value
