#!/usr/bin/env python
class CommandOption:
    def __init__(self):
        self.key: str | None = None
        self.values: str | None = None

    def __del__(self):
        del             \
            self.key,   \
            self.values
