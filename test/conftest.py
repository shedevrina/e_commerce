import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product("name_test", "description_test", 100.0, 15)

@pytest.fixture
def product_add_1():
    return Product("name_test_add_1", "description_test", 100.0, 1)

@pytest.fixture
def product_add_2():
    return Product("name_test_add_2", "description_test", 100.0, 2)


@pytest.fixture
def coll_negative_product_type():
    """Негативные данные"""
    return [True, -3, [1, "hello", [0]], [], None]


@pytest.fixture
def product_dict():
    return {
        "name": "Samsung",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 20.0,
        "quantity": 5
            }


@pytest.fixture
def product_negative_dict():
    return {
        "name": "Samsung",
    }


@pytest.fixture
def category_one():
    return Category(
        "name_test_one",
        "description_test_one",
        [
            Product("name_test1", "desk_test1", 50.0, 20),
            Product("name_test2", "desk_test2", 50.0, 20)
        ],
    )


@pytest.fixture
def category_two():
    return Category(
        "name_test_two",
        "description_test_two",
        [
            Product("name_test1", "desk_test1", 10.0, 10),
            Product("name_test2", "desk_test2", 10.0, 10)
        ],
    )


# @pytest.fixture
# def reset_category_count():
#     yield
#     Category.category_count = 0  # Сброс после теста

#
