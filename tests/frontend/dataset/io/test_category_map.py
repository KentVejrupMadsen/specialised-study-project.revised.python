from tests.frontend.dataset.io \
    import \
    CategoryMap, \
    retrieve_files


def test_category_map() -> None:
    map = CategoryMap('test')

    for f in retrieve_files():
        map.insert(f)

    print()
    print(str(repr(map)))

    assert isinstance(
        map,
        CategoryMap
    )

