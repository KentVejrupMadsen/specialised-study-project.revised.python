from os.path \
    import isfile


class Category:
    def __init__(
            self,
            name: str,
            category_directory_location: str
    ):
        self.name: str = name
        self.category_directory_location: str = category_directory_location
        self.files_in_category: list = []

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
            self.files_in_category
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
