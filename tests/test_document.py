from ssp.logic.structures \
    import Document


def test_document() -> None:
    document: Document = Document()

    assert isinstance(
        document,
        Document
    )


def test_iterations() -> None:
    document: Document = Document()

    document.create_token('running')
    document.create_token('while')
    document.create_token('training')
    document.create_token('fitness')

    for i in iter(document):
        token = document.retrieve_token_at(i)

        assert isinstance(
            token.get_word(),
            str
        )


def test_exists_token() -> None:
    document: Document = Document()

    test_label: str = 'running'

    document.create_token(test_label)
    document.create_token('while')
    document.create_token('training')
    document.create_token('fitness')

    result: bool = document.exist_token_by(test_label)
    assert result
