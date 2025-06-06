from src.product import Product

class Smartphone(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

