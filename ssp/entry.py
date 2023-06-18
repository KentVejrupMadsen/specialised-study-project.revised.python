#!/usr/bin/env python
from ssp.variables \
    import get_entry_main_label

from ssp \
    import Application


def on_entry_call():
    app = Application()
    app.run()


# calling main function
if __name__ == get_entry_main_label():
    on_entry_call()
