from tests              \
    import              \
    get_is_debugging,   \
    set_is_debugging

from ssp \
    import on_entry_call


def test_run_application() -> None:
    set_is_debugging(
        True
    )

    if get_is_debugging():
        on_entry_call()
