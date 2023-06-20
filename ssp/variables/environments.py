#!/usr/bin/env python
environment_dataset_location: str = 'dataset_location_at'


def get_environment_dataset_location() -> str:
    global environment_dataset_location
    return environment_dataset_location


def set_environment_dataset_location(
        value: str
) -> None:
    global environment_dataset_location
    environment_dataset_location = value


