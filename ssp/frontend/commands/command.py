class Command:
    def __init__(
            self,
            queue: str
    ):
        self.queue = queue

    def __del__(self):
        del self.queue
