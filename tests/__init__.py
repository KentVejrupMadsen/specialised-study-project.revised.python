#!/usr/bin/env python
from ssp.logic.structures \
    import \
    CounterObject, \
    Token, \
    DocumentToken, \
    CategoryToken

from ssp.variables  \
    import          \
    get_zero,       \
    get_one,        \
    get_two,        \
    get_three,      \
    get_four,       \
    get_five,       \
    get_six,        \
    get_seven,      \
    get_eight,      \
    get_nine

from ssp.variables  \
    import get_environment_dataset_location

from ssp                        \
    import                      \
    on_entry_call,              \
    get_location_of_script,     \
    get_location_of_repository, \
    get_location_of_dataset

from tests.globals \
    import get_generator \
    as get_random_generator
