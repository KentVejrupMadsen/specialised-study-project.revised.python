from HardenedSteel.objects  \
    import CounterObject

from ssp.frontend.events    \
    import DocumentEvent


class CategoryEvent:
    def __init__(
            self,
            category_name: str
    ):
        self.category: str = category_name

    def __del__(self):
        del self.category

