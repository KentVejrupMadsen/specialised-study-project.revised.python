from tests \
    import get_location_of_script


def test_path() -> None:
    location = get_location_of_script()
    print(location)
    assert not(location is None)
