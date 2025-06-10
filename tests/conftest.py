from unittest.mock import MagicMock

import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import BaseProduct, Product
from src.smartphone import Smartphone


@pytest.fixture(autouse=True)
def reset_category_count():
    """Сбрасывает счетчик перед каждым тестом"""
    Category.category_count = 0


@pytest.fixture
def first_category():
    return Category(
        "Mobile",
        "Perfect mobile phones",
        [
            Product("LG", "From Japan", 1000.00, 5),
            Product("Sony", "From China", 2000.00, 10),
            Product("Moto", "From USA", 3000.00, 15),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        "TV",
        "Great TV",
        [
            Product("Xiaomi", "From Korea", 50000.00, 3),
            Product("SberTV", "From Russia", 15000.00, 6),
        ],
    )


@pytest.fixture
def product():
    return Product("Lada", "From Russia", 500000.00, 10)


@pytest.fixture
def product2():
    return Product("Mazda", "From japan", 800000.00, 3)


@pytest.fixture
def read_data():
    return [
        {
            "name": "Mobile",
            "description": "description_test",
            "products": [
                {
                    "name": "name_test",
                    "description": "desc1",
                    "price": 100.0,
                    "quantity": 1,
                },
                {
                    "name": "name_test2",
                    "description": "desc2",
                    "price": 200.0,
                    "quantity": 2,
                },
            ],
        }
    ]


@pytest.fixture
def first_lawngrass():
    return LawnGrass("Трава", "Красивая", 100.00, 10, "Россия", "1 день", "Зелёный")


@pytest.fixture
def first_smartphone():
    return Smartphone("Sony Ericsson", "Новинка", 50000.00, 5, "Япония", "W810i", 64, "Чёрный")


@pytest.fixture
def mock_product():
    product = MagicMock(spec=BaseProduct)
    product.__add__.return_value = 10
    product.__str__.return_value = "Test id works"
    return product
