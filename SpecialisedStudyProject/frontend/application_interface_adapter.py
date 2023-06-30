class ApplicationInterfaceAdapter:
    def __init__(
        self,
        controller=None
    ):
        self.controller = controller

    def __del__(self):
        del self.controller

    def get_controller(self):
        from SpecialisedStudyProject.frontend \
            import SystemController

        controller: SystemController = self.controller
        return controller

    def set_controller(
        self,
        value
    ):
        from SpecialisedStudyProject.frontend \
            import SystemController

        controller: SystemController = value
        self.controller = controller

    def is_controller_none(self):
        return self.controller is None
