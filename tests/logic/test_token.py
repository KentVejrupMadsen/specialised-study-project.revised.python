from tests \
    import Token


def test_token() -> None:
    test_token = Token('lerom ipsum merara')

    print('token: ', test_token.get_word())
    print('hash: ', test_token.get_hash())

    assert not test_token is None


def test_comparison() -> None:
    test_a = Token('sierra')
    test_b = Token('sierra')

    print()
    print({test_a.get_word(), test_a.get_hash()})
    print({test_b.get_word(), test_b.get_hash()})

    assert test_a == test_b
