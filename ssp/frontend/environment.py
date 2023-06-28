from ssp                            \
    import                          \
    get_dataset_categories,         \
    get_location_of_dataset,        \
    get_location_of_repository,     \
    get_location_of_script


class Environment:
    def __init__(self):
        self.categories: list | None = None

        self.path_to_dataset: str | None = None
        self.path_to_repository: str | None = None
        self.path_to_script: str | None = None

    def __del__(self):
        del                         \
            self.categories,        \
            self.path_to_dataset,   \
            self.path_to_script,    \
            self.path_to_repository

    def get_categories(self) -> list:
        if self.categories is None:
            self.set_categories(
                get_dataset_categories()
            )

        return self.categories

    def set_categories(
            self,
            value: list
    ) -> None:
        self.categories = value

    def get_path_to_dataset(self) -> str:
        if self.path_to_dataset is None:
            self.set_path_to_dataset(
                get_location_of_dataset()
            )

        return self.path_to_dataset

    def set_path_to_dataset(
            self,
            value: str
    ) -> None:
        self.path_to_dataset = value

    def get_path_to_repository(self) -> str:
        if self.path_to_repository is None:
            self.set_path_to_repository(
                get_location_of_repository()
            )

        return self.path_to_repository

    def set_path_to_repository(
            self,
            value: str
    ) -> None:
        self.path_to_repository = value

    def get_path_to_script(self) -> str:
        if self.path_to_script is None:
            self.set_path_to_script(
                get_location_of_script()
            )

        return self.path_to_script

    def set_path_to_script(
            self,
            value: str
    ) -> None:
        self.path_to_script = value
