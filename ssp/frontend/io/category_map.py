from ssp.frontend.io \
    import DatasetDocument


class CategoryMap:
    def __init__(
            self,
            name: str
    ):
        self.name: str = name
        self.documents: list = []
        self.hash: int | None = None

    def __hash__(self) -> int:
        return self.get_hash()

    def set_hash(
            self,
            value: int
    ) -> None:
        self.hash = value

    def get_hash(self) -> int:
        if self.hash is None:
            self.update_hash()

        return self.hash

    def update_hash(self):
        self.set_hash(
            hash(
                self.get_name()
            )
        )

    def __del__(self):
        del \
            self.name, \
            self.documents

    def __len__(self) -> int:
        return int(self)

    def __int__(self) -> int:
        return self.get_number_of_document()

    def __str__(self):
        return self.name

    def insert(
            self,
            location: str
    ) -> None:
        self.documents.append(
            DatasetDocument(
                location
            )
        )

    def retrieve(
            self,
            index: int
    ) -> DatasetDocument:
        return self.documents[index]

    def remove(
            self,
            index: int
    ) -> None:
        documents: list = self.documents
        documents.pop(
            index
        )

    def get_name(self) -> str:
        return self.name

    def set_name(
            self,
            value: str
    ) -> None:
        self.name = value
        self.update_hash()

    def get_documents(
            self
    ) -> list:
        return self.documents

    def set_documents(
            self,
            documents: list
    ) -> None:
        self.documents = documents

    def get_number_of_document(self) -> int:
        return len(
            self.documents
        )
