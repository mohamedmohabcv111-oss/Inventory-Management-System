from abc import ABC , abstractmethod 

class Discount(ABC):

    def __init__(self, Discount=0.0):
        self.Discount = Discount

    @abstractmethod
    def Add_Discount(self):
        pass