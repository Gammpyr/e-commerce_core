import pytest

from src.lawngrass import LawnGrass


def test_lawngrass(first_lawngrass):
    assert first_lawngrass.name == "Трава"
    assert first_lawngrass.description == "Красивая"
    assert first_lawngrass.price == 100.00
    assert first_lawngrass.quantity == 10
    assert first_lawngrass.country == "Россия"
    assert first_lawngrass.germination_period == "1 день"
    assert first_lawngrass.color == "Зелёный"
