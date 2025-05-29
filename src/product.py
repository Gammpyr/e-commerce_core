class Product:
    """Класс для продукции"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return Product(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")

        if new_price < self.price:
            user_agree = input("Новая цена меньше старой. Вы уверены, что хотите установить новую цену? (y/n) -> ")
            if user_agree == 'y':
                self.__price = new_price
        else:
            self.__price = new_price

