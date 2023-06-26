from HardenedSteel.objects  \
    import CounterObject

from ssp.frontend.events    \
    import DocumentEvent

from ssp.logic.structures \
    import Category


class CategoryEvent:
    def __init__(
            self,
            category_name: str
    ):
        self.category: str = category_name
        self.document_events: list | None = None
        self.entity: Category | None = None

    def __del__(self):
        del                         \
            self.category,          \
            self.document_events,   \
            self.entity

    def get_entity(self) -> Category | None:
        return self.entity

    def set_entity(
            self,
            value: Category | None
    ) -> None:
        self.entity = value

    def get_category_name(self) -> str:
        return self.category

    def set_category_name(
            self,
            value: str
    ):
        self.category = value

    def is_document_events_none(self) -> bool:
        return self.document_events is None

    def get_document_events(self) -> list:
        if self.is_document_events_none():
            self.set_document_events(
                list()
            )

        return self.document_events

    def set_document_events(
            self,
            value: list
    ) -> None:
        self.document_events = value
