from ssp \
    import Controller


class Application:
    def __init__(self):
        self.controller = Controller()

    def execute(self):
        pass

    def get_controller(self) -> None | Controller:
        return self.controller

    def set_controller(
            self,
            value: Controller | None
    ):
        self.controller = value
