from ssp.frontend.commands                      \
    import ActionProcess

from ssp.builders.dataset_builder_by_directory  \
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

    def process_to_run(self):
        pass