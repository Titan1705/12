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

    def add_product(self, product):
        if isinstance(product, Product):
            if product.availability == 0:
                raise ValueError("товар с нулевым количеством не может быть добавлен")
            self.__product.append(product)

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

    def __len__(self):
        """ Подсчёт кол-ва продуктов в категории. """
        product_l = 0
        for i in self.__product:
            product_l += i.availability
        return product_l

    def __str__(self):
        """
        Магический метод для строкового отображения объекта
        """
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def average_price(self):
        """2 задание 16,1 """
        product_sum = 0
        for product in self.__product:
            product_sum += product.price
        try:
            result = product_sum / len(self)
            return result
        except ZeroDivisionError:
            return 0
