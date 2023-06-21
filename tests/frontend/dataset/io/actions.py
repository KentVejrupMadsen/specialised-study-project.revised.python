from ssp.frontend.environment \
    import Environment

from os \
    import walk

from os.path \
    import join


def retrieve_files() -> list:
    r_value = []

    env = Environment()

    for                                     \
        root,                               \
        dirs,                               \
        files                               \
        in                                  \
            walk(
                env.get_path_to_dataset()
            ):
        for file_path in files:
            full_path = join(
                root,
                file_path
            )

            r_value.append(
                full_path
            )

    return r_value
