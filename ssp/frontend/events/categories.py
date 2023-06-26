from HardenedSteel.objects  \
    import CounterObject

from ssp.persistence \
    import DatasetDocumentStream

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
        self.position: None | CounterObject = None

    def __del__(self):
        del                         \
            self.category,          \
            self.document_events,   \
            self.entity,            \
            self.position

    def __int__(self) -> int:
        if self.is_document_events_none():
            return 0

        return len(
            self.document_events
        )

    def set_position_by_document(
            self,
            value: DatasetDocumentStream
    ):
        for index in \
                range(
                    int(self)
                ):
            document_event: DocumentEvent = self.get_event_at(
                index
            )

            if value.get_location() == document_event.get_stream().get_location():
                self.get_position().set_value(
                    index
                )

    def insert_event(
            self,
            event: DocumentEvent
    ):
        self.get_document_events().append(
            event
        )

    def get_event_at(
            self,
            index: int
    ):
        return self.get_document_events()[
            index
        ]

    def remove_at(
            self,
            index: int
    ) -> None:
        self.get_document_events().pop(
            index
        )

    def get_position(self) -> CounterObject:
        if self.is_position_none():
            self.set_position(
                CounterObject()
            )

        return self.position

    def set_position(
            self,
            value: CounterObject
    ) -> None:
        self.position = value

    def is_position_none(self) -> bool:
        return self.position is None

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
