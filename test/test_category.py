
def test_category_init(category_one, category_two):
    assert category_one.name == "name_test_one"
    assert category_one.description == "description_test_one"
    assert len(category_one.product_in_list) == 2

    assert category_one.category_count == 2
    assert category_two.category_count == 2

    assert category_one.product_count == 4
    assert category_two.product_count == 4


def test_add_product(category_one, product):
    category_one.add_product(product)
    assert category_one.products == (
        "name_test1, 50.0 руб. Остаток: 20 шт.\n"
        "name_test2, 50.0 руб. Остаток: 20 шт.\n"
        "name_test, 100.0 руб. Остаток: 15 шт.\n"
    )
