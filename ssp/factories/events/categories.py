from HardenedSteel.objects          \
    import CounterObject

from HardenedSteel.globals          \
    import get_integer_zero

from ssp.persistence                \
    import DatasetDocumentStream

from ssp.factories.events            \
    import DocumentEvent

from ssp.logic.structures           \
    import Category


class CategoryEvent:
    def __init__(
            self,
            category_name: str
    ):
        self.category: str = category_name
        self.document_events: list | None = None
        self.position: None | CounterObject = None
        self.entity: Category | None = None
        self.iterator: None | CounterObject = None

    def __del__(self):
        del                         \
            self.category,          \
            self.document_events,   \
            self.entity,            \
            self.position,          \
            self.iterator

    def __len__(self) -> int:
        if self.is_document_events_none():
            return get_integer_zero()

        return len(
            self.document_events
        )

    def get_iterator(self) -> CounterObject:
        if self.is_iterator_none():
            self.set_iterator(
                CounterObject()
            )
        return self.iterator

    def set_iterator(
            self,
            value: CounterObject
    ):
        self.iterator = value

    def is_iterator_none(self) -> bool:
        return self.iterator is None

    def __iter__(self):
        self.get_position().reset()
        return self

    def __next__(self) -> int:
        if(
            self.get_iterator().previous()
            <
            len(self)
        ):
            self.get_iterator().increment()
            return self.get_iterator().previous()
        else:
            raise StopIteration

    def __int__(self) -> int:
        return int(
            self.get_position()
        )

    def retrieve_selected_document(self) -> DocumentEvent | None:
        if(
            self.is_document_events_none()
            or
            len(self) == get_integer_zero()
        ):
            return None
        return self.get_event_at(
            int(self)
        )

    def set_position_by_document(
            self,
            value: DatasetDocumentStream
    ):
        range_iterator = range(
            len(self)
        )
        normalised_input_var_location: str = \
            value.get_location().lower()

        for index in range_iterator:
            document_event: DocumentEvent = self.get_event_at(
                index
            )

            document_location_normalised: str = \
                document_event.get_stream().get_location().lower()

            if normalised_input_var_location == document_location_normalised:
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

    def select_by_location(
            self,
            value: str
    ) -> None:
        normalise_input: str = value.lower()

        for index in iter(self):
            document_event: DocumentEvent = self.get_event_at(
                index
            )

            normalised_document_path: str = str(
                document_event.get_stream().get_location()
            ).lower()
            
            if normalise_input == normalised_document_path:
                self.get_position().set_value(
                    index
                )
                return None

