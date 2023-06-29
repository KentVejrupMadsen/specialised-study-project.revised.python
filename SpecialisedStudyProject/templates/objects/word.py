from abc                                \
    import                              \
    ABC

from SpecialisedStudyProject.templates  \
    import OnChangeEvent


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

    def __del__(self) -> None:
        del                         \
            self.token,             \
            self.length,            \
            self.hash,              \
            self.is_changed_event,  \
            self.normalise

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

    def dictionary(self) -> dict:
        return {
            'token': self.get_token(),
            'length': self.get_length(),
            'hash': self.get_hash()
        }

    def trigger_event__hint_change_has_happened(self):
        self.get_changed_event().hint()

    def trigger__change_event(self) -> None:
        self.get_changed_event().on_trigger()

    def __hash__(self):
        return self.get_hash()

    def __str__(self):
        return self.get_token()

    def __repr__(self) -> str:
        return str(
            self.dictionary()
        )

    def __len__(self) -> int:
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
        return self.is_greater_than_other_words_token(
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
        return self.is_lesser_than_other_words_token(
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

    def __del__(self):
        super().__del__()
        del self.parent

    def get_parent(self) -> Word:
        return self.parent

    def set_parent(
        self,
        parent: Word
    ) -> None:
        self.parent = parent

    def is_parent_none(self) -> bool:
        return self.parent is None

    def retrieve_token(self) -> str:
        return self.get_parent().token

    def trigger(self) -> None:
        if self.is_parent_none():
            raise ValueError(
                'Has no parent.'
            )

        self.trigger_normalisation()
        self.trigger_calculation_of_length()
        self.trigger_hashing_of_token()

    def trigger_normalisation(self):
        token: str = self.retrieve_token()
        if self.get_parent().is_to_normalise():
            self.get_parent().set_token(
                str(
                    token
                ).lower()
            )

    def trigger_calculation_of_length(self):
        token: str = self.retrieve_token()
        self.get_parent().set_length(
            len(
                token
            )
        )

    def trigger_hashing_of_token(self):
        token: str = self.retrieve_token()
        self.get_parent().set_hash(
            int(
                hash(
                    token
                )
            )
        )
