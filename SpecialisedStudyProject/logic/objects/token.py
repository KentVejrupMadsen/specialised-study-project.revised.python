from SpecialisedStudyProject.templates \
    import Word

from HardenedSteel.objects             \
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
        super().__init__(
            token_content,
            is_to_normalise_on_creation=True
        )

        self.counter: CounterObject | None = None

        if self.is_to_normalise():
            self.get_changed_event().hint()
            self.get_changed_event().on_trigger()

    def __del__(self):
        super().__del__()

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

