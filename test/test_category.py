import pytest

from src.iter_in_category import IterCategory


def test_category_init(category_one, category_two):
    assert category_one.name == "name_test_one"
    assert category_one.description == "description_test_one"
    assert len(category_one.product_in_list) == 2

    assert category_one.category_count == 2
    assert category_two.category_count == 2

    assert category_one.product_count == 4
    assert category_two.product_count == 4


def test_add_product(category_one, product):
    category_one.products = product
    assert category_one.products == (
        "name_test1, 50.0 руб. Остаток: 20 шт.\n"
        "name_test2, 50.0 руб. Остаток: 20 шт.\n"
        "name_test, 100.0 руб. Остаток: 15 шт.\n"
    )


def test_category_str(category_one):
    assert str(category_one) == "name_test_one, количество продуктов: 40 шт."


def test_iter_in_category(category_one):
    iter_in_category = IterCategory(category_one)
    assert iter_in_category.index == 0
    assert next(iter_in_category).name == "name_test1"
    assert next(iter_in_category).name == "name_test2"

    with pytest.raises(StopIteration):
        next(iter_in_category)


def test_add_product_negative(category_one):
    with pytest.raises(TypeError):
        category_one.products = 1
        assert TypeError


def test_add_product_positive(category_one, product_lawn_grass_2):
    category_one.products = product_lawn_grass_2
    assert category_one.product_in_list[-1].name == "Газонная трава 2"
