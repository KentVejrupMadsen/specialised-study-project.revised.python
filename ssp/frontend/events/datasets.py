from ssp.frontend.events    \
    import                  \
    CounterObject,          \
    DataSetLabelEvent

from HardenedSteel.globals  \
    import get_integer_zero

from ssp.logic.structures   \
    import DataSet


class DataSetEvents:
    def __init__(self):
        self.labels: list | None = None

        self.iterator: CounterObject | None = None
        self.position: CounterObject | None = None

        self.entity: DataSet | None = None

    def __del__(self):
        del                 \
            self.labels,    \
            self.iterator,  \
            self.position,  \
            self.entity

    def __repr__(self):
        return str({
            'iterator': int(self.get_iterator()),
            'position': int(self.get_position()),
            'labels': self.get_event_labels()
        })

    def get_entity(self) -> DataSet:
        return self.entity

    def set_entity(
            self,
            value: DataSet | None
    ) -> None:
        self.entity = value

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

    def move_to_next_index(self):
        self.get_position().increment()

    def move_to_previous_index(self):
        self.get_position().decrement()

    def current_index(self):
        return self.get_position().get_value()

    def set_position_by_label(
            self,
            value: str
    ) -> bool:
        normalised_input_value: str = value.lower()

        for index in iter(self):
            label: DataSetLabelEvent = self.retrieve_label_event(
                index
            )

            if label.get_label_name_normalised() == normalised_input_value:
                self.get_position().set_value(
                    index
                )

                return True

        return False

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

    def create_label_event(
            self,
            value: str
    ) -> bool:
        if not self.exist_label_event(
                value
        ):
            self.get_event_labels().append(
                DataSetLabelEvent(
                    value
                )
            )

            return True

        return False

    def retrieve_label_event(
            self,
            index: int
    ):
        return self.labels[
            index
        ]

    def retrieve_label_event_by_name(
            self,
            value: str
    ):
        normalised_input = value.lower()

        for index in iter(self):
            events: DataSetLabelEvent = self.retrieve_label_event(
                index
            )

            if events.get_label_name_normalised() == normalised_input:
                return events

    def exist_label_event(
            self,
            value: str
    ) -> bool:
        if int(self) == get_integer_zero():
            return False
        else:
            normalised_input: str = value.lower()

            for index in iter(self):
                label: DataSetLabelEvent = self.retrieve_label_event(
                    index
                )

                if label.get_label_name_normalised() == normalised_input:
                    return True

        return False

    def is_event_labels_none(self) -> bool:
        return self.labels is None

    def get_event_labels(self) -> list:
        if self.is_event_labels_none():
            self.set_event_labels(
                list()
            )

        return self.labels

    def set_event_labels(
            self,
            value: list
    ) -> None:
        self.labels = value

    def __int__(self) -> int:
        if self.is_event_labels_none():
            return get_integer_zero()
        else:
            return len(
                self.labels
            )

    def __iter__(self):
        if self.is_iterator_none():
            self.set_iterator(
                CounterObject()
            )
        else:
            self.get_iterator().reset()

        return self

    def __next__(self):
        if self.get_iterator() < int(self):
            self.get_iterator().increment()
            return self.get_iterator().previous()
        else:

            raise StopIteration
