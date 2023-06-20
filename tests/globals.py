from random \
    import SystemRandom

system_generator: SystemRandom | None = None


def get_generator() -> SystemRandom | None:
    global system_generator

    if is_generator_none():
        set_generator(
            SystemRandom()
        )

    return system_generator


def is_generator_none() -> bool:
    global system_generator
    return system_generator is None


def set_generator(
        generator: SystemRandom
) -> None:
    global system_generator
    system_generator = generator
