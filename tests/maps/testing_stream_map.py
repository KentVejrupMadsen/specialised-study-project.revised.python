from SpecialisedStudyProject.logic  \
    import TokenMapStream


def test_of_stream_map() -> None:
    stream: TokenMapStream = TokenMapStream()

    assert isinstance(
        stream,
        TokenMapStream
    )
