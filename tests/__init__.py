#!/usr/bin/env python
from ssp.logic.structures \
    import CounterObject

from ssp.variables \
    import \
    get_zero, \
    get_one

from ssp.logic.tokens.factories \
    import \
    get_singleton_token_factory, \
    TokenFactory

from ssp.logic.tokens \
    import \
    TokenWord, \
    CategoryToken, \
    DocumentToken

from ssp.dataset.corpus \
    import DataSetCorpus

from ssp.variables \
    import get_environment_dataset_location


from ssp \
    import on_entry_call


