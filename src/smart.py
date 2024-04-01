from src.product import Product


class Smartfone(Product):
    """Класс SmartFone, наследуется от базового класса продукта"""
    efficiency: int    #производительность
    memory: int   #объем встроенной памяти
    model: int

    def __init__(self, name, description, price, availability, colour, efficiency, model, memory):
        super().__init__(name, description, price, availability, colour)
        self.efficiency = efficiency
        self.memory = memory
        self.model = model
