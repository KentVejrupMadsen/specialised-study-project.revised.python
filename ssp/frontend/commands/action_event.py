from ssp.frontend.commands  \
    import                  \
    Command,                \
    ProcessEvent


class ActionProcess(ProcessEvent):
    def __init__(
            self,
            command_name: str
    ):
        super().__init__()
        self.set_command(
            Command(
                command_name
            )
        )

    def __del__(self):
        super().__del__()
