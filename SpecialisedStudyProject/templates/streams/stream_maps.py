from abc                                                \
    import                                              \
    ABC,                                                \
    abstractmethod

from HardenedSteel.globals                              \
    import                                              \
    get_integer_zero

from SpecialisedStudyProject.templates.streams.events   \
    import StreamMapOnSizeChange


class StreamMap(
    ABC
):
    def __init__(self):
        self.stream: list | None = None

        self.event_on_size_change: StreamMapOnSizeChange | None = None

    def __del__(self):
        del                             \
            self.stream,                \
            self.event_on_size_change

    def hint_event_size_change(self):
        event = self.get_event_on_size_change()
        event.hint()

    def trigger_event_size_change(self):
        event = self.get_event_on_size_change()
        event.on_trigger()

    def get_event_on_size_change(self):
        if self.is_event_on_size_change_empty():
            self.set_event_on_size_change(
                StreamMapOnSizeChange(
                    self
                )
            )

        return self.event_on_size_change

    def set_event_on_size_change(
        self,
        value
    ) -> None:
        event: StreamMapOnSizeChange = value
        self.event_on_size_change = event

    def is_event_on_size_change_empty(self) -> bool:
        return self.event_on_size_change is None

    def clear(self) -> None:
        self.hint_event_size_change()
        self.get_stream().clear()

    @abstractmethod
    def is_instance_token(
        self,
        value
    ) -> bool:
        raise NotImplemented

    def insert(
        self,
        value
    ):
        self.hint_event_size_change()
        self.get_stream().append(
            value
        )

    def insert_at(
        self,
        index: int,
        value_object
    ) -> None:
        self.hint_event_size_change()
        self.get_stream().insert(
            index,
            value_object
        )

    def remove_at(
        self,
        index: int
    ) -> None:
        self.hint_event_size_change()
        self.get_stream().pop(
            index
        )

    def retrieve_at(
        self,
        index: int
    ):
        self.trigger_event_size_change()
        return self.get_stream()[
            index
        ]

    def get_stream(self) -> list:
        self.trigger_event_size_change()
        if self.is_stream_none():
            self.set_stream(
                list()
            )
        return self.stream

    def set_stream(
        self,
        value: list
    ) -> None:
        self.hint_event_size_change()
        self.stream = value

    def is_stream_none(self) -> bool:
        return self.stream is None

    def is_stream_empty(self) -> bool:
        if self.is_stream_none():
            return True

        self.trigger_event_size_change()
        return len(
            self
        ) == get_integer_zero()

    def __len__(self):
        self.trigger_event_size_change()
        return len(
            self.get_stream()
        )
