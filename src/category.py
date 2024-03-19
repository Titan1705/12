class Category:
    name: str
    description: str
    product: list
    number_of_categories = 0
    unique_product = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product

        Category.number_of_categories += 1
        Category.unique_product += 1
