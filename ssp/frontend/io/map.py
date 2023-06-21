class CategoryMap:
    def __init__(
            self,
            name: str
    ):
        self.name: str = name
        self.documents: list = []

    def __del__(self):
        del \
            self.name, \
            self.documents

    def get_name(self) -> str:
        return self.name

    def set_name(
            self,
            value: str
    ) -> None:
        self.name = value

    def get_documents(
            self
    ) -> list:
        return self.documents

    def set_documents(
            self,
            documents: list
    ) -> None:
        self.documents = documents
