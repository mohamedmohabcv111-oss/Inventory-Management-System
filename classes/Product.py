from abc import ABC, abstractmethod

class Product(ABC):
   def __init__(self ,ProductID="" , name="" , price=0.0 , Quantity=0 , supplier_id=""):
        self.__Productid = ProductID
        self.name = name
        self.__price = price       
        self.__quantity = Quantity 
        self.__supplierID = supplier_id
        
   def get_private_info(self):
        return {
           "SupplierID": self._Product__supplierID,
           "ProductID": self._Product__Productid,
           "Quantity": self._Product__quantity
        }

   @abstractmethod
   def settinginfo(self):
        pass

   @abstractmethod
   def get_public_info(self):
        pass
