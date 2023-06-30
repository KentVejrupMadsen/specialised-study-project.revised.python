from SpecialisedStudyProject.logic  \
    import                          \
    TokenMapStream,                 \
    Token

from HardenedSteel.facades          \
    import                          \
    generate_label_by_size,         \
    generate_signed_integer

do_not_test: bool = False


def get_do_not_test() -> bool:
    global do_not_test
    return do_not_test


def generate_random_token() -> Token:
    return Token(
        token_content=generate_random_label()
    )


def generate_random_label() -> str:
    return generate_label_by_size(
        generate_signed_integer(
            begin=4,
            end=30
        )
    )


def generate_stream_map(
        size: int = generate_signed_integer(
            begin=5,
            end=100
        )
) -> TokenMapStream:
    stream: TokenMapStream = TokenMapStream()

    for i in range(size):
        stream += generate_random_token()

    assert isinstance(
        stream,
        TokenMapStream
    )

    return stream


def test_of_token_map_retrieve_individually() -> None:
    print('\nRetrieve individually =======================================================================')
    stream_to_test: TokenMapStream = generate_stream_map()

    for i in range(
        len(
            stream_to_test
        )
    ):
        result = stream_to_test[i]
        assert isinstance(
            result,
            Token
        )
        print(
            repr(
                result
            )
        )


def test_of_token_map_removal_by_individual() -> None:
    pass


def test_of_token_map_removal_by_list() -> None:
    pass


def test_of_token_map_search_individually() -> None:
    pass


def test_of_token_map_search_by_list() -> None:
    pass


def test_of_token_map_deletion_individual() -> None:
    pass


def test_of_token_map_deletion_by_list() -> None:
    pass


def test_of_token_map_insertion_no_sort() -> None:
    pass


def test_of_adaptive_sorting() -> None:
    pass


def test_of_final_sorting() -> None:
    pass


def test_of_token_map_insert_individually() -> None:
    stream: TokenMapStream = TokenMapStream()

    token_size: int = 200

    for i in range(
        0,
        token_size
    ):
        stream.insert(
            generate_random_token()
        )

    print(
        len(
            stream
        )
    )
    assert len(stream) == token_size


def test_of_insertion_by_operator() -> None:
    stream: TokenMapStream = TokenMapStream()
    size: int = 100

    for i in range(size):
        label = generate_random_label()
        generated_token: Token = Token(
            token_content=label
        )

        assert isinstance(
            generated_token,
            Token
        )

        stream += generated_token

        assert 0 < len(stream)

    assert isinstance(
        stream,
        TokenMapStream
    )

    assert len(stream) == size


def test_of_consolidation_by_two_maps() -> None:
    stream: TokenMapStream = generate_stream_map()
    stream.consolidate(
        generate_stream_map()
    )

    assert isinstance(
        stream,
        TokenMapStream
    )


def test_of_consolidation_by_three_maps() -> None:
    stream: TokenMapStream = generate_stream_map()

    stream.consolidate(
        generate_stream_map()
    )

    stream.consolidate(
        generate_stream_map()
    )

    assert isinstance(
        stream,
        TokenMapStream
    )
