from SpecialisedStudyProject.templates \
    import Word


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

        if self.is_to_normalise():
            self.get_changed_event().hint()
            self.get_changed_event().on_trigger()

    def __del__(self):
        super().__del__()
