from ssp \
    import on_entry_call

is_debugging_entry: bool = False


def test_run_application() -> None:
    global is_debugging_entry
    if is_debugging_entry:
        on_entry_call()
