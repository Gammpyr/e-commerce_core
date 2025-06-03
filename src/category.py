from typing import Any

from src.product import Product


class Category:
    """Класс для категорий товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, adding_product: Any) -> None:
        """Добавляет новый продукт в категорию"""
        if isinstance(adding_product, Product):
            self.__products.append(adding_product)
            Category.product_count += 1

    @property
    def products(self) -> list:
        """Геттер для products"""
        return self.__products

    @property
    def get_list_products(self) -> list:
        result = []
        for product in self.products:
            result.append(str(product))
        return result

    def __str__(self):
        quantity = 0
        for product in self.products:
            quantity += product.quantity
        return f'{self.name}, количество продуктов: {quantity} шт.'