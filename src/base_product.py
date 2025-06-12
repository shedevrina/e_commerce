from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный родительским для класса продукта."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
