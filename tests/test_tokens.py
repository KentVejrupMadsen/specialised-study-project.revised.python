from SpecialisedStudyProject.logic \
    import Token

from HardenedSteel.facades \
    import generate_label_by_size, generate_signed_integer


def test_token():
    label: Token = Token('Test_1234')
    assert isinstance(label, Token)


def test_normalising():
    label_test: Token = Token('TESA_NASA')
    print(label_test.get_token())
    assert label_test.get_token().islower()


def test_content():
    label_as_test: Token = Token(
        generate_label_by_size(
            generate_signed_integer(begin=1, end=240)
        )
    )

    print(repr(label_as_test))





