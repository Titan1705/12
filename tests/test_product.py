import pytest
from src.product import Product


@pytest.fixture()
def product_test():
    return Product("Xiaomi Redmi Note 11", "Синий", 31000.0, 14)


def test_init(product_test):
    assert product_test.name == "Xiaomi Redmi Note 11"
    assert product_test.description == "Синий"
    assert product_test.price == 31000.0
    assert product_test.availability == 14


@pytest.fixture()
def product_test_class():
    return Product


@pytest.fixture()
def product_test_dict():
    return {'name': 'Samsung A51', 'description': 'Белый', 'price': 20000.0, 'availability': 20}


def test_init_new_product(product_test_class, product_test_dict):
    new_product = product_test_class.init_new_product(product_test_dict)
    assert type(new_product) == product_test_class
    assert new_product.name == product_test_dict['name']
    assert new_product.description == product_test_dict['description']
    assert new_product.price == product_test_dict['price']
    assert new_product.availability == product_test_dict['availability']


def test_init_new_product_with_existing_product(product_test_class, product_test):
    product_data = product_test.__dict__
    product_data['price'] = 41000
    new_product = product_test_class.init_new_product(product_data)
    assert new_product.price == product_data['price']
