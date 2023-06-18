from ssp.dataset.tokens \
    import \
    TokenWord, \
    DocumentToken, \
    CategoryToken


def test_word():
    label = 'label'
    word = TokenWord(label)
    assert str(word) == label


def test_document_token():
    label = 'test_a'
    word = DocumentToken(label)

    word.increment()
    word.increment()

    assert \
        str(word.get_word()) == label \
        and \
        word.get_counter().get_value() == 2
