from unittest.mock import MagicMock, patch

from src.category import Category
from src.utils import create_objects_from_data, get_data_from_json


@patch("json.load")
@patch("builtins.open")
def test_get_data_from_json(mock_open, mock_load, read_data):
    mock_file = MagicMock()
    mock_file.__enter__.result_value.read.result_value = {}
    mock_open.result_value = mock_file

    mock_load.return_value = read_data

    assert get_data_from_json() == read_data


def test_create_objects_from_data(read_data):
    Category.category_count = 0
    Category.product_count = 0
    obj = create_objects_from_data(read_data)[0]
    assert obj.name == "Mobile"
    assert obj.description == "description_test"
    assert obj.get_products[0].name == "name_test"
    assert obj.get_products[0].description == "desc1"
    assert obj.get_products[1].name == "name_test2"
    assert obj.get_products[1].description == "desc2"

    assert obj.category_count == 1
    assert obj.product_count == 2

