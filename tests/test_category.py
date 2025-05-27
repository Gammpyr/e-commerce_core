def test_Category_init(first_category, second_category):
    assert first_category.name == "Mobile"
    assert first_category.description == "Perfect mobile phones"
    assert len(first_category.products) == 3

    assert second_category.name == "TV"
    assert second_category.description == "Great TV"
    assert len(first_category.products) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5
