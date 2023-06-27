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

from ssp.globals                                            \
    import                                                  \
    get_ascii_number_range_start,                           \
    get_ascii_number_range_end

from ssp.persistence.exceptions                             \
    import                                                  \
    raise_category_already_exist,                           \
    raise_location_not_found,                               \
    raise_file_not_found

from ssp.persistence.dataset_document                       \
    import DatasetDocumentStream

from ssp.persistence.category_map                           \
    import CategoryMapStream

from ssp.persistence.dataset_map                            \
    import DataSetMapStream

from ssp.persistence.dataset_map_builder                    \
    import DataSetMapBuilder

from ssp.persistence.loaders                                \
    import DocumentLoader
