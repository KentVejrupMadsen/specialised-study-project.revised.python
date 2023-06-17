from ssp.dataset \
    import CounterObject


def test_get():
    cobj = CounterObject(4, 1)
    assert \
        int(cobj) == 4 \
        and \
        cobj.get_move_size() == 1


def test_counter_increment():
    cobj = CounterObject()
    cobj.increment()

    assert int(cobj) == 1


def test_counter_increase():
    cobj = CounterObject()

    cobj.increase(3)
    cobj.increase(2)

    assert int(cobj) == 5


def test_counter_decrement():
    cobj = CounterObject()
    cobj.decrement()

    assert int(cobj) == -1


def test_counter_decrease():
    cobj = CounterObject()

    cobj.decrease(2)
    cobj.decrease(2)

    assert int(cobj) == -4


def test_counter_reset():
    cobj = CounterObject(start_value=400)
    cobj.reset()

    assert int(cobj) == 0
