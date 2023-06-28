from ssp.frontend.commands  \
    import ActionProcess


class CalculateAction(ActionProcess):
    def __init__(self):
        super().__init__('calculate')

    def __del__(self):
        super().__del__()

    def execute(self):
        pass