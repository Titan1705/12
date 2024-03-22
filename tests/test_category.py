import pytest
from src.category import Category


@pytest.fixture()
def Category_Phone():
    return Category('nokia', 'plastic', '6230i')


def test_init(Category_Phone):
    assert Category_Phone.name == 'nokia'
    assert Category_Phone.description == 'plastic'
    # assert Category_Phone.products[] == "tv"
    assert Category_Phone.number_of_categories == 1
    assert Category_Phone.unique_product == Category.unique_product


def test_product_getter(for_category):
    products = ['tv, 45000 руб. Остаток: 1 шт.']
    assert for_category.products == products


def test_repr(for_category, print_repr=None):
    assert for_category.__repr__() == print_repr