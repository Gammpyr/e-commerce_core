import pytest

from src.smartphone import Smartphone


def test_smartphone_init(first_smartphone):
    assert first_smartphone.name == "Sony Ericsson"
    assert first_smartphone.description == "Новинка"
    assert first_smartphone.price == 50000.00
    assert first_smartphone.quantity == 5
    assert first_smartphone.efficiency == "Япония"
    assert first_smartphone.model == "W810i"
    assert first_smartphone.memory == 64
    assert first_smartphone.color == "Чёрный"
