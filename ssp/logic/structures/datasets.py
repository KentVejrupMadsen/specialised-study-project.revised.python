#!/usr/bin/env python
class DataSet:
    def __init__(self):
        pass

    def __del__(self):
        pass


class DataSetWrapper:
    def __init__(self):
        self.entity = DataSet()

    def __del__(self):
        del self.entity

    def get_entity(self) -> DataSet:
        return self.entity

    def set_entity(
            self,
            value: DataSet
    ) -> None:
        self.entity = value
