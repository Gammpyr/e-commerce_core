from logging import raiseExceptions

import pytest

from src.category import Category, ProductCatalog
from src.product import Product


def test_category_init(first_category, second_category):
    assert first_category.name == "Mobile"
    assert first_category.description == "Perfect mobile phones"
    assert len(first_category.products) == 3

    assert second_category.name == "TV"
    assert second_category.description == "Great TV"
    assert len(first_category.products) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_category_add_product(first_category, product):
    first_category.add_product(product)
    assert len(first_category.products) == 4


def test_category_add_product_type_error(first_category):
    with pytest.raises(TypeError):
        first_category.add_product("Not a product")


def test_category_get_list_product(first_category, product):
    assert first_category.products[0] == "LG, 1000.0 руб. Остаток: 5 шт."

    first_category.category_count = 0
    first_category.product_count = 0


def test_test_category_magic_str(first_category):
    assert str(first_category) == "Mobile, количество продуктов: 30 шт."


def test_product_catalog(first_category):

    expected = ["LG", "Sony", "Moto"]
    result = [obj.name for obj in ProductCatalog(first_category)]

    assert result == expected

def test_middle_price(first_category):
    assert first_category.middle_price == 2000.00

def test_middle_price_zero_div_error(first_category):
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price == 0.0
