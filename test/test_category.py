import pytest

from src.category import Category
from src.iter_in_category import IterCategory
from src.product import Product


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
        category_one.add_product(1)
        assert TypeError


def test_add_product_positive(category_one, product_lawn_grass_2):
    category_one.add_product(product_lawn_grass_2)
    assert category_one.product_in_list[-1].name == "Газонная трава 2"


def test_avr_category_product(category_avr, category_avr_zero_1):
    assert Category.middle_price(category_avr) == 10
    assert Category.middle_price(category_avr_zero_1) == 0


def test_custom_exeption(capsys, category_one):
    category_one.add_product(Product("name_test", "description_test", 100.0, 0))
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"  # Забираем последний вывод
    assert (
        message.out.strip().split("\n")[-2] == "Нельзя добавить продукт с нулевым количеством"
    )  # Забираем предпоследний вывод

    category_one.add_product(Product("name_test", "description_test", 100.0, 1))
    assert len(category_one.product_in_list) == 3
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"  # Забираем последний вывод
    assert message.out.strip().split("\n")[-2] == "Товар добавлен"  # Забираем предпоследний вывод
