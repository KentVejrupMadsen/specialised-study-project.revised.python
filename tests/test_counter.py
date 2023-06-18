# Import of packages
from ssp.dataset \
    import CounterObject


# Test
def test_get() -> None:
    cobj = CounterObject(4, 1)

    assert \
        int(cobj) == 4 \
        and \
        cobj.get_move_size() == 1


def test_counter_increment() -> None:
    cobj = CounterObject()

    cobj.increment()

    assert int(cobj) == 1


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
    cobj = CounterObject(start_value=400)

    cobj.reset()

    assert int(cobj) == 0


def test_counter_zero() -> None:
    cobj = CounterObject(0, 1)

    assert cobj.is_zero()


def test_counter_not_zero() -> None:
    cobj = CounterObject(200, 1)

    assert not cobj.is_zero()





