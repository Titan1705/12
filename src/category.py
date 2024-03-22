from src.product import Product


class Category:
    number_of_categories = 0
    unique_product = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.number_of_categories += 1
        Category.unique_product += len(products)

    def add_product(self, new_product):
        self.__products.append(new_product)
        Category.unique_product += 1

    @property
    def products(self):
        list_of_products = []
        for product in self.__products:
            list_of_products.append(f"{product.name}, {product.price} руб."
                                    f"Остаток: {product.availability} шт.")
        return list_of_products

    def __repr__(self):
        return (f"Категория - {self.name}, описание - {self.description},"
                f" продукты - {self.__products}|")


