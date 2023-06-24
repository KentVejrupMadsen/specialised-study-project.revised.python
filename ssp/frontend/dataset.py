#!/usr/bin/env python
from ssp.frontend       \
    import              \
    CounterObject,      \
    join,               \
    get_zero

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

        self.complete: bool = False

        self.store: list | None = None
        self.selection: CounterObject = CounterObject()

        self.initialise()

    def __del__(self):
        del                         \
            self.path_to_dataset,   \
            self.categories,        \
            self.complete,          \
            self.store,             \
            self.selection

    def reset_selection(self) -> None:
        self.selection.reset()

    def get_selection(self) -> int:
        return int(
            self.selection
        )

    def next_selection(self) -> None:
        self.selection.increment()

    def previous_selection(self) -> None:
        self.selection.decrement()

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

    def initialise(self) -> None:
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
    ) -> None:
        builder: DataSetMapBuilder = DataSetMapBuilder(
            full_path
        )

        self.get_store().append(
            builder.run()
        )

    def remove_at(
            self,
            position: int
    ) -> None:
        self.get_store().pop(
            position
        )

    def stream(self) -> None:
        selected: DataSetMapStream = self.currently_selected_map()
        self.stream_dataset_map(
            selected
        )

        self.next_selection()
        if self.is_position_at_end():
            self.set_is_complete(
                True
            )

    def stream_dataset_map(
            self,
            dsm: DataSetMapStream
    ) -> None:
        print(
            dsm.get_name()
        )

    def is_position_at_beginning(self) -> bool:
        return self.is_at_beginning(
            self.get_selection()
        )

    def is_position_at_end(self) -> bool:
        return self.is_at_end(
            self.get_selection()
        )

    def is_at_beginning(
            self,
            position: int
    ) -> bool:
        return position == get_zero()

    def is_at_end(
            self,
            position: int
    ) -> bool:
        return position == len(self)

    def currently_selected_map(self) -> DataSetMapStream:
        return self.retrieve_map(
            self.get_selection()
        )

    def retrieve_map(
            self,
            value: int
    ) -> DataSetMapStream:
        return self.get_store()[value]

    def map(self) -> bool:
        return not self.is_complete()

    def is_running(self) -> bool:
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

    def is_in_range(
            self,
            position: int
    ) -> bool:
        return position < len(
            self.get_store()
        )

    def is_position_within_range(self) -> bool:
        return self.is_in_range(
            self.get_selection()
        )

    def __len__(self) -> int:
        if self.is_store_none():
            return get_zero()

        return len(
            self.store
        )

    def __iter__(self):
        self.reset_selection()
        return self

    def __next__(self) -> int:
        self.next_selection()

        if self.is_position_within_range():
            return self.get_selection()
        else:
            raise StopIteration
