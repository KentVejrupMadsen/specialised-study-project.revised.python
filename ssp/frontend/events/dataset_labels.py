
class DataSetLabelEvent:
    def __init__(
            self,
            name: str
    ):
        self.label_name: str = name

    def __del__(self):
        del self.label_name

    def get_label_name(self) -> str:
        return self.label_name

    def get_label_name_normalised(self) -> str:
        return str(
            self.label_name
        ).lower()

    def set_label_name(
            self,
            value: str
    ) -> None:
        self.label_name = value
