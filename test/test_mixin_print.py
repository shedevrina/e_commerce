from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_mixin_print(capsys):
    """Проверка вывода в консоль информации о продукте любого класса."""
    Product("name_test", "description_test", 100.0, 15)
    massage = capsys.readouterr()
    assert massage.out.strip() == "Product(name_test, description_test, 100.0, 15)"

    Smartphone("name_test1", "description_test", 100.0, 15, 95.5, "S23 Ultra", 256, "Серый")
    massage = capsys.readouterr()
    assert massage.out.strip() == "Smartphone(name_test1, description_test, 100.0, 15)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    massage = capsys.readouterr()
    assert massage.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
