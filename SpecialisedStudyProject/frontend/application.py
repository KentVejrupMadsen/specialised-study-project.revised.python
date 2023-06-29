from SpecialisedStudyProject.frontend   \
    import SystemController


class Application:
    def __init__(self):
        self.controller: SystemController | None = None

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

    def get_controller(self) -> SystemController:
        if self.is_controller_none():
            self.set_controller(
                SystemController()
            )
        return self.controller

    def set_controller(
            self,
            value: SystemController
    ) -> None:
        self.controller = value

    def is_controller_none(self) -> bool:
        return self.controller is None
