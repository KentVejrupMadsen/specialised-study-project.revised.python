from HardenedSteel.objects  \
    import CounterObject


class WheelPattern:
    def __init__(self):
        self.selection: None | CounterObject = None

    def __del__(self):
        del self.selection

    def forward_selection(self):
        self.get_selection_counter().increment()

    def backward_selection(self):
        self.get_selection_counter().decrement()

    def set_selection(
        self,
        value: int
    ):
        self.get_selection_counter().set_value(
            value
        )

    def get_selection(self) -> int:
        return self.get_selection_counter().get_value()

    def get_selection_counter(self) -> CounterObject:
        if self.is_selection_counter():
            self.set_selection_counter(
                CounterObject()
            )
        return self.selection

    def set_selection_counter(
            self,
            value: CounterObject
    ) -> None:
        self.selection = value

    def is_selection_counter(self) -> bool:
        return self.selection is None
