from ssp \
    import Application


def on_entry_call():
    app = Application()
    app.execute()


if __name__ == '__main__':
    on_entry_call()
