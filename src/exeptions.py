class ZeroCountProduct(Exception):
    """Кастомная ошибка, если количество товаров в категории рано 0."""

    def __init__(self, massage=None):
        super().__init__(massage)
