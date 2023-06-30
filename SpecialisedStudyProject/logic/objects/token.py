from SpecialisedStudyProject.templates  \
    import Word

from HardenedSteel.objects              \
    import CounterObject

from HardenedSteel.globals              \
    import get_integer_one


class Token(
    Word
):
    def __init__(
        self,
        token_content: str
    ):
        from SpecialisedStudyProject.logic.objects.events \
            import TokenIsFoundEvent

        super().__init__(
            token_content,
            is_to_normalise_on_creation=True
        )

        self.counter: CounterObject | None = None
        self.is_found_event: TokenIsFoundEvent | None = None

        if self.is_to_normalise():
            self.get_changed_event().hint()
            self.get_changed_event().on_trigger()

    def __del__(self):
        super().__del__()
        del \
            self.is_found_event, \
            self.counter

    def get_is_found_event(self):
        from SpecialisedStudyProject.logic.objects.events \
            import TokenIsFoundEvent

        if self.is_found_event_none():
            self.set_is_found_event(
                TokenIsFoundEvent(
                    self
                )
            )

        event: TokenIsFoundEvent = self.is_found_event
        return event

    def is_found_event_none(self) -> bool:
        return self.is_found_event is None

    def set_is_found_event(self, value):
        from SpecialisedStudyProject.logic.objects.events \
            import TokenIsFoundEvent
        event: TokenIsFoundEvent = value
        self.is_found_event = event

    def is_counter_none(self) -> bool:
        return self.counter is None

    def get_counter(self) -> CounterObject:
        if self.is_counter_none():
            self.set_counter(
                CounterObject(
                    start_value=get_integer_one()
                )
            )
        
        return self.counter

    def set_counter(
            self,
            value: CounterObject
    ) -> None:
        self.counter = value

    def increment_of_counter(self):
        self.get_counter().increment()

    def event_is_found(self) -> None:
        self.increment_of_counter()
