from tests \
    import get_export_singleton


def test_environment() -> None:
    assert not (get_export_singleton() is None)
