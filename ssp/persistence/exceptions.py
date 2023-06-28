#!/usr/bin/env python
def raise_category_already_exist() -> None:
    raise Exception('category with the same name is already in the set')


def raise_location_not_found() -> None:
    raise Exception('used location does not exist')


def raise_file_not_found() -> None:
    raise Exception('file not found')

