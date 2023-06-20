from tests import DocumentToken


def test_create_doc_token() -> None:
    token = DocumentToken(word='lorem', instances=1)

    assert not(token is None)
