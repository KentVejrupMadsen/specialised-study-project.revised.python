from os.path \
    import isdir


class CorpusSet:
    def __init__(
            self,
            location: str,
            corpus_set: str
    ):
        self.location: str = location

        if not self.exist_location_path():
            raise Exception('set directory does not exist')

        self.corpus_set: str = corpus_set

    def exist_location_path(self) -> bool:
        return isdir(self.location)
