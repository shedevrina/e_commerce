from src.exeptions import ZeroCountProduct
from src.product import Product


class Category:
    """Класс для представления категории продуктов"""

    name: str
    description: str
    products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name=None, description=None, products=None):

        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        self.all_count = 0
        for i in self.product_in_list:
            self.all_count += i.quantity
        return f"{self.name}, количество продуктов: {self.all_count} шт."

    @property
    def products(self) -> str:  # Геттер для __products
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    def add_product(self, product: Product):
        """Метод добавления нового продукта в категорию."""
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroCountProduct("Нельзя добавить продукт с нулевым количеством")
            except ZeroCountProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар добавлен")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    @property
    def product_in_list(self):
        return self.__products

    def middle_price(self):
        """Метод для подсчета средней цены товаров категории."""
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
