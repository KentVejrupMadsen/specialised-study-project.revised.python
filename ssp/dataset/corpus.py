from os.path \
    import isdir


class DataSetCorpus:
    def __init__(
            self,
            dataset_location: str
    ):
        self.path_to_dataset: str = dataset_location

    def get_dataset_location(self) -> str:
        return self.path_to_dataset

    def set_dataset_location(
            self,
            value: str
    ) -> None:
        self.path_to_dataset = value

    def exist_dataset_location(self) -> bool:
        return isdir(
            self.path_to_dataset
        )
