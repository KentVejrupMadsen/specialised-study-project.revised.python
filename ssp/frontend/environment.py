from ssp.frontend.environments \
    import EnvironmentExports


class Environment:
    def __init__(self):
        self.exports: EnvironmentExports | None = EnvironmentExports()

    def __del__(self):
        pass

    def get_exports(self) -> EnvironmentExports | None:
        return self.exports

    def set_exports(
            self,
            value: EnvironmentExports
    ) -> None:
        self.exports = value
