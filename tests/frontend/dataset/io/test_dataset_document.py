from random \
    import randint

from ssp.persistence \
    import DatasetDocument

from tests.frontend.dataset.io \
    import retrieve_files


def retrieve_random_file() -> DatasetDocument:
    files = retrieve_files()
    length: int = len(files) - 1

    random_index = randint(
        0,
        length
    )
    extracted_from_set = files[random_index]

    document = DatasetDocument(extracted_from_set)

    return document


def test_document() -> None:
    document = retrieve_random_file()

    print()
    print(repr(document))

    assert isinstance(
        document,
        DatasetDocument
    )


def test_document_open_and_read_file() -> None:
    document = retrieve_random_file()

    document.open()

    while not (document.is_loaded()):
        line: str = document.load_line()

        print(
            'example line: ',
            line
        )

        assert isinstance(line, str)

    document.close()

    assert isinstance(
        document,
        DatasetDocument
    )

