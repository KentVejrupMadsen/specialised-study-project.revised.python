#!/usr/bin/env python
is_debugging: bool = True


def get_is_debugging() -> bool:
    global is_debugging
    return is_debugging


def set_is_debugging(
        value: bool
) -> None:
    global is_debugging
    is_debugging = value

