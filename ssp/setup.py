from os.path \
    import \
    realpath, \
    dirname

location_of_script: str | None = None


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
