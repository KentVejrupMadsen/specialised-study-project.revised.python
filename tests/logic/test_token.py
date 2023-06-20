#!/usr/bin/env python
# Import of packages
from tests \
    import \
    TokenWord, \
    DocumentToken, \
    CategoryToken


# Test
def test_word() -> None:
    label = 'label'
    word = TokenWord(label)
    assert str(word) == label


def test_work_length() -> None:
    label: str = 'tokenised'
    word = TokenWord(label)
    assert len(word) == len(label)


def test_document_label() -> None:
    test_label: str = 'abc_test'
    word = DocumentToken(test_label)

    assert str(word) == test_label


def test_document_integer() -> None:
    test_label = 'jsa'

    word = DocumentToken(test_label)

    word.increment()
    word.increment()

    assert int(word) == 2


def test_category_integer() -> None:
    test_label = 'sra'

    word = CategoryToken(test_label)

    word.increment()
    word.increment()

    assert int(word) == 2


def test_category_label() -> None:
    test_label = 'cba_test'
    word = CategoryToken(test_label)

    assert str(word) == test_label


def test_document_token() -> None:
    label = 'test_a'
    word = DocumentToken(label)

    word.increment()
    word.increment()

    assert \
        str(word.get_word()) == label \
        and \
        int(word.get_counter()) == 2


def test_category_token() -> None:
    label = 'test_b'
    word = CategoryToken(label)

    word.increment()
    word.increment()

    assert \
        str(word.get_word() == label) \
        and \
        int(word.get_counter()) == 2
