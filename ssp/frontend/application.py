#!/usr/bin/env python
from ssp.frontend       \
    import Controller


class Application:
    def __init__(self):
        self.controller = Controller()

    def __del__(self):
        del self.controller

    def initialise(self):
        self.get_controller().initialise()

    def execute(self):
        self.get_controller().execute()

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
