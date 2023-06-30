from SpecialisedStudyProject.templates.events   \
    import OnChangeEvent


class StreamMapOnSizeChange(
    OnChangeEvent
):
    def __init__(
            self,
            parent
    ):
        from SpecialisedStudyProject.templates.streams \
            import StreamMap

        super().__init__()
        self.parent: StreamMap | None = parent

    def __del__(
            self
    ):
        super().__del__()
        del self.parent

    def is_parent_none(
            self
    ) -> bool:
        return self.parent is None

    def get_parent(
            self
    ):
        from SpecialisedStudyProject.templates.streams \
            import StreamMap

        parent: StreamMap = self.parent
        return parent

    def set_parent(
            self,
            value
    ) -> None:
        from SpecialisedStudyProject.templates.streams \
            import StreamMap

        self.parent: StreamMap = value

    def trigger(self) -> None:
        from SpecialisedStudyProject.templates.streams \
            import StreamMap

        if self.is_parent_none():
            raise ValueError(
                'No parent'
            )

        parent: StreamMap = self.get_parent()

        if parent.is_stream_empty():
            return None

        parent.refresh_length()
