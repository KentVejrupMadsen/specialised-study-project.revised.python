from ssp.frontend.environment \
    import Environment


def test_env():
    env = Environment()

    print(env.get_path_to_dataset())
    print(env.get_path_to_script())
    print(env.get_path_to_repository())
