from SpecialisedStudyProject.logic  \
    import                          \
    TokenMapStream,                 \
    Token

from HardenedSteel.facades          \
    import                          \
    generate_label_by_size,         \
    generate_signed_integer


def generate_random_label() -> str:
    return generate_label_by_size(
        generate_signed_integer(
            begin=4,
            end=30
        )
    )


def test_of_stream_map() -> None:
    stream: TokenMapStream = TokenMapStream()

    assert isinstance(
        stream,
        TokenMapStream
    )


def test_of_token_map_retrieve_individual() -> None:
    stream: TokenMapStream = TokenMapStream()

    for i in range(100):
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



def test_of_token_map_retrieve_list() -> None:
    pass


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


def test_of_insertion_by_default() -> None:
    pass


def test_of_consolidation_by_two_maps() -> None:
    pass


def test_of_consolidation_by_three_maps() -> None:
    pass


def test_of_consolidation_by_five_maps() -> None:
    pass


def test_of_consolidation_by_ten_maps() -> None:
    pass

