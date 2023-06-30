from SpecialisedStudyProject.logic \
    import \
    TokenMapStream, \
    Token

from HardenedSteel.facades \
    import \
    generate_signed_integer, \
    generate_label_by_size


def test_stream():
    size: int = 100000

    stream: TokenMapStream = TokenMapStream()

    for i in range(size):
        generated_token: Token = Token(
            generate_label_by_size(
                length_of_label=generate_signed_integer(
                    begin=3,
                    end=10
                )
            )
        )

        if not stream.exist_element_in_set(
                generated_token
        ):
            stream += generated_token
        else:
            stream.insert_instances_from_a_token(
                generated_token
            )

    assert isinstance(
        stream,
        TokenMapStream
    )
