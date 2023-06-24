#!/usr/bin/env python
zero: int   = 0
one: int    = 1
two: int    = 2
three: int  = 3
four: int   = 4
five: int   = 5
six: int    = 6
seven: int  = 7
eight: int  = 8
nine: int   = 9

ascii_number_range_start: int = ord('0')
ascii_number_range_end: int = ord('9')


def get_ascii_number_range_start() -> int:
    global ascii_number_range_start
    return ascii_number_range_start


def get_ascii_number_range_end() -> int:
    global ascii_number_range_end
    return ascii_number_range_end


def get_zero() -> int:
    global zero
    return zero


def get_one() -> int:
    global one
    return one


def get_two() -> int:
    global two
    return two


def get_three() -> int:
    global three
    return three


def get_four() -> int:
    global four
    return four


def get_five() -> int:
    global five
    return five


def get_six() -> int:
    global six
    return six


def get_seven() -> int:
    global seven
    return seven


def get_eight() -> int:
    global eight
    return eight


def get_nine() -> int:
    global nine
    return nine
