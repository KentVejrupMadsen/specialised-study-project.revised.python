from ssp.frontend.environments \
    import EnvironmentExports

from ssp                        \
    import                      \
    get_dataset_categories,     \
    get_location_of_dataset,    \
    get_location_of_repository, \
    get_location_of_script


class Environment:
    def __init__(self):
        self.exports: EnvironmentExports | None = EnvironmentExports()
        self.categories: list | None = None

        self.path_to_dataset: str | None = None
        self.path_to_repository: str | None = None
        self.path_to_script: str | None = None

    def __del__(self):
        del                         \
            self.exports,           \
            self.categories,        \
            self.path_to_dataset,   \
            self.path_to_script,    \
            self.path_to_repository

    def get_categories(self) -> list:
        if self.categories is None:
            categories = self.get_exports().get_labels()

            if categories is None:
                categories = get_dataset_categories()
            else:
                categories = categories.split(',')

            self.set_categories(categories)

        return self.categories

    def set_categories(
            self,
            value: list
    ):
        self.categories = value

    def get_path_to_dataset(self) -> str:
        if self.get_path_to_dataset() is None:
            env_var = self.get_exports().get_dataset_location()

            if not (env_var is None):
                self.set_path_to_dataset(
                    env_var
                )
            else:
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
        return self.path_to_repository

    def set_path_to_repository(
            self,
            value: str
    ) -> None:
        self.path_to_repository = value

    def get_path_to_script(self) -> str:
        return self.path_to_script

    def set_path_to_script(
            self,
            value: str
    ) -> None:
        self.path_to_script = value

    def get_exports(self) -> EnvironmentExports | None:
        return self.exports

    def set_exports(
            self,
            value: EnvironmentExports
    ) -> None:
        self.exports = value
