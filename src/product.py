from src.product_abc import AbcProduct


class Product(AbcProduct):
    name: str
    description: str
    price: float
    availability: int
    colour: str

    products_list = []

    def __init__(self, name, description, price, availability, colour=None):
        self.name = name
        self.description = description
        self.__price = price
        self.availability = availability
        self.colour = colour

    @classmethod
    def init_new_product(cls, product_data, list_of_products=None):
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        availability = product_data['availability']
        if list_of_products:
            for product in list_of_products:
                if product.name == name:
                    product.availability += availability
                    if product.price < price:
                        product.price = price
                    return product
        new_product = (cls(name, description, price, availability, colour=None))
        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print('Новая цена не соответствует условиям')
        else:
            self.__price = value

    def __str__(self):
        """
        Магический метод для строкового отображения объекта
        """
        return f'{self.name},{self.__price}руб. Остаток: {self.availability} шт.'

    def __add__(self, other):
        if type(other) == self.__class__:
            return self.__price * self.availability + other.__price * other.availability
        return 'Нельзя складывать продукты разных типов'
