#!/usr/bin/env python
from ssp.variables \
    import \
    get_zero,\
    get_one, \
    is_int_zero


def is_instance_of_counter_object(value) -> bool:
    return isinstance(
        value,
        CounterObject
    )


def is_instance_of_integer(value) -> bool:
    return isinstance(
        value,
        int
    )


class CounterObject:
    def __init__(
            self,
            start_value: int = get_zero(),
            move_by: int = get_one()
    ):
        self.value: int = start_value
        self.move: int = move_by

    def __del__(self):
        del \
            self.value, \
            self.move

    def __add__(
            self,
            other
    ):
        if is_instance_of_counter_object(
            other
        ):
            o_co: CounterObject = other
            self.increase(
                o_co.get_value()
            )

        if is_instance_of_integer(
            other
        ):
            o_int: int = other
            self.increase(
                o_int
            )

        return self

    def __eq__(self, other) -> bool:
        rVal: bool = False

        return rVal

    def reset(self):
        self.set_value(
            get_zero()
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
        return is_int_zero(
            self.get_value()
        )

    def __str__(self) -> str:
        return str(
            self.get_value()
        )

    def __int__(self) -> int:
        return self.get_value()
