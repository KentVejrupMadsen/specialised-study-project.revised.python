#!/usr/bin/env python
training_label: str     = 'training'
test_label: str         = 'test'

entry_main_label: str   = '__main__'


def get_training_label() -> str:
    global training_label
    return training_label


def get_test_label() -> str:
    global test_label
    return test_label


def get_entry_main_label() -> str:
    global entry_main_label
    return entry_main_label
