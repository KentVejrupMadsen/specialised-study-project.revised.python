#!/usr/bin/env python
from ssp.persistence                    \
    import                              \
    DatasetDocumentStream


class CategoryMapStream:
    def __init__(
            self,
            name: str
    ):
        from ssp.builders.events import CategoryEvent
        self.name: str = name
        self.documents: list = []
        self.hash: int | None = None

        self.event: None | CategoryEvent = None

    def get_event(self):
        return self.event

    def set_event(
            self,
            value
    ) -> None:
        self.event = value

    def is_event_none(self) -> bool:
        return self.event is None

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
        del                     \
            self.name,          \
            self.documents,     \
            self.hash

    def __len__(self) -> int:
        return int(
            self
        )

    def __int__(self) -> int:
        return self.get_number_of_document()

    def __str__(self):
        return self.name

    def insert(
            self,
            location: str
    ) -> None:
        created_document = DatasetDocumentStream(
            location
        )

        self.documents.append(
            created_document
        )

    def is_location_in_set(
            self,
            location_path: str
    ) -> bool:
        location_path_hash: int = hash(location_path)

        for index in range(
            self.get_number_of_document()
        ):
            currently_selected_document: DatasetDocumentStream = self.retrieve(
                index
            )

            if hash(currently_selected_document) == location_path_hash:
                if currently_selected_document.get_location() == location_path:
                    return True

        return False

    def retrieve(
            self,
            index: int
    ) -> DatasetDocumentStream:
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
