from src.product import Product


class Grass(Product):
    """Класс Трава газонная, наследуется от базового класса продукта"""
    country_of_origin: str    #страна-производитель
    germination_period: int   #срок прорастания

    def __init__(self, name, description, price, availability, colour, country_of_origin, germination_period):
        super().__init__(name, description, price, availability, colour)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
