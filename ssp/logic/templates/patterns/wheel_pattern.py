#!/usr/bin/env python
from abc                    \
    import                  \
    ABC,                    \
    abstractmethod

from HardenedSteel.objects  \
    import CounterObject


class WheelPattern(ABC):
    def __init__(self):
        self.position: None | CounterObject = None

    def __del__(self):
        del self.position

    def forward_selection(self):
        self.get_position_counter().increment()

    def backward_selection(self):
        self.get_position_counter().decrement()

    def set_selection(
        self,
        value: int
    ):
        self.get_position_counter().set_value(
            value
        )

    @abstractmethod
    def is_at_beginning(self) -> bool:
        raise NotImplemented

    @abstractmethod
    def is_at_end(self) -> bool:
        raise NotImplemented

    def place_position_at_end(self):
        self.get_position_counter().set_value(
            len(self)
        )

    def place_position_at_beginning(self):
        self.get_position_counter().reset()

    def initiate_backward_selection(self):
        if self.is_at_beginning():
            self.get_position_counter().set_value(
                len(self)
            )
        else:
            self.backward_selection()

    def initiate_forward_selection(self):
        if self.is_at_end():
            self.get_position_counter().reset()
        else:
            self.forward_selection()

    def get_position(self) -> int:
        return self.get_position_counter().get_value()

    def get_position_counter(self) -> CounterObject:
        if self.is_position_counter_none():
            self.set_position_counter(
                CounterObject()
            )

        return self.position

    def set_position_counter(
            self,
            value: CounterObject
    ) -> None:
        self.position = value

    def is_position_counter_none(self) -> bool:
        return self.position is None

    def __int__(self) -> int:
        return self.get_position()

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplemented
