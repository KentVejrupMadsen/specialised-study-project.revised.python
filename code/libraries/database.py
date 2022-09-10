import sqlite3
import os

from os.path import exists

from libraries.db.setup \
    import DatabaseSetup


class Database:
    def __init__(self, name):
        self.dbname = name + '.db'
        self.connector = None

        self.pre()

    def pre(self):
        path = os.getcwd() + '/' + self.dbname
        if exists(path):
            print('database file found: deleting it')
            os.remove(path)

    def setup_tables(self):
        setup = DatabaseSetup(self)
        self.start()
        setup.build_tables()
        setup.build_references()
        self.close()

    def start(self):
        self.connector = sqlite3.connect(self.dbname)

    def close(self):
        self.connector.close()