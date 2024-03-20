class Category:
    number_of_categories = 0
    unique_product = 0

    def __init__(self, name: str, description: str, product: list):
        self.name = name
        self.description = description
        self.__product = product
        Category.number_of_categories += 1
        Category.unique_product += len(product)

    @property
    def product(self):
        return self.__product

    @property
    def products(self):
        list_of_products = []
        for product in self.__product:
            list_of_products.append(f"{product.name}, {product.price} руб. "
                                    f"Остаток: {product.availability} шт.")
        return list_of_products