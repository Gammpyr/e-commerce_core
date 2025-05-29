class Category:
    """Класс для категорий товаров"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, new_product):
        self.__products.append(new_product)

    @property
    def products(self):
        for product in self.__products:
            print(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')

