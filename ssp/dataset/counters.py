#!/usr/bin/env python
def zero() -> int:
    return 0


def one() -> int:
    return 1


class CounterObject:
    def __init__(
            self,
            start_value: int = zero(),
            move_by: int = one()
    ):
        self.value: int = start_value
        self.move: int = move_by

    def __del__(self):
        del \
            self.value, \
            self.move

    def reset(self):
        self.set_value(
            zero()
        )

    def get_move_size(self) -> int:
        return self.move

    def set_move_size(
            self,
            value: int
    ) -> None:
        self.move = value

    def get_value(self) -> int:
        return self.value

    def set_value(
            self,
            value: int
    ) -> None:
        self.value = value

    def increase(
            self,
            by_size: int
    ) -> None:
        self.set_value(
            self.value
            +
            by_size
        )

    def increment(self):
        self.increase(
            self.get_move_size()
        )

    def decrease(
            self,
            by_size: int
    ) -> None:
        self.set_value(
            self.value
            -
            by_size
        )

    def decrement(self):
        self.decrease(
            self.get_move_size()
        )

    def is_zero(self) -> bool:
        return self.get_value() == zero()

    def __str__(self) -> str:
        return str(
            self.get_value()
        )

    def __int__(self) -> int:
        return self.get_value()
