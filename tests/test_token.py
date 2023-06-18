#!/usr/bin/env python
# Import of packages
from ssp.dataset.tokens \
    import \
    TokenWord, \
    DocumentToken, \
    CategoryToken


# Test
def test_word() -> None:
    label = 'label'
    word = TokenWord(label)
    assert str(word) == label


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
