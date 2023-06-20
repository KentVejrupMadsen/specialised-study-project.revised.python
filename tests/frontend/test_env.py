from ssp.frontend.environment \
    import Environment


def test_env():
    env = Environment()

    print({
        'path': [
            env.get_path_to_script(),
            env.get_path_to_dataset(),
            env.get_path_to_repository()
        ],

        'category': env.get_categories()
    })


def test_category() -> None:
    env = Environment()
    assert isinstance(
        env.get_categories(),
        list
    )


def test_path_to_script() -> None:
    env = Environment()
    assert isinstance(
        env.get_path_to_script(),
        str
    )


def test_path_to_repository() -> None:
    env = Environment()
    assert isinstance(
        env.get_path_to_repository(),
        str
    )


def test_path_to_dataset() -> None:
    env = Environment()
    assert isinstance(
        env.get_path_to_dataset(),
        str
    )

