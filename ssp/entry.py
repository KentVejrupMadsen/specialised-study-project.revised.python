from ssp \
    import Application


def on_entry_call():
    app = Application()
    app.run()


if __name__ == '__main__':
    on_entry_call()
