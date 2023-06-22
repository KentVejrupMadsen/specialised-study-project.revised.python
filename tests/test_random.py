from tests \
    import generate_label_by_size


def test() -> None:
    rdr_txt: str = generate_label_by_size(20)

    print()
    print({'random_text': rdr_txt})

    assert isinstance(
        rdr_txt,
        str
    )
