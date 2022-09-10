#!/usr/bin/python3
import os

from libraries.dataset \
    import Dataset

from libraries.database \
    import Database


def main():
    ds()
    db()


def db():
    db = Database('test')


def ds():
    data_path = os.getcwd() + '/.data'
    ds = Dataset()
    ds.set_path(data_path)


if __name__ == '__main__':
    main()