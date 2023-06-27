#!/usr/bin/env python
environment_dataset_location: str   = 'dataset_location_at'
environment_labels: str             = 'dataset_labels'


def get_environment_dataset_location() -> str:
    global environment_dataset_location
    return environment_dataset_location


def set_environment_dataset_location(
        value: str
) -> None:
    global environment_dataset_location
    environment_dataset_location = value


def get_environment_dataset_labels() -> str:
    global environment_labels
    return environment_labels


def set_environment_labels(
        value: str
) -> None:
    global environment_labels
    environment_labels = value
