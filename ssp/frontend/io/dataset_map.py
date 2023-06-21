class DataSetMap:
    def __init__(self):
        self.categories: list = []

    def __del__(self):
        del self.categories

    def get_categories(self) -> list:
        return self.categories

    def set_categories(
            self,
            value: list
    ) -> None:
        self.categories = value
