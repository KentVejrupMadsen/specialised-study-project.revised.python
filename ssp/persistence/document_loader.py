from ssp.persistence \
    import DatasetDocumentStream


class DocumentLoader:
    def __init__(
            self,
            dataset_document: DatasetDocumentStream
    ):
        self.stream: DatasetDocumentStream = dataset_document

    def __del__(self):
        del self.stream

    def load(self) -> None:
        stream: DatasetDocumentStream = self.stream

        stream.set_is_to_normalise(
            True
        )

        while not stream.is_loaded():
            line: str = stream.load_line()

        stream.close()
