from ssp.logic.templates    \
    import BagOfWords

from ssp.logic.structures   \
    import CategoryToken

from HardenedSteel.objects  \
    import CounterObject


class Category(BagOfWords):
    def __init__(
            self,
            category_name: str
    ):
        super().__init__()
        self.category_name: str = category_name

        self.tokens: list | None = None
        self.iterator: CounterObject | None = None

    def __del__(self):
        super().__del__()
        del                         \
            self.category_name,     \
            self.tokens,            \
            self.iterator

    def get_name(self) -> str:
        return self.category_name

    def set_name(
            self,
            value: str
    ) -> None:
        self.category_name = value

    def get_tokens(self) -> list:
        if self.is_tokens_none():
            self.set_tokens(
                list()
            )
        return self.tokens

    def set_tokens(
            self,
            value: list
    ) -> None:
        self.tokens = value

    def is_tokens_none(self) -> bool:
        return self.tokens is None

    def on_event_found_token(
            self,
            token: str
    ):
        if self.is_empty():
            self.create_category_token(
                token
            )
        else:
            if self.exist_token_by_string(
                token
            ):
                self.increase_token_counter_for(
                    token
                )
            else:
                self.create_category_token(
                    token
                )

    def increase_token_counter_for(
            self,
            token_name
    ) -> bool:
        if self.is_empty():
            return False

        hash_of_input_token: int = hash(token_name)

        for index in iter(self):
            current_token: CategoryToken = self.retrieve_token_at(index)
            if hash_of_input_token == current_token.get_hash():
                if token_name == current_token.get_word():
                    current_token.get_counter().increment()
                    return True
        return False

    def exist_token_by_string(
            self,
            value: str
    ) -> bool:
        if self.is_empty():
            return False

        hash_of_input_value: int = hash(value)
        for index in iter(self):
            current_token: CategoryToken = self.retrieve_token_at(index)
            if hash_of_input_value == current_token.get_hash():
                if value == current_token.get_word():
                    return True
        return False

    def retrieve_token_at(
            self,
            index: int
    ) -> CategoryToken:
        return self.get_tokens()[index]

    def remove_token_at(
            self,
            index: int
    ):
        return self.get_tokens()[index]

    def create_category_token(
            self,
            value: str
    ):
        self.insert_category_token(
            CategoryToken(
                word=value
            )
        )

    def insert_category_token(
            self,
            value: CategoryToken
    ) -> None:
        self.get_tokens().append(
            value
        )

    def is_empty(self) -> bool:
        return bool(
            self.is_tokens_none()
            or
            len(self) == 0
        )

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

    def __iter__(self):
        if self.is_iterator_none():
            self.set_iterator(
                CounterObject()
            )
        else:
            self.get_iterator().reset()

        return self

    def __next__(self) -> int:
        self.get_iterator().increment()

        if self.get_iterator().previous() < len(self):
            return self.get_iterator().previous()
        else:
            raise StopIteration

    def __len__(self) -> int:
        return len(
            self.get_tokens()
        )
