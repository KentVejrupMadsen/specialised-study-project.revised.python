from ssp.logic.templates \
    import OnFire

from ssp.persistence \
    import DatasetDocumentStream

from HardenedSteel.globals \
    import get_integer_zero

from HardenedSteel.objects \
    import CounterObject


class DocumentLoader:
    def __init__(
            self,
            dataset_document: DatasetDocumentStream
    ):
        self.stream: DatasetDocumentStream = dataset_document
        self.events: list | None = None
        self.iterator: CounterObject | None = None

    def __del__(self):
        del                 \
            self.stream,    \
            self.events,    \
            self.iterator

    def get_events(self) -> list:
        if self.is_events_none():
            self.set_events(
                list()
            )
        return self.events

    def set_events(
            self,
            value: list
    ):
        self.events = value

    def reset_iterator(self) -> None:
        self.get_iterator().reset()

    def get_iterator(self) -> CounterObject:
        if self.is_iterator_none():
            self.set_iterator(
                CounterObject()
            )

        return self.iterator

    def set_iterator(
            self,
            value: CounterObject
    ) -> None:
        self.iterator = value

    def is_iterator_none(self) -> bool:
        return self.iterator is None

    def insert_event(
            self,
            value: OnFire
    ):
        self.get_events().append(
            value
        )

    def get_event_at(
            self,
            index_at: int
    ):
        return self.get_events()[
            index_at
        ]

    def remove_event_at(
            self,
            index_at: int
    ):
        self.get_events().pop(
            index_at
        )

    def is_events_none(self) -> bool:
        return self.events is None

    def __iter__(self):
        self.reset_iterator()
        return self

    def __next__(self):
        self.get_iterator().increment()

        if self.is_iterator_within_range():
            return self.get_iterator().previous()
        else:
            raise StopIteration

    def is_iterator_within_range(self):
        return bool(
            int(self.get_iterator())
            <=
            len(self)
        )

    def __len__(self):
        if self.is_events_none():
            return get_integer_zero()
        return len(
            self.get_events()
        )

    def trigger_event(
            self,
            value: str
    ):
        for index in iter(self):
            event: OnFire = self.get_event_at(index)

            if not event.is_handler_none():
                event.found_token(
                    value
                )

    def load(self) -> None:
        stream: DatasetDocumentStream = self.stream

        stream.set_is_to_normalise(
            True
        )

        while not stream.is_loaded():
            stream.load_line()

            if not stream.is_line_empty():
                line: str = stream.get_buffer()
                line: str = self.filter_padding(
                    line
                )

                self.map(
                    line
                )

        stream.close()

    def map(
            self,
            line
    ):
        tokens: list | None = line.split(' ')

        for index in range(len(tokens)):
            selected_token = tokens[index]

            self.map_token(
                selected_token
            )

    def map_token(
            self,
            token: str
    ):
        token = self.filter_token_for_invalid_chars(
            token
        )

        is_valid = self.is_valid_token(
            token
        )

        if is_valid:
            print(token)
            self.trigger_event(
                value=token
            )

    def is_valid_token(
            self,
            line: str
    ) -> bool:
        is_valid: bool = False
        is_valid = len(line) > 3
        return is_valid

    def filter_token_for_invalid_chars(
            self,
            line: str
    ):
        result: str = line

        result = result.replace(',', '')
        result = result.replace('<', '')
        result = result.replace('>', '')
        result = result.replace('(', '')
        result = result.replace(')', '')
        result = result.replace('"', '')
        result = result.replace('#', '')
        result = result.replace('&', '')
        result = result.replace(':', '')
        result = result.replace(';', '')

        return result

    def filter_padding(
            self,
            line: str
    ) -> str:
        result: str = line
        begins_at: int = get_line_start(result)
        ends_at: int = get_line_end(result)
        result = result[begins_at: ends_at]

        return result


def get_line_start(
        line: str
) -> int:
    starts_at: CounterObject = CounterObject()

    for index in range(len(line)):
        currently_selected_char: int = ord(line[index])

        if currently_selected_char == ord(' '):
            starts_at.increment()
        else:
            break

    return int(starts_at)


def get_line_end(
        line: str
) -> int:
    ends_at: CounterObject = CounterObject()

    string_character_position: CounterObject = \
        CounterObject(start_value=len(line))

    while string_character_position.get_value() > get_integer_zero():
        index = string_character_position.previous()
        character_in_line: chr = line[index]
        character_numerical: int = ord(character_in_line)

        if character_numerical == ord(' '):
            ends_at.increment()
        elif character_numerical == ord('\r'):
            ends_at.increment()
        elif character_numerical == ord('\n'):
            ends_at.increment()
        else:
            break

        string_character_position.decrement()

    return int(
        len(line)
        -
        int(ends_at)
    )

