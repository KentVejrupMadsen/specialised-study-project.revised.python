from ssp.logic.templates    \
    import BagOfWords

from ssp.logic.structures   \
    import CategoryToken


class Category(BagOfWords):
    def __init__(
            self,
            category_name: str
    ):
        super().__init__()
        self.category_name: str = category_name

    def __del__(self):
        super().__del__()
        del self.category_name

    def get_name(self) -> str:
        return self.category_name

    def set_name(
            self,
            value: str
    ) -> None:
        self.category_name = value

    def on_event_found_token(
            self,
            token: str
    ):
        pass
