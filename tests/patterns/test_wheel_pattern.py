from tests.patterns.wheel \
    import TestClassForWheel


def testing_wheel():
    print()

    test_class = TestClassForWheel()

    for i in range(20):
        test_class.generate_random_number()

    test_class.__reversed__()

    for i in range(25):
        print(test_class.get_position())
        test_class.move()
