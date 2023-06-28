from ssp.frontend.commands  \
    import ActionProcess


class DebuggableAction(ActionProcess):
    def __init__(self):
        super().__init__('debug-operation')

    def __del__(self):
        super().__del__()

    def execute(self):

        self.set_is_done(
            True
        )
