#!/usr/bin/env python
from os.path \
    import join

from ssp.persistence    \
    import              \
    DataSetMapBuilder,  \
    DataSetMapStream


class DataSet:
    def __init__(
            self,
            location_to_dataset: str,
            categories: list
    ):
        self.path_to_dataset: str = location_to_dataset
        self.categories: list = categories

        self.complete: bool = True

        self.store: list | None = None

        self.initialise()

    def get_full_path(self) -> str:
        return self.path_to_dataset

    def set_full_path(
            self,
            value: str
    ) -> None:
        self.path_to_dataset = value

    def get_categories(self) -> list:
        return self.categories

    def set_categories(
            self,
            value: list
    ) -> None:
        self.categories = value

    def initialise(self):
        for category in self.categories:
            self.insert(
                join(
                    self.path_to_dataset,
                    category
                )
            )

    def insert(
            self,
            full_path: str
    ):
        builder: DataSetMapBuilder = DataSetMapBuilder(
            full_path
        )

        self.get_store().append(
            builder.run()
        )

    def __del__(self):
        del                         \
            self.path_to_dataset,   \
            self.categories,        \
            self.complete,          \
            self.store

    def stream(self):
        pass

    def map(self) -> bool:
        return not self.is_complete()

    def is_complete(self) -> bool:
        return self.complete

    def set_is_complete(
            self,
            value: bool
    ) -> None:
        self.complete = value

    def is_store_none(self) -> bool:
        return self.store is None

    def get_store(self) -> list | None:
        if self.is_store_none():
            self.set_store(
                list()
            )

        return self.store

    def set_store(
            self,
            value: list
    ) -> None:
        self.store = value
