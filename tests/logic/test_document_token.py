from tests \
    import DocumentToken

from tests.strings import random_text


def test_create_doc_token() -> None:
    token = DocumentToken(
        word=random_text(25),
        instances=1
    )

    assert not(token is None)


def test_increase() -> None:
    token = DocumentToken(
        word=random_text(25),
        instances=1
    )

    token.get_counter().increment()
    token.get_counter().increment()

    assert int(token) == 3


def test_decrease() -> None:
    token = DocumentToken(
        word=random_text(25),
        instances=4
    )

    token.get_counter().decrement()
    token.get_counter().decrement()

    assert int(token) == 2


def test_retrieve_token() -> None:
    token = DocumentToken(word=random_text(5), instances=12)

    print({
        token.get_word(),
        token.get_hash(),
        int(token.get_counter())
    })
    assert isinstance(token.get_word(), str)
