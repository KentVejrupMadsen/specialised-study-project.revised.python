from tests \
    import get_random_generator


def random_text(length_of_text: int) -> str:
    result_str: str = ''

    for character in range(0, length_of_text):
        result_str = result_str + character_in_range(97, 122)

    return result_str


def character_in_range(
        begin: int,
        end: int
):
    random_number: int = get_random_generator().randint(begin, end)
    return chr(random_number)
