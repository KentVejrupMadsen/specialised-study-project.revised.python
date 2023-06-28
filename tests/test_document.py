from ssp.logic.structures.documents \
    import Document

from HardenedSteel.facades \
    import generate_label_by_size


def test_of_logic_document():
    doc = Document()

    find: str = 'abcef'

    doc.create_token('test')
    doc.create_token('abcd')
    doc.create_token('laoef')
    doc.create_token(find)

    found = doc.exist_token_by_string(
        find
    )

    assert found


def test_of_logic_document_tokens():
    doc = Document()

    for i in range(200):
        label_generated: str = generate_label_by_size(20)
        doc.create_token(label_generated)

    for index in iter(doc):
        token = doc.get_token_by_index(
            index
        )
        print(repr(token))

    assert isinstance(
        doc,
        Document
    )
