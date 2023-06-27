from ssp.logic.templates    \
    import                  \
    ABC,                    \
    abstractmethod


class BagOfWords(ABC):
    def __init__(self):
        pass

    def __del__(self):
        pass

    @abstractmethod
    def on_event_found_token(
            self,
            token: str
    ):
        pass
