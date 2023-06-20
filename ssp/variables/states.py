from ssp.variables \
    import get_zero


def is_int_zero(
        value: int
) -> bool:
    return value == get_zero()
