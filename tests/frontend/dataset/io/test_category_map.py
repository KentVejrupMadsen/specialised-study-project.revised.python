from tests.frontend.dataset.io \
    import \
    retrieve_files

from ssp.persistence \
    import CategoryMap


def test_category_map() -> None:
    print()

    cm = CategoryMap('test')

    for f in retrieve_files():
        cm.insert(f)

    assert isinstance(
        cm,
        CategoryMap
    )

