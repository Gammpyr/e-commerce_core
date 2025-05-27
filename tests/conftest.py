import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_category():
    return Category('Mobile',
                    'Perfect mobile phones',
                    [
                        Product('LG', 'From Japan', 1000.00, 5),
                        Product('Sony', 'From China', 2000.00, 10),
                        Product('Moto', 'From USA', 3000.00, 15),
                    ]
                    )


@pytest.fixture
def second_category():
    return Category('TV',
                    'Great TV',
                    [
                        Product('Xiaomi', 'From Korea', 50000.00, 3),
                        Product('SberTV', 'From Russia', 15000.00, 6),
                    ]
                    )


@pytest.fixture
def product():
    return Product('Lada', 'From Russia', 500000.00, 10),