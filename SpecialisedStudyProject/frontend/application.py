from frontend   \
    import Controller


class Application:
    def __init__(self):
        self.controller: Controller | None = None

    def __del__(self):
        del self.controller

    def initialise(self) -> None:
        pass

    def execute(self) -> None:
        pass

    def clean(self) -> None:
        pass

    def run(self) -> None:
        self.initialise()
        self.execute()
        self.clean()

    def get_controller(self) -> Controller:
        if self.is_controller_none():
            self.set_controller(
                Controller()
            )
        return self.controller

    def set_controller(
            self,
            value: Controller
    ) -> None:
        self.controller = value

    def is_controller_none(self) -> bool:
        return self.controller is None
