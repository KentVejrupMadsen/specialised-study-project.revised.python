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

    def move_position_forward(self):
        self.get_position_counter().increment()

    def move_position_backward(self):
        self.get_position_counter().decrement()

    def set_position(
        self,
        value: int
    ):
        self.get_position_counter().set_value(
            value
        )

    @abstractmethod
    def is_position_at_beginning(self) -> bool:
        raise NotImplemented

    @abstractmethod
    def is_position_at_end(self) -> bool:
        raise NotImplemented

    def place_position_at_end(self):
        self.get_position_counter().set_value(
            len(self)
        )

    def place_position_at_beginning(self):
        self.get_position_counter().reset()

    def initiate_moving_position_backward(self):
        if self.is_position_at_beginning():
            self.reset_position_to_end()
        else:
            self.move_position_backward()

    def initiate_moving_position_forward(self):
        if self.is_position_at_end():
            self.reset_position_to_start()
        else:
            self.move_position_forward()

    def get_position(self) -> int:
        return self.get_position_counter().get_value()

    def get_position_counter(self) -> CounterObject:
        if self.is_position_counter_none():
            self.set_position_counter(
                CounterObject()
            )

        return self.position

    def reset_position_to_start(self):
        self.get_position_counter().reset()

    def reset_position_to_end(self):
        self.get_position_counter().set_value(
            self.get_last_position()
        )

    def set_position_counter(
            self,
            value: CounterObject
    ) -> None:
        self.position = value

    def is_position_counter_none(self) -> bool:
        return self.position is None

    def __int__(self) -> int:
        return int(
            self.get_position()
        )

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplemented

    def get_last_position(self) -> int:
        return (
            len(self) - 1
        )
