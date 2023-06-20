from tests \
    import get_export_singleton


def test_environment() -> None:
    assert not (get_export_singleton() is None)


def test_environment_labels() -> None:
    singleton = get_export_singleton()
    singleton.get_labels()


def test_environment_dataset_location() -> None:
    singleton = get_export_singleton()
    singleton.get_dataset_location()
