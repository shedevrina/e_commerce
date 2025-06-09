from src.product import Product


class Category:
    """Класс для представления категории продуктов"""

    name: str
    description: str
    products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name="NoName", description="NoName", products=None):

        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    # Геттер для __products
    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def product_in_list(self):
        return self.__products
