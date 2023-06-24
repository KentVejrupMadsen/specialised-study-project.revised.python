#!/usr/bin/env python
from ssp.persistence                \
    import                          \
    CategoryMapStream,              \
    raise_category_already_exist,   \
    CounterObject


class DataSetMapStream:
    def __init__(self):
        self.name: str | None = None
        self.categories: list = []

        self.selection_counter: CounterObject | None = None

    def __del__(self):
        del                         \
            self.name,              \
            self.categories,        \
            self.selection_counter

    def get_selection_counter(self) -> CounterObject:
        if self.selection_counter is None:
            self.set_selection_counter(
                CounterObject()
            )

        return self.selection_counter

    def set_selection_counter(
            self,
            value: CounterObject
    ) -> None:
        self.selection_counter = value

    def __len__(self):
        return len(
            self.categories
        )

    def get_name(self) -> str | None:
        return self.name

    def set_name(
            self,
            value: str
    ):
        self.name = value

    def get_categories(self) -> list:
        return self.categories

    def set_categories(
            self,
            value: list
    ) -> None:
        self.categories = value

    def create(
            self,
            category_name: str
    ) -> CategoryMapStream:
        if self.has_category(
            category_name
        ):
            raise_category_already_exist()

        new_map = CategoryMapStream(
            category_name
        )

        self.categories.append(
            new_map
        )

        return new_map

    def retrieve(
            self,
            index: int
    ) -> CategoryMapStream:
        return self.categories[index]

    def remove(
            self,
            index: int
    ) -> None:
        self.categories.pop(
            index
        )

    def remove_by_name(
            self,
            value: str
    ):
        index_to_remove: int | None = None

        for index in iter(self):
            cm = self.retrieve(index)

            if cm.get_name() == value:
                index_to_remove = index

        if self.is_variable_not_none(
                index_to_remove
        ):
            self.remove(
                index_to_remove
            )

    def is_variable_none(
            self,
            value
    ) -> bool:
        return value is None

    def is_variable_not_none(
            self,
            value
    ) -> bool:
        return not self.is_variable_none(value)

    def has_category(
            self,
            category_name: str
    ) -> bool:
        for index in iter(self):
            category = self.retrieve(
                index
            )

            if hash(category) == hash(category_name):
                if category.get_name() == category_name:
                    return True

        return False

    def __iter__(self):
        self.selection_counter: CounterObject()
        return self

    def __next__(self):
        self.get_selection_counter().increment()

        next_step: int = int(self.get_selection_counter())

        if next_step <= len(self):
            return int(
                self.get_selection_counter()
            )
        else:
            raise StopIteration
