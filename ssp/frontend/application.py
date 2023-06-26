#!/usr/bin/env python
from ssp.frontend       \
    import Controller


class Application:
    def __init__(self):
        self.controller = Controller()

    def __del__(self):
        del self.controller

    def initialise(self) -> None:
        self.get_controller().initialise()

    def execute(self) -> None:
        self.get_controller().execute()

    def garbage_collection(self) -> None:
        pass

    def get_controller(self) -> None | Controller:
        return self.controller

    def set_controller(
            self,
            value: Controller | None
    ) -> None:
        self.controller = value

    def run(self) -> None:
        self.initialise()
        self.execute()
        self.garbage_collection()
