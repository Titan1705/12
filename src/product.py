class Product:
    name: str
    description: str
    price: float
    availability: int

    def __init__(self, name, description, price, availability):
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability
