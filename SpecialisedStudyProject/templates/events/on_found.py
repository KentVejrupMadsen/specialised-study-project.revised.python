from abc            \
    import          \
    ABC,            \
    abstractmethod


class OnFoundEvent(ABC):
    def __init__(self):
        pass

    def __del__(self):
        pass

    @abstractmethod
    def on_trigger(self):
        raise NotImplemented
