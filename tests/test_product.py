from unittest.mock import MagicMock, patch

import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == "Lada"
    assert product.description == "From Russia"
    assert product.price == 500000.00
    assert product.quantity == 10


Product("Lada", "From Russia", 500000.00, 10)


def test_product_new_product():
    test_dict = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет",
        "price": 180000.0,
        "quantity": 5,
    }
    result = Product.new_product(test_dict)
    assert "Samsung Galaxy S23 Ultra" == result.name
    assert "256GB, Серый цвет" == result.description
    assert 180000.0 == result.price
    assert 5 == result.quantity


def test_product_price(product):
    product.price = -100
    assert product.price == 500000.0
    product.price = 600000.0
    assert product.price == 600000.0


@patch("src.product.input")
def test_product_price_setter(mock_input, product):
    mock_input.return_value = "n"
    assert product.price == 500000

    mock_input.return_value = "y"
    product.price = 400000
    assert product.price == 400000


def test_product_add(product, product2):
    assert product + product2 == 7_400_000


def test_product_add_product_type_error(product):
    with pytest.raises(TypeError):
        result = product + 10000


def test_add_method(mock_product):
    other = MagicMock()
    result = mock_product + other
    assert result == 10
    mock_product.__add__.assert_called_once_with(other)


def test_str_method(mock_product):
    result = str(mock_product)
    assert result == "Test id works"
    mock_product.__str__.assert_called_once()
