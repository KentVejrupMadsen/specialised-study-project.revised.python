from ssp.logic.structures \
    import CategoryToken


class Category:
    def __init__(
            self,
            category_name: str
    ):
        self.category_name: str = category_name

    def __del__(self):
        del self.category_name

    def get_name(self) -> str:
        return self.category_name

    def set_name(
            self,
            value: str
    ) -> None:
        self.category_name = value

