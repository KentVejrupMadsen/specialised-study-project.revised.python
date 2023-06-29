from abc                                \
    import                              \
    ABC

from SpecialisedStudyProject.templates  \
    import OnChangeEvent

from HardenedSteel.objects              \
    import CounterObject


class Word(
    ABC
):
    def __init__(
        self,
        value: str,
        is_to_normalise_on_creation: bool = False
    ) -> None:
        self.token: str = value
        self.length: int | None = None
        self.hash: int | None = None
        self.is_changed_event: OnWordChanges | None = None
        self.normalise: bool = is_to_normalise_on_creation
        self.iterator: CounterObject | None = None

    def __del__(self) -> None:
        del                         \
            self.token,             \
            self.length,            \
            self.hash,              \
            self.is_changed_event,  \
            self.normalise,         \
            self.iterator

    def is_iterator_none(
        self
    ) -> bool:
        return self.iterator is None

    def set_iterator(
        self,
        value: CounterObject
    ) -> None:
        self.iterator = value

    def get_iterator(self) -> CounterObject:
        if self.is_iterator_none():
            self.set_iterator(
                CounterObject(
                    start_value=1
                )
            )

        return self.iterator

    def is_to_normalise(self) -> bool:
        return self.normalise

    def set_is_to_normalise(
        self,
        value: bool
    ) -> None:
        self.normalise = value

    def is_changed_event_none(self) -> bool:
        return self.is_changed_event is None

    def get_changed_event(self) -> OnChangeEvent:
        if self.is_changed_event_none():
            self.set_changed_event(
                OnWordChanges(self)
            )

        return self.is_changed_event

    def set_changed_event(
        self,
        value: OnChangeEvent
    ):
        self.is_changed_event = value

    def is_length_none(self) -> bool:
        return self.length is None

    def get_length(self) -> int:
        self.trigger__change_event()
        return self.length

    def set_length(
        self,
        value: int
    ) -> None:
        self.length = value

    def get_token(self) -> str:
        self.trigger__change_event()
        return self.token

    def set_token(
        self,
        value: str
    ) -> None:
        self.trigger_event__hint_change_has_happened()
        self.token = value

    def get_hash(self) -> int:
        self.trigger__change_event()
        return self.hash

    def set_hash(
        self,
        value: int
    ) -> None:
        self.hash = value

    def attribute_name_for_token(self) -> str:
        return 'token'

    def attribute_name_for_length(self) -> str:
        return 'length'

    def attribute_name_for_hash(self) -> str:
        return 'hash'

    def attribute_name_for_position(self) -> str:
        return 'position'

    def attribute_name_for_index(self) -> str:
        return 'index'

    def attribute_name_for_character(self) -> str:
        return 'character'

    def dictionary(
        self
    ) -> dict:
        return {
            self.attribute_name_for_token(): self.get_token(),
            self.attribute_name_for_length(): self.get_length(),
            self.attribute_name_for_hash(): self.get_hash(),
            self.attribute_name_for_position():
                {
                    self.attribute_name_for_index(): int(self),
                    self.attribute_name_for_character(): self.get_position()
                }
        }

    def get_position(self) -> chr:
        return self.get_token()[
            int(self)
        ]

    def trigger_event__hint_change_has_happened(
            self
    ) -> None:
        self.get_changed_event().hint()

    def trigger__change_event(
        self
    ) -> None:
        self.get_changed_event().on_trigger()

    def __iter__(self):
        self.get_iterator().reset()
        return self

    def __next__(self) -> int:
        iterator = self.get_iterator()
        iterator.increment()
        index_position: int = iterator.previous()

        if int(index_position) < len(self):
            return int(
                index_position
            )
        else:
            raise StopIteration

    def __int__(self):
        return int(
            self.get_iterator().previous()
        )

    def __hash__(
            self
    ) -> int:
        return self.get_hash()

    def __str__(
            self
    ) -> str:
        return self.get_token()

    def __repr__(
        self
    ) -> str:
        return str(
            self.dictionary()
        )

    def __len__(
            self
    ) -> int:
        return self.get_length()

    # Base Operators
    # ** Equal to or ==
    def __eq__(
        self,
        other
    ) -> bool:
        if is_variation_of_word(
                other
        ):
            return self.is_equal_to_other_word(
                other
            )

        return False

    def is_equal_to_other_word(
        self,
        other
    ):
        compare_to: Word = other

        return bool(
            self.is_equal_to_other_words_hash(
                compare_to
            )
            and
            self.is_equal_to_other_words_length(
                compare_to
            )
            and
            self.is_equal_to_other_words_token(
                compare_to
            )
        )

    # ** Greater Than or >
    def __gt__(
        self,
        other
    ) -> bool:
        if is_variation_of_word(
                other
        ):
            return self.is_greater_than_other_word(
                other
            )
        return False

    def is_greater_than_other_word(
        self,
        other
    ):
        compare_to: Word = other

        if self.is_equal_to_other_words_length(
                compare_to
        ):
            return bool(
                self.is_greater_than_other_words_token(
                    compare_to
                )
            )

        return self.is_greater_than_other_words_length(
            compare_to
        )

    def is_greater_than_other_words_token(
        self,
        other
    ):
        compare_to: Word = other
        return self.get_token() > compare_to.get_token()

    def is_greater_than_other_words_length(
        self,
        other
    ):
        compare_to: Word = other
        return self.get_length() > compare_to.get_length()

    def is_greater_than_other_words_hash(
        self,
        other
    ):
        compare_to: Word = other
        return self.get_hash() > compare_to.get_hash()

    # ** Lower than or <
    def __lt__(
        self,
        other
    ) -> bool:
        if is_variation_of_word(
                other
        ):
            return self.is_lesser_than_other_word(
                other
            )

        return False

    def is_lesser_than_other_word(
        self,
        other
    ):
        compare_to: Word = other

        if self.is_equal_to_other_words_length(
                compare_to
        ):
            return bool(
                self.is_lesser_than_other_words_token(
                    compare_to
                )
            )

        return self.is_lesser_than_other_words_length(
            compare_to
        )

    def is_lesser_than_other_words_token(
        self,
        other
    ):
        compare_to: Word = other
        return self.get_token() < compare_to.get_token()

    def is_lesser_than_other_words_length(
        self,
        other
    ):
        compare_to: Word = other
        return self.get_length() < compare_to.get_length()

    def is_lesser_than_other_words_hash(
        self,
        other
    ):
        compare_to: Word = other
        return self.get_hash() < compare_to.get_hash()

    # is equal to
    def is_equal_to_other_words_token(
        self,
        other
    ):
        compare_to: Word = other
        return self.get_token() == compare_to.get_token()

    def is_equal_to_other_words_hash(
        self,
        other
    ):
        compare_to: Word = other
        return self.get_hash() == compare_to.get_hash()

    def is_equal_to_other_words_length(
        self,
        other
    ):
        compare_to: Word = other
        return self.get_length() == compare_to.get_length()


def is_variation_of_word(
    value
) -> bool:
    return isinstance(
        value,
        Word
    )


# Events
class OnWordChanges(
    OnChangeEvent
):
    def __init__(
        self,
        parent_token: Word
    ):
        super().__init__()
        self.parent: Word = parent_token

    def __del__(
        self
    ):
        super().__del__()
        del self.parent

    def get_parent(
        self
    ) -> Word:
        return self.parent

    def set_parent(
        self,
        parent: Word
    ) -> None:
        self.parent = parent

    def is_parent_none(
        self
    ) -> bool:
        return self.parent is None

    def retrieve_token(
        self
    ) -> str:
        return self.get_parent().token

    def trigger(
        self
    ) -> None:
        if self.is_parent_none():
            raise ValueError(
                'Has no parent.'
            )

        self.trigger_normalisation()
        self.trigger_calculation_of_length()
        self.trigger_hashing_of_token()

    def trigger_normalisation(
        self
    ) -> None:
        token: str = self.retrieve_token()
        if self.get_parent().is_to_normalise():
            self.get_parent().set_token(
                str(
                    token
                ).lower()
            )

    def trigger_calculation_of_length(
        self
    ) -> None:
        token: str = self.retrieve_token()
        self.get_parent().set_length(
            len(
                token
            )
        )

    def trigger_hashing_of_token(
        self
    ) -> None:
        token: str = self.retrieve_token()
        self.get_parent().set_hash(
            int(
                hash(
                    token
                )
            )
        )
