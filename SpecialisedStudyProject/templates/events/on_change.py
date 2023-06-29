from abc            \
    import          \
    ABC,            \
    abstractmethod


class OnChangeEvent(
    ABC
):
    def __init__(self):
        self.has_changed: bool = False

    def __del__(self):
        del self.has_changed

    def is_changed(self) -> bool:
        return self.has_changed

    def set_has_changed(
            self,
            value: bool
    ) -> None:
        self.has_changed = value

    def hint(self):
        self.set_has_changed(
            True
        )

    def complete(self):
        self.set_has_changed(
            False
        )

    def on_trigger(self) -> None:
        if self.is_changed():
            self.complete()
            self.trigger()

    @abstractmethod
    def trigger(self):
        raise NotImplemented
