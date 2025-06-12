from src.product import Product


class LawnGrass(Product):
    """Класс-наследник от продукта: «Трава газонная» ."""

    def __init__(
        self, name=None, description=None, price=None, quantity=None, country=None, germination_period=None, color=None
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Переопределение. Чтобы складывались только объекты класса-наследника"""
        if not isinstance(other, LawnGrass):
            raise TypeError

        all_summ = self.price * self.quantity + other.price * other.quantity
        return all_summ
