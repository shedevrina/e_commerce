def test_category_init(category_one, category_two):
    assert category_one.name == "name_test_one"
    assert category_one.description == "description_test_one"
    assert len(category_one.products) == 2

    assert category_one.category_count == 2
    assert category_two.category_count == 2

    assert category_one.product_count == 4
    assert category_two.product_count == 4
