from ssp.dataset.corpus \
    import DataSetCorpus


path_to_dataset: str = 'C:\\Workspace\\Codespace\\containers\\projects\\ssp.revised.python\\dataset\\Reuters21578\\dataset'


def get_dataset_location_path() -> str:
    global path_to_dataset
    return path_to_dataset


def test_dataset():
    dataset = DataSetCorpus(
        get_dataset_location_path()
    )

    assert dataset.exist_dataset_location()
