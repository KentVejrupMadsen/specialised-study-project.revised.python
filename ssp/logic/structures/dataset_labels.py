class DataSetLabel:
    def __init__(
            self,
            label: str
    ):
        self.label_name: str = label

    def __del__(self):
        del self.label_name

    def get_name(self) -> str:
        return self.label_name

    def set_name(
            self,
            value: str
    ) -> None:
        self.label_name = value
