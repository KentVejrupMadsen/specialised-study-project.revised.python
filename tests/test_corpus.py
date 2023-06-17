from os \
    import environ

from ssp.dataset.corpus \
    import DataSetCorpus


path_to_dataset: str = environ['dataset_location_at']


def get_dataset_location_path() -> str:
    global path_to_dataset
    return path_to_dataset


def test_dataset():
    dataset = DataSetCorpus(
        get_dataset_location_path()
    )

    assert dataset.exist_dataset_location()
