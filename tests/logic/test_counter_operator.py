from tests \
    import \
    CounterObject, \
    get_zero, \
    get_one, \
    get_two


def test_counter_add_integer() -> None:
    counter = CounterObject(
        get_zero()
    )

    counter + get_one()

    assert counter.get_value() == get_one()


def test_counter_add_counter_object() -> None:
    counter_a = CounterObject(
        get_one()
    )

    counter_b = CounterObject(
        get_one()
    )

    result = counter_a + counter_b

    assert int(result) == get_two()
