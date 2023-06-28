#!/usr/bin/env python
from HardenedSteel.objects  \
    import CounterObject

from HardenedSteel.facades  \
    import is_integer_zero

from HardenedSteel.globals  \
    import                  \
    get_integer_zero,       \
    get_integer_one

from ssp.frontend.commands  \
    import ActionProcess

from time                   \
    import sleep


class WorkQueue:
    def __init__(
            self,
            parent_controller=None
    ):
        self.iterator: CounterObject | None = None
        self.parent_controller = parent_controller

        self.seconds_to_sleep: int = get_integer_one()

        self.complete: bool = False

        self.queue: list | None = None
        self.removal: list | None = None

    def __del__(self):
        del                         \
            self.queue,             \
            self.iterator,          \
            self.complete,          \
            self.seconds_to_sleep,  \
            self.removal,           \
            self.parent_controller

    def set_parent(
            self,
            value
    ):
        self.parent_controller = value

    def get_parent(self):
        return self.parent_controller

    def is_parent_none(self) -> bool:
        return self.parent_controller is None

    def get_removal(self) -> list:
        if self.is_removal_none():
            self.set_removal(
                list()
            )
        return self.removal

    def set_removal(
            self,
            value: list
    ) -> None:
        self.removal = value

    def is_removal_none(self) -> bool:
        return self.removal is None

    def get_seconds_to_sleep(self):
        return self.seconds_to_sleep

    def set_seconds_to_sleep(
        self,
        value: int
    ) -> None:
        self.seconds_to_sleep = value

    def cycle(self):
        self.check_status_for_individual_actions()
        self.remove_completed_processes()

        if not self.is_complete():
            sleep(
                self.get_seconds_to_sleep()
            )

    def retrieve_queue(
        self,
        index: int
    ):
        return self.get_queue()[index]

    def check_status_for_individual_actions(self) -> None:
        if is_integer_zero(
            len(self)
        ):
            self.set_is_complete(
                True
            )
            return None

        jobs_done: CounterObject = CounterObject()

        for index in iter(self):
            queue_process: ActionProcess = self.retrieve_queue(
                index
            )
            if not queue_process.is_started():
                queue_process.bootstrap_process()
            if queue_process.is_done():
                jobs_done.increment()
                self.get_removal().append(index)

        if jobs_done.get_value() == len(self):
            self.set_is_complete(
                True
            )
        return None

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

    def index_to_remove(self, index):
        return self.get_removal()[index]

    def remove_completed_processes(self) -> None:
        size_of_removal: int = len(
            self.get_removal()
        )
        index_position: CounterObject = CounterObject(
            start_value=size_of_removal
        )

        while index_position.previous() >= get_integer_zero():
            # offsets to given index
            current_position = index_position.previous()
            index_to_remove: int = self.index_to_remove(
                current_position
            )

            self.get_queue().pop(
                index_to_remove
            )

            # next index
            index_position.decrement()

        self.empty_removal_index()

    def empty_removal_index(self):
        self.get_removal().clear()

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
