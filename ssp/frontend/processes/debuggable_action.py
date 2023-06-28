#!/usr/bin/env python
from ssp.frontend.commands          \
    import ActionProcess

from ssp.builders                   \
    import DataSetBuildByDirectory


class DebuggableAction(
    ActionProcess
):
    def __init__(
        self,
        parent_queue=None
    ):
        super().__init__(
            'debug-operation',
            parent_queue=parent_queue
        )

    def __del__(self):
        super().__del__()

    def execute(self):
        self.process_to_run()

        self.set_is_done(
            True
        )

    def process_to_run(self) -> None:
        from ssp.frontend import WorkQueue, Controller
        parent: WorkQueue = self.get_parent_queue()
        parent_controller: Controller = parent.get_parent()
        env = parent_controller.get_environment()

        build = DataSetBuildByDirectory(
            env.get_path_to_dataset(),
            env.get_categories()
        )

        build.stream()



