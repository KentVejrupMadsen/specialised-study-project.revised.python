from SpecialisedStudyProject.frontend   \
    import                              \
    SystemController,                   \
    ApplicationInterfaceAdapter


class Application:
    def __init__(
        self
    ):
        self.controller: SystemController | None = None
        self.adapter: ApplicationInterfaceAdapter | None = None

        self.is_workflow: bool = False
        self.is_to_continue: bool = True

    def __del__(
        self
    ):
        del                         \
            self.controller,        \
            self.adapter,           \
            self.is_to_continue,    \
            self.is_workflow

    def __bool__(self):
        return self.is_to_continue

    def get_is_to_continue(
        self
    ) -> bool:
        return self.is_to_continue

    def set_is_to_continue(
        self,
        value: bool
    ) -> None:
        self.is_to_continue = value

    def get_is_workflow(self) -> bool:
        return self.is_workflow

    def set_is_workflow(
        self,
        value: bool
    ) -> None:
        self.is_workflow = value

    def initialise(
        self
    ) -> None:
        pass

    def execute(
        self
    ) -> None:
        if self.get_is_workflow():
            self.workflow_execution()
        else:
            self.command_iteration()

    def workflow_execution(self):
        pass

    def command_iteration(self):
        while bool(self):
            pass

    def clean(
        self
    ) -> None:
        pass

    def run(
        self
    ) -> None:
        self.initialise()
        self.execute()
        self.clean()

    def get_controller(
        self
    ) -> SystemController:
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

    def get_adapter(self):
        if self.is_adapter_none():
            self.set_adapter(
                ApplicationInterfaceAdapter(
                    self.get_controller()
                )
            )

        return self.adapter

    def set_adapter(
        self,
        with_value: ApplicationInterfaceAdapter
    ) -> None:
        self.adapter = with_value

    def is_adapter_none(self) -> bool:
        return self.adapter is None
