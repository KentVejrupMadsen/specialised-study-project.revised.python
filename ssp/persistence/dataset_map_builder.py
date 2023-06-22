#!/usr/bin/env python
from ssp.persistence        \
    import                  \
    DataSetMap,             \
    CategoryMap,            \
    basename,               \
    listdir,                \
    isdir,                  \
    join,                   \
    walk


class DataSetMapBuilder:
    def __init__(
            self,
            dataset_location: str
    ):
        self.location: str = dataset_location
        self.dataset: None | DataSetMap = None

        if not isdir(self.location):
            raise Exception('location not found')

    def __del__(self):
        del self.location

    def run(self) -> DataSetMap:
        self.set_dataset(
            DataSetMap()
        )

        self.get_dataset().set_name(
            basename(
                self.get_location()
            )
        )

        self.generate_categories()

        return self.get_dataset()

    def generate_categories(self):
        found_items: list = listdir(
            self.get_location()
        )

        for entry in found_items:
            full_path: str = join(
                self.location,
                entry
            )

            if isdir(full_path):
                cm: CategoryMap = self.get_dataset().create(entry)

                self.search_for_files(
                    cm,
                    full_path
                )

    def search_for_files(
            self,
            cm: CategoryMap,
            full_path
    ):
        for root, dirs, files in walk(
                full_path,
                topdown=False
        ):
            for selected_file in files:
                path_to_file: str = join(
                    root,
                    selected_file
                )

                cm.insert(
                    path_to_file
                )

    def get_location(self) -> str:
        return self.location

    def set_location(
            self,
            value: str
    ) -> None:
        self.location = value

    def get_dataset(self) -> DataSetMap | None:
        return self.dataset

    def set_dataset(
            self,
            value: DataSetMap | None
    ) -> None:
        self.dataset = value
