from os.path    \
    import      \
    realpath,   \
    dirname,    \
    pardir,     \
    join

location_of_script: str | None = None
location_of_repository: str | None = None


def get_location_of_script() -> str:
    global location_of_script

    if location_of_script is None:
        set_location_of_script(
            dirname(
                realpath(
                    __file__
                )
            )
        )

    return location_of_script


def set_location_of_script(
        value: str
) -> None:
    global location_of_script
    location_of_script = value


def get_location_of_repository() -> str:
    global location_of_repository

    if location_of_repository is None:
        parent = join(
            get_location_of_script(),
            pardir
        )

        set_location_of_repository(
            realpath(
                parent
            )
        )

    return location_of_repository


def set_location_of_repository(
        value: str
) -> None:
    global location_of_repository
    location_of_repository = value
