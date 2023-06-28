from ssp.frontend.commands  \
    import ActionProcess


class DebuggableAction(ActionProcess):
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()
