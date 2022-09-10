import sqlite3

from db.setup \
    import DatabaseSetup


class Database:
    def __init__(self, name):
        self.dbname = name + '.db'
        self.connector = None

    def setup_table(self):
        setup = DatabaseSetup(self)

    def start(self):
        self.connector = sqlite3.connect(self.dbname)

    def close(self):
        self.connector.close()