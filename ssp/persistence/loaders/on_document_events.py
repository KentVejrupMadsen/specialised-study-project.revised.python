from ssp.logic.templates \
    import OnFire


class OnDocumentEvent(OnFire):
    def __init__(self):
        super().__init__()

    def __del__(self):
        pass
    