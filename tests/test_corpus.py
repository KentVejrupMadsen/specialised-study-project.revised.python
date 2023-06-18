# Import of packages
from os \
    import environ

from ssp.dataset.corpus \
    import DataSetCorpus

from ssp.variables \
    import get_environment_dataset_location

# Global Variables
environment_dataset_pointer = environ[
    get_environment_dataset_location()
]

dataset: None | DataSetCorpus = None

# Setup of workflow for test
if not (environment_dataset_pointer is None):
    path_to_dataset: str = environment_dataset_pointer


# Accessors
def get_dataset_location_path() -> str:
    global path_to_dataset
    return path_to_dataset


def get_dataset() -> DataSetCorpus:
    global dataset

    if dataset is None:
        dataset = DataSetCorpus(
            get_dataset_location_path()
        )

    return dataset


# Test
def test_dataset() -> None:
    ds = get_dataset()

    assert ds.exist_dataset_location()
