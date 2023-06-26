from ssp.logic.structures \
    import Document


class DocumentEvent:
    def __init__(self):
        self.entity: Document | None = None

    def __del__(self):
        del \
            self.entity

    def get_entity(self) -> Document | None:
        return self.entity

    def set_entity(
            self,
            value: Document | None
    ) -> None:
        self.entity = value
