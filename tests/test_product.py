import pytest

from src import category
from src.product import Product


@pytest.fixture()
def product_test():
    return Product("Xiaomi Redmi Note 11", "Синий", 31000.0, 14)


def test_init(product_test):
    assert product_test.name == "Xiaomi Redmi Note 11"
    assert product_test.description == "Синий"
    assert product_test.price == 31000.0
    assert product_test.availability == 14

