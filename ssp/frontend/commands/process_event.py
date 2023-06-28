from ssp.frontend.commands \
    import Command


class ProcessEvent:
    def __init__(self):
        self.command: Command | None = None

    def __del__(self):
        del self.command

    def is_command_none(self) -> bool:
        return self.command is None

    def get_command(self) -> Command:
        return self.command

    def set_command(
            self,
            value: Command
    ) -> None:
        self.command = value
