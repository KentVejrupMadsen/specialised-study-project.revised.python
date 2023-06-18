from tests \
    import get_zero

from ssp.logic.structures.factories \
    import \
    get_singleton_token_factory


def test_token_factory() -> None:
    assert not (
        get_singleton_token_factory() is None
    )


def test_insert_to_factory() -> None:
    factory = get_singleton_token_factory()

    factory.insert('abc')
    factory.insert('cda')
    factory.insert('tra')
    factory.insert('sed')

    assert not len(factory) == get_zero()
