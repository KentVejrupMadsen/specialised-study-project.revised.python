#!/usr/bin/env python
from HardenedSteel.globals              \
    import get_integer_zero

ascii_number_range_start: int = ord(
    str(
        get_integer_zero()
    )
)
ascii_number_range_end: int = ord(
    str(
        9
    )
)


def get_ascii_number_range_start() -> int:
    global ascii_number_range_start
    return ascii_number_range_start


def get_ascii_number_range_end() -> int:
    global ascii_number_range_end
    return ascii_number_range_end
