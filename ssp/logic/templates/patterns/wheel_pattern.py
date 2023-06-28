#!/usr/bin/env python
from abc                    \
    import                  \
    ABC,                    \
    abstractmethod

from HardenedSteel.objects  \
    import CounterObject


class WheelPattern(
    ABC
):
    def __init__(self):
        self.position: None | CounterObject = None
        self.iterator: None | CounterObject = None
        self.increment: bool = True

    def __del__(self):
        del                 \
            self.position,  \
            self.increment, \
            self.iterator

    def get_iterator(self) -> CounterObject:
        if self.is_iterator_none():
            self.set_iterator(
                CounterObject()
            )

        return self.iterator

    def is_iterator_none(self) -> bool:
        return self.iterator is None

    def set_iterator(
            self,
            value: CounterObject
    ) -> None:
        self.iterator = value

    def is_to_increment(self) -> bool:
        return self.increment

    def set_is_to_increment(
            self,
            value: bool
    ) -> None:
        self.increment = value

    def move_position(self):
        if self.is_to_increment():
            self.initiate_moving_position_forward()
        else:
            self.initiate_moving_position_backward()

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

    def __iter__(self):
        self.get_iterator().reset()
        return self

    def __next__(self):
        self.get_iterator().increment()

        index_position: int = self.get_iterator().previous()

        is_within_begin_range: bool = index_position >= 0
        is_within_end_range: bool = index_position < len(self)

        if is_within_begin_range and is_within_end_range:
            return index_position
        else:
            raise StopIteration
