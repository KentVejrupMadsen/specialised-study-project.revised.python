from SpecialisedStudyProject.persistence.database   \
    import DatabaseTemplate

from sqlite3                                        \
    import connect

from sqlite3.dbapi2                                 \
    import Cursor

from os                                             \
    import remove

from os.path                                        \
    import                                          \
    abspath,                                        \
    dirname,                                        \
    isdir,                                          \
    isfile


class SQLite3Database(
    DatabaseTemplate
):
    def __init__(
        self,
        path_to_database: str,
        delete_on_creation: bool = False
    ):
        if delete_on_creation:
            if isfile(path_to_database):
                remove(path_to_database)

        super().__init__(
            database_handler=connect(
                path_to_database,
                check_same_thread=False,
                cached_statements=1024
            )
        )

    def __del__(self):
        self.clean()
        super().__del__()

    def get_cursor(self) -> Cursor:
        return self.get_handler().cursor()

    def clean(self) -> None:
        if self.is_handler_instantiated():
            self.handler.close()

    def exist_directory(
        self,
        value: str
    ) -> bool:
        parent_directory = dirname(
            abspath(
                value
            )
        )

        return isdir(
            parent_directory
        )
