from platform \
    import system

from os \
    import environ

from ssp.variables \
    import \
    get_environment_dataset_location, \
    get_environment_dataset_labels


class EnvironmentExports:
    def __init__(self):
        self.labels: None | str = None
        self.dataset_location: None | str = None
        self.environments: dict | None = None

    def get_environment_variables(self) -> dict | None:
        if self.environments is None:
            self.set_environment_variables(
                dict(environ)
            )

        return self.environments

    def set_environment_variables(
            self,
            var: dict
    ) -> None:
        self.environments = var

    def normalise_for_platform(
            self,
            value: str
    ):
        system_type = system().lower()

        if system_type == 'windows':
            return value.upper()

        return value

    def has_entry(
            self,
            key: str
    ):
        environment = self.get_environment_variables()

        if key in environment:
            return True
        
        return False

    def get_entry(
            self,
            key: str
    ):
        key_normalised_for_platform: str = self.normalise_for_platform(key)

        if self.has_entry(key_normalised_for_platform):
            return self.get_environment_variables()[key_normalised_for_platform]

        return None

    def setup_labels(self):
        self.set_labels(
            self.get_entry(
                get_environment_dataset_labels()
            )
        )

    def setup_dataset_location(self):
        self.set_dataset_location(
            self.get_entry(
                get_environment_dataset_location()
            )
        )

    def get_labels(self) -> None | str:
        if self.labels is None:
            self.setup_labels()

        return self.labels

    def set_labels(
            self,
            value: str | None
    ) -> None:
        self.labels = value

    def get_dataset_location(self) -> None | str:
        if self.dataset_location is None:
            self.setup_dataset_location()

        return self.dataset_location

    def set_dataset_location(
            self,
            value: str | None
    ) -> None:
        self.dataset_location = value
