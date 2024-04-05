from abc import ABC, abstractmethod


class AbcProduct(ABC):
    @classmethod
    @abstractmethod
    def init_new_product(cls, *args, **kwargs):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    def price(self, value):
        pass

