from unittest.mock import patch, MagicMock

import pytest

from src.utils import get_data_from_json


@patch("json.load")
@patch("builtins.open")
def test_get_data_from_json(mock_open, mock_load, read_data):
    mock_file = MagicMock()
    mock_file.__enter__.result_value.read.result_value = {}
    mock_open.result_value = mock_file

    mock_load.return_value = read_data

    assert get_data_from_json() == read_data

def test_create_objects_from_data(read_data):
