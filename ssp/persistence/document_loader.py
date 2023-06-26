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

    def load(self):
        pass