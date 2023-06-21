from ssp.frontend.io.dataset_map \
    import DataSetMap


class DataSet:
    def __init__(
            self,
            location_to_dataset: str,
            categories: list
    ):
        self.path_to_dataset: str = location_to_dataset
        self.categories: list = categories

        self.complete: bool = False

        self._map = DataSetMap()

    def __del__(self):
        del \
            self.path_to_dataset, \
            self.categories

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

    def get_map(self) -> DataSetMap:
        return self._map

    def set_map(
            self,
            value: DataSetMap
    ) -> None:
        self._map = value
