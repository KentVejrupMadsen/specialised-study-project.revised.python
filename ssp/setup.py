from os.path    \
    import      \
    realpath,   \
    dirname,    \
    pardir,     \
    join

location_of_script: str | None = None
location_of_repository: str | None = None
location_of_dataset: str | None = None


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


def get_location_of_dataset() -> str:
    global location_of_dataset

    if location_of_dataset is None:
        location_to_dataset = join(
            get_location_of_repository(),
            'dataset'
        )

        location_to_dataset = join(
            location_to_dataset,
            'Reuters21578'
        )

        location_to_dataset = join(
            location_to_dataset,
            'dataset'
        )

        set_location_of_dataset(
            location_to_dataset
        )

    return location_of_dataset


def set_location_of_dataset(
        value: str
) -> None:
    global location_of_dataset
    location_of_dataset = value
