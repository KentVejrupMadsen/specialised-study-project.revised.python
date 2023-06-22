#!/usr/bin/env python
from ssp.persistence \
    import \
    DataSetMap, \
    DataSetMapBuilder

from ssp.frontend.environment \
    import \
    get_dataset_categories, \
    Environment

from os.path \
    import join


def test_builder() -> None:
    env = Environment()

    for dataset_category in get_dataset_categories():
        fullpath = join(
            env.get_path_to_dataset(),
            dataset_category
        )

        builder = DataSetMapBuilder(
            dataset_location=fullpath
        )

        dataset: DataSetMap = builder.run()

        print(
            'build: ',
            dataset.get_name()
        )
