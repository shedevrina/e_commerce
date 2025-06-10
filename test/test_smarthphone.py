import pytest


def test_product_smartphone(product_smartphone_1):
    assert product_smartphone_1.name == "name_test1"
    assert product_smartphone_1.description == "description_test"
    assert product_smartphone_1.price == 100.0
    assert product_smartphone_1.quantity == 15
    assert product_smartphone_1.efficiency == 95.5
    assert product_smartphone_1.model == "S23 Ultra"
    assert product_smartphone_1.memory == 256
    assert product_smartphone_1.color == "Серый"


def test_add_smartphone(product_smartphone_1, product_smartphone_2):
    summ = product_smartphone_1 + product_smartphone_2
    assert summ == 1510.0


def test_add_smartphone_negative_type(product_smartphone_1, product_lawn_grass_1):
    with pytest.raises(TypeError) as info:
        assert product_smartphone_1 + product_lawn_grass_1 == info.value
