from os \
    import environ

from ssp.dataset.corpus \
    import DataSetCorpus

from ssp.variables \
    import get_environment_dataset_location


environment_dataset_pointer = environ[
    get_environment_dataset_location()
]

if not (environment_dataset_pointer is None):
    path_to_dataset: str = environment_dataset_pointer


def get_dataset_location_path() -> str:
    global path_to_dataset
    return path_to_dataset


dataset: None | DataSetCorpus = None


def get_dataset() -> DataSetCorpus:
    global dataset

    if dataset is None:
        dataset = DataSetCorpus(
            get_dataset_location_path()
        )

    return dataset


def test_dataset():
    ds = get_dataset()

    assert ds.exist_dataset_location()
