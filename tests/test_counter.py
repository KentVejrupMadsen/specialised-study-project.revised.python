from ssp.dataset \
    import CounterObject


def test_counter_increase():
    cobj = CounterObject()
    cobj.increment()

    assert cobj.get_value() == 1


def test_counter_decrease():
    cobj = CounterObject()
    cobj.decrement()

    assert cobj.get_value() == -1

