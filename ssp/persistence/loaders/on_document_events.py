from ssp.logic.templates \
    import OnFire


class OnDocumentEvent(OnFire):
    def __init__(
        self,
        document_factory_event
    ):
        super().__init__()
        self.debug_by_default()
        self.handler = document_factory_event

    def __del__(self):
        super().__del__()

    def found_token(
            self,
            value: str
    ):
        handler = self.get_document_event_handler()
        handler.get_entity().on_event_found_token(
            value
        )

    def get_document_event_handler(self):
        from ssp.builders.events import DocumentEvent
        document_event_handler: DocumentEvent = self.get_handler()
        return document_event_handler
