from src.product import Product

class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

