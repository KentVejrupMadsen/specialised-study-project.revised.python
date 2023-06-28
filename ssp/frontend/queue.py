from HardenedSteel.objects  \
    import CounterObject

from HardenedSteel.facades \
    import is_integer_zero

from ssp.frontend.commands \
    import ActionProcess

from time                   \
    import sleep


class WorkQueue:
    def __init__(self):
        self.iterator: CounterObject | None = None
        self.queue: list | None = None
        self.complete: bool = False

    def __del__(self):
        del                 \
            self.queue,     \
            self.iterator,  \
            self.complete

    def cycle(self):
        if is_integer_zero(
            len(self)
        ):
            self.set_is_complete(
                True
            )

        self.check_status_for_individual_actions()

        if not self.is_complete():
            sleep(2)

    def retrieve_queue(self, index: int):
        return self.get_queue()[index]

    def check_status_for_individual_actions(self):
        jobs_done: CounterObject = CounterObject()

        for index in iter(self):
            queue_process: ActionProcess = self.retrieve_queue(index)

            if not queue_process.is_started():
                queue_process.bootstrap_process()

            if queue_process.is_done():
                jobs_done.increment()

        if jobs_done.get_value() == len(self):
            self.set_is_complete(
                True
            )

    def insert_action_process(
            self,
            action: ActionProcess
    ) -> None:
        queue = self.get_queue()
        queue.append(
            action
        )

    def set_is_complete(
            self,
            value: bool
    ) -> None:
        self.complete = value

    def is_complete(self) -> bool:
        return self.complete

    def remove_completed_processes(self) -> None:
        pass

    def get_queue(self) -> list:
        if self.is_queue_none():
            self.set_queue(
                list()
            )

        return self.queue

    def get_iterator(self) -> CounterObject:
        if self.is_iterator_none():
            self.set_iterator(
                CounterObject()
            )

        return self.iterator

    def set_queue(
            self,
            value: list
    ):
        self.queue = value

    def set_iterator(
            self,
            value: CounterObject
    ) -> None:
        self.iterator = value

    def is_iterator_none(self) -> bool:
        return self.iterator is None

    def is_queue_none(self) -> bool:
        return self.queue is None

    def __iter__(self):
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
            self.get_queue()
        )
