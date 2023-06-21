from tests.frontend.dataset.io \
    import \
    CategoryMap, \
    retrieve_files


def test_category_map() -> None:
    print()

    cm = CategoryMap('test')

    for f in retrieve_files():
        cm.insert(f)

    assert isinstance(
        cm,
        CategoryMap
    )

