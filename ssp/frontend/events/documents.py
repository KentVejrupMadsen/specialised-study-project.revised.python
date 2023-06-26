from ssp.logic.structures \
    import Document


class DocumentEvent:
    def __init__(self):
        self.entity: Document | None = None

    def __del__(self):
        del \
            self.entity
