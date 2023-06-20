from ssp.frontend.environments \
    import EnvironmentExports

singleton = None


def get_export_singleton() -> EnvironmentExports | None:
    global singleton

    if singleton is None:
        set_export_singleton(
            EnvironmentExports()
        )

    return singleton


def set_export_singleton(
        value: EnvironmentExports
) -> None:
    global singleton
    singleton = value
