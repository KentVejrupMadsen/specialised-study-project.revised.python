from tests.strings \
    import random_text


def test() -> None:
    rdr_txt: str = random_text(30)

    print()
    print({'random_text': rdr_txt})

    assert isinstance(
        rdr_txt,
        str
    )
