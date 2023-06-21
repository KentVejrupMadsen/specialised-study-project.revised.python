from ssp.frontend.io \
    import CategoryMap


class DataSetMap:
    def __init__(self):
        self.categories: list = []

    def __del__(self):
        del self.categories

    def __len__(self):
        return len(self.categories)

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
    ) -> CategoryMap:
        new_map = CategoryMap(
            category_name
        )

        self.categories.append(
            new_map
        )

        return new_map

    def retrieve(
            self,
            index: int
    ) -> CategoryMap:
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

        for index in self.map_range():
            cm = self.retrieve(index)

            if cm.get_name() == value:
                index_to_remove = index

        if not(index_to_remove is None):
            self.remove(
                index_to_remove
            )

    def has_category(
            self,
            category_name: str
    ) -> bool:
        for index in self.map_range():
            category = self.retrieve(
                index
            )

            if hash(category) == hash(category_name):
                if category.get_name() == category_name:
                    return True

        return False

    def map_range(self):
        return range(
            len(self)
        )
