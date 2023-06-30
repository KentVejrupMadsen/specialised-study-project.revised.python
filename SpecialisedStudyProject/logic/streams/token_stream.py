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

    def insert_instances_from_a_token(
        self,
        value: Token
    ):
        for i in range(len(self)):
            current: Token = self[i]

            if current == value:
                current.set_counter(
                    current.get_counter() + value.get_counter()
                )

