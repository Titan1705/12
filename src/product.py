class Product:
    name: str
    description: str
    price: float
    availability: int

    products_list = []

    def __init__(self, name, description, price, availability):
        self.name = name
        self.description = description
        self.__price = price
        self.availability = availability

    @classmethod
    def init_new_product(cls, product_data, list_of_products=None):
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        availability = product_data['availability']
        if list_of_products:
            for product in list_of_products:
                if product.name == name:
                    product.quantity += availability
                    if product.price < price:
                        product.price = price
                    return product
        new_product = (cls(name, description, price, availability))
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
        """ Сложение сумм продуктов """
        if isinstance(other, self.__class__) and isinstance(self, other.__class__):
            return self.availability * self.__price + other.availability * other.__price
        raise TypeError