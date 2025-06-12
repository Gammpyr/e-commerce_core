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

    def __str__(self) -> str:
        quantity = 0
        for product in self.__products:
            quantity += product.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."

    def add_product(self, adding_product: Any) -> None:
        """Добавляет новый продукт в категорию"""
        if isinstance(adding_product, Product):
            self.__products.append(adding_product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def get_products(self) -> list:
        """Геттер для products"""
        return self.__products

    @property
    def products(self) -> list:
        result = []
        for product in self.__products:
            result.append(str(product))
        return result

    @property
    def middle_price(self):

        sum_price = sum(product.price for product in self.__products)

        try:
            result = sum_price / len(self.get_products)
        except ZeroDivisionError:
            return 0

        return round(result, 2)


class ProductCatalog:
    """Перебирает товары одной категории"""

    def __init__(self, category: Any) -> None:
        self.__products = category.get_products

    def __iter__(self) -> Any:
        self.counter = -1
        return self

    def __next__(self) -> Any:
        if self.counter == len(self.__products) - 1:
            raise StopIteration
        self.counter += 1
        return self.__products[self.counter]
