import pytest


def test_mixin_log(capsys, product):
    captured = capsys.readouterr()
    assert captured.out == "Product(Lada, From Russia, 500000.0, 10)\n"
