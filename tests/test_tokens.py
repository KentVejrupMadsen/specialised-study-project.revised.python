from SpecialisedStudyProject.templates \
    import Word

from SpecialisedStudyProject.logic \
    import Token

from HardenedSteel.facades \
    import \
    generate_label_by_size, \
    generate_signed_integer


def test_token_subclass():
    token: Token = Token(
        generate_label_by_size(
            generate_signed_integer(
                begin=1,
                end=20
            )
        )
    )

    assert isinstance(
        token,
        Word
    )


def test_token():
    label: Token = Token(
        generate_label_by_size(
            generate_signed_integer(
                begin=1,
                end=20
            )
        )
    )

    assert isinstance(
        label,
        Token
    )


def test_normalising():
    label_test: Token = Token('TESA_NASA')
    print(label_test.get_token())
    assert label_test.get_token().islower()


def test_content():
    label_as_test: Token = Token(
        generate_label_by_size(
            generate_signed_integer(
                begin=1,
                end=240
            )
        )
    )

    print(repr(label_as_test))


def test_tokens_in_a_unsorted_set() -> None:
    content_list: list = list()

    print("\n")
    print("============================================ unsorted list ============================================")

    for i in range(
            generate_signed_integer(
                begin=10,
                end=200
            )
    ):
        generated_token: Token = Token(
            generate_label_by_size(
                generate_signed_integer(
                    begin=3,
                    end=25
                )
            )
        )
        content_list.append(
            generated_token
        )

    print()

    for i in range(len(content_list)):
        current = content_list[i]

        print(
            repr(
                current
            )
        )


def test_iteration_of_token() -> None:
    print('\n\n')
    label_token: Token = Token(
        generate_label_by_size(
            20
        )
    )

    print('iteration of a token ===================================================================================')
    print(repr(label_token))

    for index in iter(label_token):
        print(dict({
            'index': index,
            'character': label_token.get_character_at_current_position()
        }))

    print('\n\n')


def test_tokens_in_a_sorted_set() -> None:
    content_list: list = list()

    print("\n")
    print("# Test ====================================== Sorted list =============================================")

    for i in range(
            generate_signed_integer(
                begin=10,
                end=200
            )
    ):
        generated_token: Token = Token(
            generate_label_by_size(
                generate_signed_integer(
                    begin=3,
                    end=25
                )
            )
        )
        content_list.append(
            generated_token
        )

    print("# Before ==========================================================================================")
    for i in range(len(content_list)):
        current = content_list[i]

        print(
            repr(
                current
            )
        )

    content_list.sort()

    print("# After ==========================================================================================")
    for i in range(len(content_list)):
        current = content_list[i]

        print(
            repr(
                current
            )
        )


