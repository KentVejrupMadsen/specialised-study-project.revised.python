from ssp.controller \
    import Controller


def main():
    app = Application()
    app.execute()


class Application:
    def __init__(self):
        self.controller = Controller()

    def execute(self):
        pass
