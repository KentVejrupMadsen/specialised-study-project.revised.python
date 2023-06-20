from ssp.adhoc \
    import environ

from ssp.variables \
    import \
    get_environment_dataset_location, \
    get_environment_labels

environment_variables: dict | None = None


def get_environment_variables() -> dict | None:
    global environment_variables

    if environment_variables is None:
        set_environment_variables(
            dict(
                environ
            )
        )

    return environment_variables


def set_environment_variables(
        variables: dict
) -> None:
    global environment_variables
    environment_variables = variables


def is_environment_variable_none(
        key: str
) -> bool:
    envs: dict = get_environment_variables()

    if key in envs:
        return envs[key] is None

    return True


def retrieve_environment_label(
        key: str
):
    return environ[key]


class EnvironmentExports:
    def __init__(self):
        self.labels: None | str = None
        self.dataset_location: None | str = None

    def setup_labels(self):
        if not is_environment_variable_none(
            get_environment_labels()
        ):
            self.set_labels(
                retrieve_environment_label(
                    get_environment_labels()
                )
            )

    def setup_dataset_location(self):
        if not is_environment_variable_none(
            get_environment_dataset_location()
        ):
            self.set_dataset_location(
                retrieve_environment_label(
                    get_environment_dataset_location()
                )
            )

    def get_labels(self) -> None | str:
        if self.labels is None:
            self.setup_labels()

        return self.labels

    def set_labels(
            self,
            value: str
    ) -> None:
        self.labels = value

    def get_dataset_location(self) -> None | str:
        if self.dataset_location is None:
            self.setup_dataset_location()

        return self.dataset_location

    def set_dataset_location(
            self,
            value: str
    ) -> None:
        self.dataset_location = value
