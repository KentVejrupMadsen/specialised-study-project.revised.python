#!/usr/bin/env python
from ssp.frontend                       \
    import                              \
    CounterObject,                      \
    join,                               \
    get_zero

from ssp.logic.structures               \
    import Document

from ssp.frontend.events                \
    import                              \
    DataSetEvents,                      \
    DataSetLabelEvent,                  \
    CategoryEvent,                      \
    DocumentEvent

from ssp.persistence                    \
    import                              \
    DataSetMapBuilder,                  \
    DataSetMapStream,                   \
    CategoryMapStream,                  \
    DatasetDocumentStream,              \
    DocumentLoader


class DataSetBuildByDirectory:
    def __init__(
            self,
            location_to_dataset: str,
            categories: list
    ):
        self.path_to_dataset: str = location_to_dataset
        self.categories: list = categories
        self.selection: CounterObject | None = None
        self.iterator: CounterObject | None = None
        self.data_event: DataSetEvents | None = None
        self.complete: bool = False
        self.store: list | None = None

        self.initialise()

    def __del__(self):
        del                         \
            self.path_to_dataset,   \
            self.categories,        \
            self.complete,          \
            self.store,             \
            self.selection,         \
            self.data_event,        \
            self.iterator

    def is_iterator_none(self) -> bool:
        return self.iterator is None

    def get_iterator(self) -> CounterObject:
        if self.is_iterator_none():
            self.set_iterator(
                CounterObject()
            )

        return self.iterator

    def set_iterator(
            self,
            value: CounterObject
    ) -> None:
        self.iterator = value

    def is_data_event_none(self) -> bool:
        return self.data_event is None

    def get_events(self) -> DataSetEvents:
        if self.is_data_event_none():
            self.set_events(
                DataSetEvents()
            )

        return self.data_event

    def set_events(
            self,
            value: DataSetEvents
    ) -> None:
        self.data_event = value

    def remove_events(self) -> None:
        self.data_event = None

    def reset_iterator(self) -> None:
        self.get_iterator().reset()

    def get_selection(self) -> int:
        return self.get_selection_counter().previous()

    def is_selection_none(self) -> bool:
        return self.selection is None

    def get_selection_counter(self) -> CounterObject:
        if self.is_selection_none():
            self.set_selection_counter(
                CounterObject()
            )

        return self.selection

    def set_selection_counter(
            self,
            value: CounterObject
    ) -> None:
        self.selection = value

    def next_selection(self) -> None:
        self.get_selection_counter().increment()

    def previous_selection(self) -> None:
        self.get_selection_counter().decrement()

    def next_iterator(self) -> None:
        self.get_iterator().increment()

    def previous_iterator(self) -> None:
        self.get_iterator().previous()

    def get_full_path(self) -> str:
        return self.path_to_dataset

    def set_full_path(
            self,
            value: str
    ) -> None:
        self.path_to_dataset = value

    def get_categories(self) -> list:
        return self.categories

    def set_categories(
            self,
            value: list
    ) -> None:
        self.categories = value

    def initialise(self) -> None:
        for category in self.categories:
            self.insert_build_dataset_label(
                join(
                    self.path_to_dataset,
                    category
                )
            )

    def insert_build_dataset_label(
            self,
            full_path: str
    ) -> None:
        builder: DataSetMapBuilder = DataSetMapBuilder(
            full_path
        )

        self.insert_label(
            builder.run()
        )

    def remove_at(
            self,
            position: int
    ) -> None:
        self.get_store().pop(
            position
        )

    def insert_label(
            self,
            value: DataSetMapStream
    ) -> None:
        self.get_store().append(
            value
        )

    def synchronise_events_stream_labels(
            self,
            map_stream: DataSetMapStream
    ) -> None:
        events = self.get_events()

        if not (
            events.get_selection_label_name()
            ==
            map_stream.get_name()
        ):
            events.set_position_by_label(
                map_stream.get_name()
            )

    def synchronise_events_stream_category(
            self,
            category_stream: CategoryMapStream
    ) -> None:
        events = self.get_events()
        label_events = events.retrieve_selection()

        if not(
            category_stream.get_name()
            ==
            label_events.get_label_name_normalised()
        ):
            events.retrieve_selection().set_position_by_label(
                category_stream.get_name()
            )

    def synchronise_events_stream_document(
            self,
            document_stream: DatasetDocumentStream
    ) -> None:
        events = self.get_events()
        label_events = events.retrieve_selection()

        category_event = label_events.retrieve_selected_category_event()
        if category_event is None:
            return None

        currently_selected_document: DocumentEvent | None = \
            category_event.retrieve_selected_document()

        if currently_selected_document is None:
            return None

        # Check that the document is matching with the stream
        if not(
            document_stream.get_location()
            ==
            currently_selected_document.get_stream().get_location()
        ):
            category_event.select_by_location(
                document_stream.get_location()
            )

    def run_stream(self):
        for index in iter(self):
            self.stream_map_by_index(
                index
            )

    def stream(self) -> None:
        self.stream_map_by_index(
            self.get_selection()
        )
        self.next_selection()

    def stream_map_by_index(
            self,
            index: int
    ) -> None:
        selected: DataSetMapStream = self.retrieve_map(
            index
        )

        self.get_events().create_label_event(
            selected.get_name()
        )

        self.stream_dataset_map(
            selected
        )

        if self.is_position_at_end():
            self.set_is_complete(
                True
            )

    def add_event_for_category(
            self,
            value: str
    ):
        label = self.get_currently_selected_label()
        label.create_category(
            value
        )

    def add_event_for_document(
            self,
            value: DatasetDocumentStream
    ):
        category: CategoryEvent = self.get_currently_selected_category()

        event: DocumentEvent = DocumentEvent()
        event.set_entity(
            Document()
        )
        event.set_stream(
            value
        )
        category.insert_event(
            event
        )

    def stream_dataset_map(
            self,
            dsm: DataSetMapStream
    ) -> None:
        self.synchronise_events_stream_labels(
            dsm
        )

        for selected_category \
                in dsm.get_categories():
            category_label: CategoryMapStream = selected_category
            self.add_event_for_category(
                category_label.get_name()
            )

            self.stream_dataset_category(
                category_label
            )

    def stream_dataset_category(
            self,
            cms: CategoryMapStream
    ) -> None:
        self.synchronise_events_stream_category(
            cms
        )

        for document in cms.get_documents():
            selected_document: DatasetDocumentStream = document

            self.add_event_for_document(
                selected_document
            )

            self.stream_dataset_document(
                selected_document
            )

    def stream_dataset_document(
            self,
            document: DatasetDocumentStream
    ) -> None:
        self.synchronise_events_stream_document(
            document
        )

        loader = DocumentLoader(
            document
        )

        loader.load()

    def is_position_at_beginning(self) -> bool:
        return self.is_at_beginning(
            self.get_selection()
        )

    def is_position_at_end(self) -> bool:
        return self.is_at_end(
            self.get_selection()
        )

    def is_at_beginning(
            self,
            position: int
    ) -> bool:
        return position == get_zero()

    def is_at_end(
            self,
            position: int
    ) -> bool:
        return position == len(self)

    def currently_selected_map(self) -> DataSetMapStream:
        return self.retrieve_map(
            self.get_selection()
        )

    def retrieve_map(
            self,
            value: int
    ) -> DataSetMapStream:
        return self.get_store()[value]

    def map(self) -> bool:
        return not self.is_complete()

    def is_running(self) -> bool:
        return not self.is_complete()

    def is_complete(self) -> bool:
        return self.complete

    def set_is_complete(
            self,
            value: bool
    ) -> None:
        self.complete = value

    def is_store_none(self) -> bool:
        return self.store is None

    def get_store(self) -> list | None:
        if self.is_store_none():
            self.set_store(
                list()
            )

        return self.store

    def set_store(
            self,
            value: list
    ) -> None:
        self.store = value

    def is_in_range(
            self,
            position: int
    ) -> bool:
        return position < len(
            self.get_store()
        )

    def is_position_within_range(self) -> bool:
        return self.is_in_range(
            self.get_iterator().previous()
        )

    def get_currently_selected_label(self) -> DataSetLabelEvent:
        return self.get_events().retrieve_selection()

    def get_currently_selected_category(self) -> CategoryEvent:
        return self.get_currently_selected_label().retrieve_selected_category_event()

    def get_currently_selected_document(self) -> DocumentEvent:
        return self.get_currently_selected_category().retrieve_selected_document()

    def __int__(self):
        return int(
            self.get_selection()
        )

    def __len__(self) -> int:
        if self.is_store_none():
            return get_zero()

        return len(
            self.store
        )

    def __iter__(self):
        self.reset_iterator()
        return self

    def __next__(self) -> int:
        self.get_iterator().increment()

        if self.is_position_within_range():
            return self.get_iterator().previous()
        else:
            raise StopIteration
