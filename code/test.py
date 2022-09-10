#!/usr/bin/python3
import os

from libraries.dataset \
    import Dataset


def main():
    data_path = os.getcwd() + '/.data'
    ds = Dataset()
    ds.set_path(data_path)


if __name__ == '__main__':
    main()