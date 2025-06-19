import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def product():
    """Объект родительского класса"""
    return Product("name_test", "description_test", 100.0, 15)


@pytest.fixture
def product_add_1():
    """Объект родительского класса. Для сложения"""
    return Smartphone("name_test_add_1", "description_test", 100.0, 1)


@pytest.fixture
def product_add_2():
    """Объект родительского класса. Для сложения"""
    return Smartphone("name_test_add_2", "description_test", 100.0, 2)


@pytest.fixture
def coll_negative_product_type():
    """Негативные данные"""
    return [True, -3, [1, "hello", [0]], [], None]


@pytest.fixture
def product_dict():
    """Для добавления объекта родительского класса в виде словаря."""
    return {"name": "Samsung", "description": "256GB, Серый цвет, 200MP камера", "price": 20.0, "quantity": 5}


@pytest.fixture
def product_negative_dict():
    return {
        "name": "Samsung",
    }


@pytest.fixture
def category_one():
    """Объект родительского класса"""
    return Category(
        "name_test_one",
        "description_test_one",
        [
            Product("name_test1", "desk_test1", 50.0, 20),
            Product("name_test2", "desk_test2", 50.0, 20)],
    )


@pytest.fixture
def category_two():
    """Объект родительского класса"""
    return Category(
        "name_test_two",
        "description_test_two",
        [
            Product("name_test1", "desk_test1", 10.0, 10),
            Product("name_test2", "desk_test2", 10.0, 10)],
    )


@pytest.fixture
def category_add_product():
    """Объект родительского класса"""
    return Category(
        "name_test_1",
        "description_test_two",
        [
            Product("name_test1", "desk_test1", 10.0, 10),
            Product("name_test2", "desk_test2", 10.0, 10)],
    )


@pytest.fixture
def product_smartphone_1():
    """Объект класса-наследника"""
    return Smartphone(
        "name_test1",
        "description_test",
        100.0,
        15,
        95.5,
        "S23 Ultra",
        256,
        "Серый")


@pytest.fixture
def product_smartphone_2():
    """Объект класса-наследника"""
    return Smartphone(
        "name_test2",
        "description_test2",
        10.0,
        1,
        98.2,
        "15",
        512,
        "Gray space")


@pytest.fixture
def product_lawn_grass_1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0, 20,
        "Россия",
        "7 дней",
        "Зеленый")


@pytest.fixture
def product_lawn_grass_2():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0, 15,
        "США",
        "5 дней",
        "Темно-зеленый")


@pytest.fixture
def category_avr():
    return Category(
        "name_test_1",
        "description_test_two",

        [Product("name_test1", "desk_test1", 10.0, 2),
         Product("name_test2", "desk_test2", 10.0, 2)],
    )


@pytest.fixture
def category_avr_zero_1():
    return Category(
        "name_test_1",
        "description_test_two",
        [],
    )


@pytest.fixture
def category_avr_zero_2():
    return Category(
        "name_test_2", "description_test_two",
        [Product("name_test1", "desk_test1", 10.0, 0)])
