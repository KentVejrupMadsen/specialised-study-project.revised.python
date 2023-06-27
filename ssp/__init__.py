#!/usr/bin/env python
from os.path                    \
    import                      \
    isdir,                      \
    dirname,                    \
    pardir,                     \
    realpath,                   \
    join

from os                         \
    import listdir

from ssp.globals              \
    import get_entry_main_label

from ssp.setup                  \
    import                      \
    get_location_of_script,     \
    get_location_of_repository, \
    get_location_of_dataset,    \
    get_dataset_categories

from ssp.frontend               \
    import Application

from ssp.entry                  \
    import on_entry_call
