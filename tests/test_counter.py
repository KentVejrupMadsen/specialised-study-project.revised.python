#!/usr/bin/env python
# Import of packages
from tests \
    import CounterObject, get_zero, get_one


# Test
def test_get() -> None:
    cobj = CounterObject(4, get_one())

    assert \
        int(cobj) == 4 \
        and \
        cobj.get_move_size() == get_one()


def test_counter_increment() -> None:
    cobj = CounterObject()

    cobj.increment()

    assert int(cobj) == get_one()


def test_counter_increase() -> None:
    cobj = CounterObject()

    cobj.increase(3)
    cobj.increase(2)

    assert int(cobj) == 5


def test_counter_decrement() -> None:
    cobj = CounterObject()

    cobj.decrement()

    assert int(cobj) == -1


def test_counter_decrease() -> None:
    cobj = CounterObject()

    cobj.decrease(2)
    cobj.decrease(2)

    assert int(cobj) == -4


def test_counter_reset() -> None:
    cobj = CounterObject(
        start_value = 400
    )

    cobj.reset()

    assert int(cobj) == get_zero()


def test_counter_zero() -> None:
    cobj = CounterObject(
        get_zero(),
        get_one()
    )

    assert cobj.is_zero()


def test_counter_not_zero() -> None:
    cobj = CounterObject(
        200,
        get_one()
    )

    assert not cobj.is_zero()





