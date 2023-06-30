from SpecialisedStudyProject.templates \
    import StreamMap

from SpecialisedStudyProject.logic \
    import Token


class TokenMapStream(
    StreamMap
):
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()

    def is_instance_token(
        self,
        value
    ) -> bool:
        return isinstance(
            value,
            Token
        )

