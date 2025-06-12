from src.product import Product


class Smartphone(Product):
    """Класс-наследник от продукта: «Смартфон» ."""

    def __init__(
        self,
        name=None,
        description=None,
        price=None,
        quantity=None,
        efficiency=None,
        model=None,
        memory=None,
        color=None,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Переопределение. Чтобы складывались только объекты класса-наследника"""
        if not isinstance(other, Smartphone):
            raise TypeError

        all_summ = self.price * self.quantity + other.price * other.quantity
        return all_summ
