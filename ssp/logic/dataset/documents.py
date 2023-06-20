#!/usr/bin/env python
from ssp.logic.dataset \
    import CorpusPreprocessor

from ssp.logic.structures.tokens \
    import DocumentToken


class Document:
    def __init__(
            self,
            location: str,
            processor: CorpusPreprocessor = CorpusPreprocessor()
    ):
        self.file_location: str = location

        self.file_object = None
        self.processor = processor
        self.tokens: list | None = None
        self.debugging: bool = False

    def __del__(self):
        self.done()

    def get_tokens(self) -> list | None:
        return self.tokens

    def set_tokens(
            self,
            value: list | None
    ) -> None:
        self.tokens = value

    def open(self):
        self.set_file_object(
            open(
                self.file_location,
                'r'
            )
        )

    def done(self):
        if not self.is_file_object_none():
            self.get_file_object().close()

    def process(self):
        self.processor.open_stream()

        if self.is_file_object_none():
            self.open()

        self.__process__read_line_by_line()

        self.set_tokens(
            self.processor.get_token_set()
        )

        self.processor.close_stream()
        self.done()

        self.status()

    def status(self):
        if self.is_debugging():
            print('DEBUGGING: Document')
            print('Results for: ', self.get_file_location())

            for token in self.get_tokens():
                selected: DocumentToken = token

                print('  --  token value: ', selected.get_word())
                print('  --  mentions: ', selected.get_counter())
                print()

            print()

    def __process__read_line_by_line(self):
        for line in self.get_file_object().readlines():
            self.processor.stream(
                line
            )

    def get_file_location(self) -> str:
        return self.file_location

    def set_file_location(
            self,
            location: str
    ) -> None:
        self.file_location = location

    def get_file_object(self):
        return self.file_object

    def set_file_object(
            self,
            value
    ) -> None:
        self.file_object = value

    def is_file_object_none(self) -> bool:
        return self.get_file_object() is None

    def is_debugging(self) -> bool:
        return self.debugging

    def set_is_debugging(
            self,
            value: bool
    ) -> None:
        self.debugging = value
