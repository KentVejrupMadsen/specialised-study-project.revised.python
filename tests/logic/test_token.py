from tests                  \
    import                  \
    Token,                  \
    generate_label_by_size


def test_token() -> None:
    test_token = Token(generate_label_by_size(40))

    print()
    print(
        {test_token.get_word(), test_token.get_hash()}
    )

    assert not test_token is None


def test_comparison_true() -> None:
    test_token: str = generate_label_by_size(40)

    test_a = Token(test_token)
    test_b = Token(test_token)

    print()
    print(
        {test_a.get_word(), test_a.get_hash()}
    )
    print(
        {test_b.get_word(), test_b.get_hash()}
    )

    assert test_a == test_b

