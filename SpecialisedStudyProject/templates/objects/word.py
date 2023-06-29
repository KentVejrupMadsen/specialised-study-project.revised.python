from abc                \
    import              \
    ABC

from SpecialisedStudyProject.templates          \
    import OnChangeEvent


class Word(ABC):
    def __init__(
        self,
        value: str,
        is_to_normalise_on_creation: bool = False
    ) -> None:
        self.token: str = value
        self.length: int | None = None
        self.hash: int | None = None
        self.normalise: bool = is_to_normalise_on_creation

        self.is_changed_event: OnWordChanges | None = None

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
        self.get_changed_event().on_trigger()
        return self.length

    def set_length(
        self,
        value: int
    ) -> None:
        self.length = value

    def get_token(self) -> str:
        self.get_changed_event().on_trigger()
        return self.token

    def set_token(
        self,
        value: str
    ) -> None:
        self.get_changed_event().hint()
        self.token = value

    def get_hash(self) -> int:
        self.get_changed_event().on_trigger()
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

    def __hash__(self):
        return self.get_hash()

    def __str__(self):
        return self.get_token()

    def __repr__(self) -> str:
        return str(
            self.dictionary()
        )

    def __del__(self) -> None:
        del                         \
            self.token,             \
            self.length,            \
            self.is_changed_event

    def __len__(self) -> int:
        return self.get_length()


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
