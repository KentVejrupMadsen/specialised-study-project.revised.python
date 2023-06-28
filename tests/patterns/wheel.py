from ssp.logic.templates \
    import WheelPattern

from HardenedSteel.facades \
    import generate_signed_integer


class TestClassForWheel(
    WheelPattern
):
    def __init__(self):
        super().__init__()
        self.elements: list | None = None
        self.increment: bool = True

    def __del__(self):
        super().__del__()
        del self.increment

    def __len__(self):
        return len(
            self.get_elements()
        )

    def __reversed__(self):
        self.set_is_to_increment(
            not self.is_to_increment()
        )

    def move(self):
        if self.is_to_increment():
            self.initiate_forward_selection()
        else:
            self.initiate_backward_selection()

    def is_to_increment(self) -> bool:
        return self.increment

    def set_is_to_increment(
            self,
            value: bool
    ) -> None:
        self.increment = value

    def generate_random_number(self):
        self.get_elements().append(
            generate_signed_integer()
        )

    def selection(self):
        return self.elements[
            self.get_position()
        ]

    def is_at_end(self) -> bool:
        return self.get_position() == (len(self) - 1)

    def is_at_beginning(self) -> bool:
        return self.get_position() == 0

    def is_elements_none(self) -> bool:
        return self.elements is None

    def get_elements(self) -> list:
        if self.is_elements_none():
            self.set_elements(
                list()
            )
        return self.elements

    def set_elements(
            self,
            value: list
    ) -> None:
        self.elements = value

