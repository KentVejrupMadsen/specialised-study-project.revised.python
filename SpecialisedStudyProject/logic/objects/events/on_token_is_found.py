from SpecialisedStudyProject.templates              \
    import OnFoundEvent

from SpecialisedStudyProject.logic.objects.events   \
    import token_exception_not_found


class TokenIsFoundEvent(
    OnFoundEvent
):
    def __init__(
        self,
        parent
    ):
        from SpecialisedStudyProject.logic \
            import Token
        super().__init__()
        self.parent: Token | None = parent

    def __del__(self):
        super().__del__()
        del self.parent

    def on_trigger(self):
        from SpecialisedStudyProject.logic \
            import Token

        if self.is_parent_none():
            token_exception_not_found()

        parent: Token = self.get_parent()
        parent.event_is_found()

    def get_parent(self):
        return self.parent

    def set_parent(
        self,
        value
    ) -> None:
        self.parent = value

    def is_parent_none(self) -> bool:
        return self.parent is None

