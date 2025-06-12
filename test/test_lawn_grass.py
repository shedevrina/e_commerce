import pytest


def test_product_grass(product_lawn_grass_1):
    assert product_lawn_grass_1.name == "Газонная трава"
    assert product_lawn_grass_1.description == "Элитная трава для газона"
    assert product_lawn_grass_1.price == 500.0
    assert product_lawn_grass_1.quantity == 20
    assert product_lawn_grass_1.country == "Россия"
    assert product_lawn_grass_1.germination_period == "7 дней"
    assert product_lawn_grass_1.color == "Зеленый"


def test_add_grass(product_lawn_grass_1, product_lawn_grass_2):
    summ = product_lawn_grass_1 + product_lawn_grass_2
    assert summ == 16750.0


def test_add_grass_negative_type(product_lawn_grass_1, product_smartphone_1):
    with pytest.raises(TypeError) as info:
        assert product_lawn_grass_1 + product_smartphone_1 == info.value
