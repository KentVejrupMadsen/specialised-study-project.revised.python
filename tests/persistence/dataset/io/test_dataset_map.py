from ssp.persistence    \
    import              \
    DataSetMap,         \
    DataSetMapBuilder

from ssp.frontend.environment \
    import Environment

from os.path \
    import join


def test_build_dataset() -> None:
    env = Environment()

    dmb = DataSetMapBuilder(
        join(
            env.get_path_to_dataset(),
            'training'
        )
    )

    dataset = dmb.run()

    print(
        'test build path: ',
        dmb.get_location()
    )

    assert isinstance(
        dataset,
        DataSetMap
    )


def test_build_dataset_for_test() -> None:
    env = Environment()

    dmb = DataSetMapBuilder(
        join(env.get_path_to_dataset(), 'test')
    )

    dataset = dmb.run()

    print('test build path: ', dmb.get_location())

    assert isinstance(
        dataset,
        DataSetMap
    )

def test_dataset_map_on_insert() -> None:
    dm = DataSetMap()

    label: str = 'training'
    s = dm.create(label)

    assert s.get_name() == label


def test_dataset_map_has_element() -> None:
    dm = DataSetMap()
    label: str = 'label_c'

    dm.create('test_a')
    dm.create('test_b')
    dm.create(label)
    dm.create('test_d')
    dm.create('test_e')
    dm.create('test_f')
    dm.create('test_g')

    has: bool = dm.has_category(label)
    assert has


def test_dataset_map_do_not_have_element() -> None:
    dm = DataSetMap()

    label: str = 'abcef'

    dm.create('ajasdnj')
    dm.create('læmasflæ')
    dm.create('kfdsafa')
    dm.create('legre')
    dm.create('nehgte')
    dm.create('asdqwe')

    has: bool = dm.has_category(label)
    assert not has


def test_dataset_map_remove() -> None:
    dm = DataSetMap()
    label: str = 'label_c'

    dm.create('test_a')
    dm.create('test_b')
    dm.create(label)
    dm.create('test_d')
    dm.create('test_e')
    dm.create('test_f')
    dm.create('test_g')

    dm.remove_by_name(
        label
    )

    has: bool = dm.has_category(label)
    assert not has

