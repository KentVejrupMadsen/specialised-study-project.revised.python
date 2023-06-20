#!/usr/bin/env python
from ssp                    \
    import                  \
    get_entry_main_label,   \
    Application


def on_entry_call() -> None:
    app = Application()
    app.run()


# calling main function
if __name__ == get_entry_main_label():
    on_entry_call()
