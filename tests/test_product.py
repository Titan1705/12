import pytest
from src.product import Product


@pytest.fixture()
def Product_Samsung():
    return Product('tv', '65', '45000', 1)


def test_init2(Product_Samsung):
    assert Product_Samsung.name == 'tv'
    assert Product_Samsung.description == '65'
    assert Product_Samsung.price == '45000'
    assert Product_Samsung.availability == 1


def test_init_new_product(dict_with_product, for_category):
    assert len(for_category.products) == 2
    assert len(Product.products_list) == 2
    Product.init_new_product(dict_with_product, for_category)
    assert len(for_category.products) == 3
    Product.init_new_product(dict_with_product, for_category)
    assert len(for_category.products) == 3