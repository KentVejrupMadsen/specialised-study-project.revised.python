from os.path \
    import \
    isdir, \
    join

from ssp.dataset \
    import CorpusSet

from ssp.variables \
    import \
    training_label, \
    test_label


class DataSetCorpus:
    def __init__(
            self,
            dataset_location: str
    ):
        self.path_to_dataset: str = dataset_location

        if not self.exist_dataset_location():
            raise Exception('dataset location path does not exist')

        path_to_training: str = join(
            self.path_to_dataset,
            training_label()
        )
        self.training: CorpusSet = CorpusSet(
            path_to_training,
            training_label()
        )

        path_to_test: str = join(
            self.path_to_dataset,
            test_label()
        )
        self.test: CorpusSet = CorpusSet(
            path_to_test,
            test_label()
        )

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
