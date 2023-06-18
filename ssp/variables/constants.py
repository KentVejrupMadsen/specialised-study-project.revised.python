#!/usr/bin/env python
zero: int = 0
one: int = 1


def get_zero() -> int:
    global zero
    return zero


def get_one() -> int:
    global one
    return one
