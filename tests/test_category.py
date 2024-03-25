import pytest
from src.category import Category
from src.product import Product
from tests.test_product import product_test


@pytest.fixture()
def category_test(product_test):
    return Category("Смартфоны", "Современные", [product_test])


def test_init(category_test):
    assert category_test.name == 'Смартфоны'
    assert category_test.description == 'Современные'
    assert category_test.product == ['Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.']
    assert category_test.number_of_categories == 1
    assert category_test.unique_product == Category.unique_product


def test_add_product(category_test, product_test):
    category_test.add_product(product_test)
    assert len(category_test.product) == 2
