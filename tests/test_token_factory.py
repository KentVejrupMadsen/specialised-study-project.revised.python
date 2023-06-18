#!/usr/bin/env python
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


def test_remove_at() -> None:
    factory = get_singleton_token_factory()

    label = 'to_be_removed'

    factory.insert(label)
    factory.delete(label)

    assert factory.search_for_token(label) is None


def test_search_for_token_in_factory() -> None:
    factory = get_singleton_token_factory()
    test_label = 'test_search'

    factory.insert(
        test_label
    )
    word = factory.search_for_token(
        test_label
    )

    assert str(word) == test_label


def test_list_dump() -> None:
    print('\nList Dump')

    list = get_singleton_token_factory().get_corpus()

    for e in list:
        print(
            '  -- token dump: ',
            str(e)
        )

    assert not(
            get_singleton_token_factory() is None
    )
