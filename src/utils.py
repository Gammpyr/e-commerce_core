import json
import os
from src.category import Category
from src.product import Product


def get_data_from_json(filename:str ='products.json') -> dict:
    """Возвращает данные из указанного json-файла"""
    full_path = os.path.join('./data/', filename)
    abs_path = os.path.abspath(full_path)

    with open(abs_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def create_objects_from_data(data):
    """ Определяем классы из полученного словаря """
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categories.append(Category(**category))

    return categories


if __name__ == '__main__':
    json_data = get_data_from_json()
    result = create_objects_from_data(json_data)
    for obj in result:
        print(obj.name)
        print(obj.description)
        print(obj.products)

        print(obj.category_count)
        print(obj.product_count)
        print()