from ssp.frontend.environment \
    import Environment

from tests \
    import DataSet


def test_dataset() -> None:
    print('dataset')

    environment_setup = Environment()

    ds = DataSet(
        environment_setup.get_path_to_dataset(),
        environment_setup.get_categories()
    )

    while ds.map():
        ds.stream()

    assert isinstance(ds, DataSet)
