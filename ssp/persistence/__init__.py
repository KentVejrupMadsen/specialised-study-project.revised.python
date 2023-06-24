#!/usr/bin/env python
from io                                                     \
    import TextIOBase

from os                                                     \
    import                                                  \
    listdir,                                                \
    walk

from os.path                                                \
    import                                                  \
    isfile,                                                 \
    isdir,                                                  \
    basename,                                               \
    join


from HardenedSteel.facades.texts.characters.ranges          \
    import                                                  \
    ascii_uppercase_begin,                                  \
    ascii_uppercase_end

from HardenedSteel.facades.texts.characters.ranges          \
    import                                                  \
    ascii_lowercase_begin,                                  \
    ascii_lowercase_end

from ssp.persistence.dataset_document                       \
    import DatasetDocument

from ssp.persistence.category_map                           \
    import CategoryMap

from ssp.persistence.dataset_map                            \
    import DataSetMap

from ssp.persistence.dataset_map_builder                    \
    import DataSetMapBuilder
