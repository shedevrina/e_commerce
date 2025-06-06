class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.__price = price
        self.description = description
        self.quantity = quantity

    # Метод принимающий словарь для создания нового объекта класса
    @classmethod
    def new_product(cls, product_dict: dict):

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

    # Геттер для __price
    @property
    def price(self):
        return self.__price

    # Сеттер для __price. Проверка цены.
    @price.setter
    def price(self, price: float):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price
