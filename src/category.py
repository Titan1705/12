from src.product import Product


class Category:
    number_of_categories = 0
    unique_product = 0

    def __init__(self, name: str, description: str, product: list[Product]):
        self.name = name
        self.description = description
        self.__product = product
        Category.number_of_categories += 1
        Category.unique_product += len(product)

    def add_product(self,product):
        self.__product.append(product)
        Category.unique_product += 1

    @property
    def product(self):
        list_of_products = []
        for product in self.__product:
            list_of_products.append(f"{product.name}, {product.price} руб. "
                                    f"Остаток: {product.availability} шт.")
        return list_of_products

    def __repr__(self):
        return (f"Категория - {self.name}, описание - {self.description},"
                f" продукты - {self.__product}|")


