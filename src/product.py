class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name=None, description=None, price=None, quantity=None):
        self.name = name
        self.__price = price
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError

        all_summ = self.price * self.quantity + other.price * other.quantity
        return all_summ

    @classmethod
    def new_product(cls, product_dict: dict):  # Метод принимающий словарь для создания нового объекта класса

        if type(product_dict) != dict:
            raise TypeError("Ошибка типа данных")
        elif (
            "name" not in product_dict
            or "description" not in product_dict
            or "price" not in product_dict
            or "quantity" not in product_dict
        ):
            raise ValueError("Неполные данные")
        else:
            name = product_dict["name"]
            description = product_dict["description"]
            price = product_dict["price"]
            quantity = product_dict["quantity"]
            return cls(name, description, price, quantity)

    @property
    def price(self):  # Геттер для __price
        return self.__price

    @price.setter
    def price(self, price: float):  # Сеттер для __price. Проверка цены.
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price
