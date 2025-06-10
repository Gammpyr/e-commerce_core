from abc import ABC, abstractmethod
from typing import Any

from src.mixinlog import MixinLog


class BaseProduct(ABC):

    @abstractmethod
    def __add__(self, other: Any):
        pass

    @abstractmethod
    def __str__(self) -> Any:
        pass


class Product(MixinLog, BaseProduct):
    """Класс для продукции"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        if type(self) is type(other):
            return (self.quantity * self.price) + (other.quantity * other.price)
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_data: dict) -> Any:
        """Создает новый объект класса. Если объект с таким именем уже существует,
        то складывает количество и выставляет большую цену"""
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для price"""
        return self.__price

    @price.setter
    def price(self, new_price: int) -> None:
        """Сеттер для price"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.price:
            user_agree = input("Новая цена меньше старой. Вы уверены, что хотите установить новую цену? (y/n) -> ")
            if user_agree.lower() == "y":
                self.__price = new_price
        else:
            self.__price = new_price
