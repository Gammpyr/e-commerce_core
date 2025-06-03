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
    result = first_category
    result.add_product(product)
    assert len(result.products) == 4


def test_category_get_list_product(first_category, product):
    assert first_category.get_list_products[0] == "LG, 1000.0 руб. Остаток: 5 шт."

    first_category.category_count = 0
    first_category.product_count = 0

def test_test_category_magic_str(first_category):
    assert str(first_category) == 'Mobile, количество продуктов: 30 шт.'


def test_product_catalog(first_category):
    product_list = ProductCatalog(first_category)
    expected = ['LG', 'Sony', 'Moto']
    result = []
    for obj in product_list:
        result.append(obj.name)

    assert result == expected