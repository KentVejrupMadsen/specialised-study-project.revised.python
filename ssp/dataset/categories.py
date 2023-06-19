#!/usr/bin/env python
from os.path \
    import isfile

from ssp.dataset \
    import Document

from ssp.variables \
    import is_int_zero


class Category:
    def __init__(
            self,
            name: str,
            category_directory_location: str
    ):
        self.name: str = name
        self.category_directory_location: str = category_directory_location
        self.files_in_category: list = []
        self.documents: list = []

    def load(self):
        if not is_int_zero(
                self.number_of_files_in_category()
        ):
            for file_location \
                    in self.files_in_category:

                doc = Document(
                    location=file_location
                )
                self.add_document(doc)

    def add_document(
            self,
            document: Document
    ):
        self.get_documents().append(
            document
        )

    def number_of_files_in_category(self) -> int:
        return len(self.files_in_category)

    def get_documents(self) -> list:
        return self.documents

    def set_documents(
            self,
            value: list
    ):
        self.documents = value

    def get_name(self) -> str:
        return self.name

    def set_name(
            self,
            value: str
    ):
        self.name = value

    def get_category_directory_location(self) -> str:
        return self.category_directory_location

    def set_category_directory_location(
            self,
            value: str
    ):
        self.category_directory_location = value

    def size_of_category(self) -> int:
        return len(
            self.documents
        )

    def insert_file(
            self,
            located_at: str
    ):
        if isfile(located_at):
            self.files_in_category.append(
                located_at
            )

    def get_files(self):
        return self.files_in_category

    def set_files(
            self,
            value: list
    ):
        self.files_in_category = value
