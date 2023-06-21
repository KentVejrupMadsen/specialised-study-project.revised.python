class DatasetDocument:
    def __init__(
            self,
            location
    ):
        self.location: str = location
        self.loaded: bool = False

    def __del__(self):
        del \
            self.location, \
            self.loaded

    def get_location(self) -> str:
        return self.location

    def set_location(
            self,
            value: str
    ) -> None:
        self.location = value

    def get_loaded(self) -> bool:
        return self.loaded

    def set_loaded(
            self,
            value: bool
    ) -> None:
        self.loaded = value
