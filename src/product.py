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
    def init_new_product(cls, dict_with_prod, category):
        name = dict_with_prod['name']
        description = dict_with_prod['description']
        price = dict_with_prod['price']
        availability = dict_with_prod['quantity']
        for product in Product.products_list:
            if product.name == name:
                product.quantity += availability
                if product.price < price:
                    product.price = price
                return None
        category.add_product(cls(name, description, price, availability))

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print('Новая цена не соответствует условиям')
        else:
            self.__price = value
