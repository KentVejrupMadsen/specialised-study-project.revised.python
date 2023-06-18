#!/usr/bin/env python
training_label: str = 'training'
test_label: str = 'test'


def get_training_label() -> str:
    global training_label
    return training_label


def get_test_label() -> str:
    global test_label
    return test_label
