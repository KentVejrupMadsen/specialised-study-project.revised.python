#!/usr/bin/env python
from ssp.logic.dataset \
    import \
    CorpusPreprocessor, \
    raise_set_directory_does_not_exist, \
    Category, \
    isdir, \
    listdir, \
    join,\
    walk


class CorpusSet:
    def __init__(
            self,
            location: str,
            corpus_set: str,
            corpus_processor: CorpusPreprocessor = CorpusPreprocessor()
    ):
        self.location: str = location

        if not self.exist_location_path():
            raise_set_directory_does_not_exist()

        self.processor = corpus_processor

        self.corpus_set: str = corpus_set
        self.categories: list = []
        self.search()

    def get_categories(self) -> list:
        return self.categories

    def set_categories(
            self,
            values: list
    ):
        self.categories = values

    def exist_location_path(self) -> bool:
        return isdir(self.location)

    def get_location_path(self) -> str:
        return self.location

    def search(self):
        found_categories = listdir(
            self.get_location_path()
        )

        for category \
                in found_categories:
            full_path_to_category = join(
                self.get_location_path(),
                category
            )

            if isdir(
                full_path_to_category
            ):
                category = self.retrieve_files_in_category(
                    category=category,
                    at_category_location=full_path_to_category
                )

                category.load()

                self.get_categories().append(
                    category
                )

    def retrieve_files_in_category(
            self,
            category: str,
            at_category_location: str
    ):
        label = Category(
            name=category,
            category_directory_location=at_category_location,
            processor=self.processor
        )

        for root, dirs, files in walk(
            at_category_location,
            topdown=False
        ):
            for name in files:
                file_location = join(
                    root,
                    name
                )

                label.insert_file(
                    located_at=file_location
                )

        return label
