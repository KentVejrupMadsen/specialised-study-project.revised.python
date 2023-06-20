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


def test_counter_equal_to_counter_object() -> None:
    counter_a = CounterObject(
        get_two()
    )
    counter_b = CounterObject(
        get_two()
    )

    assert counter_a == counter_b


def test_counter_equal_to_integer() -> None:
    counter_a = CounterObject(
        get_one()
    )
    assert counter_a == get_one()


def test_counter_substraction_by_integer() -> None:
    counter = CounterObject(get_two())
    result = counter - get_one()

    assert int(result) == get_one()


def test_counter_substraction_by_counter_object() -> None:
    counter_a = CounterObject(get_two())
    counter_b = CounterObject(get_two())

    result = counter_a - counter_a

    assert int(result) == get_zero()
