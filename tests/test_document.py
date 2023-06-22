#!/usr/bin/env python
from ssp.persistence    \
    import              \
    DataSetMap,         \
    DataSetMapBuilder,  \
    CategoryMap,        \
    DatasetDocument

from ssp.frontend.environment   \
    import                      \
    get_dataset_categories,     \
    Environment

from os.path \
    import join


def test_of_documents() -> None:
    env = Environment()

    print()

    for dataset_category in get_dataset_categories():
        fullpath = join(
            env.get_path_to_dataset(),
            dataset_category
        )

        builder = DataSetMapBuilder(
            dataset_location=fullpath
        )

        dataset: DataSetMap = builder.run()

        for category in dataset.get_categories():
            selected_category: CategoryMap = category

            for document in selected_category.get_documents():
                selected_document: DatasetDocument = document

                while selected_document.is_not_loaded():
                    selected_document.load_line()

                selected_document.close()

