from SpecialisedStudyProject.persistence.database \
    import SQLite3Database

path_to_database: str = 'C:\\Users\\Kentv\\Desktop\\test.sqlite3'


def test_of_database() -> None:
    global path_to_database

    example: SQLite3Database = SQLite3Database(
        path_to_database=path_to_database,
        delete_on_creation=True
    )

