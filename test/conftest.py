import pytest
from src.product import Product
from src.category import Category



@pytest.fixture
def product():
    return Product("name_test", "description_test", 100.00, 15)



@pytest.fixture
def category_one():
    return Category("name_test_one", "description_test_one",
                    [Product("name_test1", "desk_test1", 50.00, 20),
                     Product("name_test2", "desk_test2", 50.00, 20)])


@pytest.fixture
def category_two():
    return Category("name_test_two", "description_test_two",
                    [Product("name_test1", "desk_test1", 10.00, 10),
                     Product("name_test2", "desk_test2", 10.00, 10)])




# @pytest.fixture
# def reset_category_count():
#     yield
#     Category.category_count = 0  # Сброс после теста

#
# @pytest.fixture
# def coll_negative_type():
#     """Негативные данные"""
#     return [True, -3, [1, "hello", [0]], {}, [], None]
