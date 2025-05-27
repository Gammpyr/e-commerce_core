def test_product_init(product):
    assert product.name == "Lada"
    assert product.description == "From Russia"
    assert product.price == 500000.00
    assert product.quantity == 10
