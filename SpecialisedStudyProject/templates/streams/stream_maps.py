from abc                                                \
    import                                              \
    ABC,                                                \
    abstractmethod

from HardenedSteel.facades                              \
    import is_integer_zero

from HardenedSteel.objects                              \
    import CounterObject

from SpecialisedStudyProject.templates.streams.events   \
    import StreamMapOnSizeChange


class StreamMap(
    ABC
):
    def __init__(
        self
    ):
        self.stream: list | None = None
        self.event_on_size_change: StreamMapOnSizeChange | None = None
        self.iterator: CounterObject | None = None
        self.length: int | None = None

    def __del__(
        self
    ):
        del                             \
            self.stream,                \
            self.event_on_size_change,  \
            self.iterator,              \
            self.length

    def __getitem__(
        self,
        index: int
    ):
        return self.get_stream()[
            index
        ]

    def __setitem__(
        self,
        index: int,
        value
    ):
        self.assign_to(
            index,
            value
        )

    def __int__(self):
        return int(
            self.get_iterator().previous()
        )

    def __len__(
        self
    ) -> int:
        self.trigger_event_size_change()
        return self.get_length()

    def __iter__(self):
        self.trigger_event_size_change()
        self.get_iterator().reset()
        return self

    def __next__(
        self
    ) -> int:
        self.get_iterator().increment()
        next_index_position: int = int(self)
        if next_index_position < len(self):
            return next_index_position
        else:
            raise StopIteration

    def __iadd__(
        self,
        other
    ):
        if self.is_instance_token(
            other
        ):
            self.insert(
                other
            )

        return self

    def assign_to(
        self,
        index: int,
        value
    ):
        if self.is_instance_token(
            value
        ):
            self.get_stream()[index] = value
        else:
            raise ValueError(
                'wrong type'
            )

    def is_length_none(self) -> bool:
        return self.length is None

    def refresh_length(self):
        self.set_length(
            len(
                self.get_stream()
            )
        )

    def get_length(
        self
    ) -> int:
        if self.is_length_none():
            self.refresh_length()

        return self.length

    def set_length(
        self,
        value: int
    ) -> None:
        self.length = value

    def get_iterator(
        self
    ) -> CounterObject:
        if self.is_iterator_none():
            self.set_iterator(
                CounterObject()
            )
        return self.iterator

    def set_iterator(
        self,
        value: CounterObject
    ) -> None:
        self.iterator = value

    def is_iterator_none(
        self
    ) -> bool:
        return self.iterator is None

    def hint_event_size_change(
        self
    ):
        event = self.get_event_on_size_change()
        event.hint()

    def trigger_event_size_change(
        self
    ):
        event = self.get_event_on_size_change()
        event.on_trigger()

    def get_event_on_size_change(
        self
    ):
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

    def is_event_on_size_change_empty(
        self
    ) -> bool:
        return self.event_on_size_change is None

    def clear(
        self
    ) -> None:
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

    def get_stream(
        self
    ) -> list:
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

    def is_stream_none(
        self
    ) -> bool:
        return self.stream is None

    def is_stream_empty(
        self
    ) -> bool:
        if self.is_stream_none():
            return True

        self.trigger_event_size_change()
        return is_integer_zero(
            len(self)
        )
