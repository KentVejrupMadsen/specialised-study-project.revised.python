from random \
    import randint

from ssp.frontend.io \
    import DatasetDocument

from tests.frontend.dataset.io \
    import retrieve_files


def test_document() -> None:
    files = retrieve_files()
    length: int = len(files) - 1

    random_index = randint(
        0,
        length
    )
    extracted_from_set = files[random_index]

    document = DatasetDocument(extracted_from_set)

    print()
    print(repr(document))

    assert isinstance(
        document,
        DatasetDocument
    )
