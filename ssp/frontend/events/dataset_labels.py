from HardenedSteel.objects  \
    import CounterObject

from ssp.frontend.events \
    import CategoryEvent


class DataSetLabelEvent:
    def __init__(
            self,
            name: str
    ):
        self.label_name: str = name
        self.position: CounterObject | None = None
        self.category_events: list | None = None

    def __del__(self):
        del                         \
            self.label_name,        \
            self.position,          \
            self.category_events

    def create_category(
            self,
            value: str
    ) -> None:
        self.get_category_events().append(
            CategoryEvent(
                value
            )
        )

    def retrieve_category_event(
            self,
            index: int
    ) -> CategoryEvent:
        return self.get_category_events()[index]

    def set_position_by_label(
            self,
            category_name: str
    ) -> None:
        if self.is_category_events_none():
            return None

        normalised_category_name: str = category_name.lower()

        for index in range(
                    len(
                        self.category_events
                    )
                ):
            category_event: CategoryEvent = self.retrieve_category_event(index)

            if normalised_category_name == category_event.get_category_name().lower():
                self.get_position().set_value(index)
                return None

    def delete_category_event(
            self,
            index: int
    ) -> None:
        self.get_category_events().pop(
            index
        )

    def get_category_events(self) -> list:
        if self.is_category_events_none():
            self.set_category_events(
                list()
            )

        return self.category_events

    def set_category_events(
            self,
            value: list
    ) -> None:
        self.category_events = value

    def is_category_events_none(self) -> bool:
        return self.category_events is None

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

    def get_position(self) -> CounterObject:
        if self.position is None:
            self.set_position(
                CounterObject()
            )

        return self.position

    def set_position(
            self,
            value: CounterObject
    ):
        self.position = value

    def __repr__(self):
        return str({
            'label': self.label_name,
            'categories': self.get_category_events(),
            'position': int(
                self.get_position()
            )
        })
