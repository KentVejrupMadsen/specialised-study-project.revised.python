#!/usr/bin/env python
from ssp.frontend                   \
    import                          \
    Environment,                    \
    DataSetBuildByDirectory


class Controller:
    def __init__(self):
        self.environment = Environment()
        self.dataset: DataSetBuildByDirectory | None = None

    def __del__(self):
        del                   \
            self.environment, \
            self.dataset

    def setup(self) -> None:
        self.set_dataset(
            DataSetBuildByDirectory(
                self.get_environment().get_path_to_dataset(),
                self.get_environment().get_categories()
            )
        )

    def initialise(self):
        self.setup()

        ds = self.get_dataset()
        while ds.is_running():
            ds.stream()

    def execute(self):
        ds = self.get_dataset()

    def get_environment(self) -> Environment:
        return self.environment

    def set_environment(
            self,
            value: Environment
    ) -> None:
        self.environment = value

    def get_dataset(self) -> None | DataSetBuildByDirectory:
        return self.dataset

    def set_dataset(
            self,
            value: None | DataSetBuildByDirectory
    ) -> None:
        self.dataset = value
