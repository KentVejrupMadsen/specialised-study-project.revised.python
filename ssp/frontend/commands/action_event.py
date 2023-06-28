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

        self.options: list | None = None

    def __del__(self):
        super().__del__()
        del self.options

    def is_options_none(self) -> bool:
        return self.options is None

    def get_options(self) -> list:
        if self.is_options_none():
            self.set_options(
                list()
            )
            
        return self.options

    def set_options(
            self,
            value: list
    ) -> None:
        self.options = value
