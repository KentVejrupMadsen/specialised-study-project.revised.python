#!/usr/bin/env python
from ssp.persistence            \
    import                      \
    DataSetMapStream,           \
    CategoryMapStream,          \
    basename,                   \
    listdir,                    \
    isdir,                      \
    join,                       \
    walk,                       \
    raise_location_not_found


class DataSetMapBuilder:
    def __init__(
            self,
            dataset_location: str
    ):
        self.location: str = dataset_location
        self.dataset: None | DataSetMapStream = None

        if not isdir(self.location):
            raise_location_not_found()

    def __del__(self):
        del self.location

    def run(self) -> DataSetMapStream:
        self.set_dataset(
            DataSetMapStream()
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
                cm: CategoryMapStream = self.get_dataset().create(entry)

                self.search_for_files(
                    cm,
                    full_path
                )

    def search_for_files(
            self,
            cm: CategoryMapStream,
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

    def get_dataset(self) -> DataSetMapStream | None:
        return self.dataset

    def set_dataset(
            self,
            value: DataSetMapStream | None
    ) -> None:
        self.dataset = value
