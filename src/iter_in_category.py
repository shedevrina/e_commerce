from src.category import Category


class IterCategory:
    """Принимает на вход объект класса категории и производит итерацию по товарам категории."""

    def __init__(self, category_obj: Category):
        self.category_obj = category_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if len(self.category_obj.product_in_list) > self.index:
            product = self.category_obj.product_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
