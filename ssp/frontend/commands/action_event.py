from ssp.frontend.commands  \
    import                  \
    ProcessEvent,           \
    Command                 \

from multiprocessing        \
    import Process

from abc                    \
    import abstractmethod


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

        self.started: bool = False
        self.done: bool = False

        self.process: Process | None = None

    def __del__(self):
        super().__del__()
        del                 \
            self.options,   \
            self.done,      \
            self.started,   \
            self.process

    def get_process(self) -> Process | None:
        return self.process

    def set_process(
            self,
            value: Process
    ):
        self.process = value

    def is_process_none(self) -> bool:
        return self.process is None

    def bootstrap_process(self):
        if self.is_process_none():
            self.set_process(
                Process(
                    self.execute()
                )
            )

            self.get_process().run()

    @abstractmethod
    def execute(self):
        pass

    def is_started(self) -> bool:
        return self.started

    def set_is_started(
            self,
            value: bool
    ) -> None:
        self.started = value

    def is_done(self) -> bool:
        return self.done

    def set_is_done(
        self,
        value: bool
    ) -> None:
        self.done = value

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
