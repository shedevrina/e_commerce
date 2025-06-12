import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == "name_test"
    assert product.description == "description_test"
    assert product.price == 100.00
    assert product.quantity == 15


def test_new_product(product_dict):
    product = Product(**product_dict)
    assert product.name == "Samsung"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 20.0
    assert product.quantity == 5


def test_new_product_type(coll_negative_product_type):
    with pytest.raises(TypeError) as info_type_error:
        for i in coll_negative_product_type:
            Product(**i)
            assert str(info_type_error.value) == "Ошибка типа данных"


def test_new_product_value(product_negative_dict):
    with pytest.raises(ValueError) as info_value_error:
        for i in product_negative_dict:
            Product.new_product(product_negative_dict)
            assert str(info_value_error.value) == " 'Неполные данные' "


def test_price_update(capsys, product):
    product.price = 0.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product.price = -100.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_all_summ_product(product_add_1, product_add_2):
    assert product_add_1 + product_add_2 == 300.0


def test_product_str(product):
    assert str(product) == "name_test, 100.0 руб. Остаток: 15 шт."


def test_all_summ_product_other_class(product_add_1, product_lawn_grass_1):
    with pytest.raises(TypeError):
        assert product_add_1 + product_lawn_grass_1