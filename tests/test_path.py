from tests \
    import get_location_of_script, get_location_of_repository, get_location_of_dataset

from os.path import isdir


def test_path() -> None:
    location = get_location_of_script()
    assert not(location is None) and isdir(location)


def test_repository() -> None:
    location = get_location_of_repository()
    assert not(location is None) and isdir(location)


def test_dataset() -> None:
    location = get_location_of_dataset()
    assert not(location is None) and isdir(location)
