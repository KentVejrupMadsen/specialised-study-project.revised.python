#!/usr/bin/env python
from ssp.adhoc \
    import environ

from ssp.logic.structures \
    import CounterObject

from ssp.variables \
    import \
    get_zero, \
    get_one

from ssp.logic.structures.tokens.factories \
    import \
    get_singleton_token_factory, \
    TokenFactory

from ssp.logic.structures.tokens \
    import \
    TokenWord, \
    CategoryToken, \
    DocumentToken

from ssp.logic.dataset \
    import DataSetCorpus

from ssp.variables \
    import get_environment_dataset_location

from ssp \
    import on_entry_call


