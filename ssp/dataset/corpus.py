#!/usr/bin/env python
from os.path \
    import \
    isdir, \
    join

from ssp.dataset \
    import CorpusSet

from ssp.variables \
    import \
    get_training_label, \
    get_test_label

from ssp.dataset \
    import CorpusPreprocessor


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
            get_training_label()
        )
        self.training: CorpusSet = CorpusSet(
            path_to_training,
            get_training_label()
        )

        path_to_test: str = join(
            self.path_to_dataset,
            get_test_label()
        )
        self.test: CorpusSet = CorpusSet(
            path_to_test,
            get_test_label()
        )

        self.preprocessor = CorpusPreprocessor()

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

    def get_preprocessor(self) -> CorpusPreprocessor:
        return self.preprocessor

    def set_preprocessor(
            self,
            with_value: CorpusPreprocessor
    ) -> None:
        self.preprocessor = with_value

    def get_test(self) -> CorpusSet:
        return self.test

    def get_training(self) -> CorpusSet:
        return self.training

    def set_training(
            self,
            value: CorpusSet
    ) -> None:
        self.training = value

    def set_test(
            self,
            value: CorpusSet
    ) -> None:
        self.test = value
