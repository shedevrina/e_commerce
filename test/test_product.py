def test_product_init(product):
    assert product.name == "name_test"
    assert product.description == "description_test"
    assert product.price == 100.00
    assert product.quantity == 15
