from ssp.dataset.corpus \
    import DataSetCorpus


path_to_dataset: str = 'C:\\Workspace\\Codespace\\containers\\projects\\ssp.revised.python\\dataset\\Reuters21578\\dataset'


def test_dataset():
    global path_to_dataset
    dataset = DataSetCorpus(path_to_dataset)

    assert dataset.exist_dataset_location()
