from ssp.logic.structures \
    import Document

from ssp.persistence \
    import DatasetDocumentStream


class DocumentEvent:
    def __init__(self):
        self.entity: Document | None = None
        self.stream: DatasetDocumentStream | None = None

    def __del__(self):
        del                 \
            self.entity,    \
            self.stream

    def get_entity(self) -> Document | None:
        return self.entity

    def set_entity(
            self,
            value: Document | None
    ) -> None:
        self.entity = value

    def get_stream(self):
        return self.stream

    def set_stream(
            self,
            stream: DatasetDocumentStream
    ) -> None:
        if stream.is_event_none():
            stream.set_event(self)

        self.stream = stream
