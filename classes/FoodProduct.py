from classes.Product import Product
from Interfaces.IDiscountable import Discount

class FoodProduct(Product, Discount):
    def __init__(self, ProductID="", name="", price=0.0, quantity=0, supplier_id="", expiration_date="", storage_temp=""):
        Product.__init__(self, ProductID, name, price, quantity, supplier_id)
        Discount.__init__(self, 0.0)
        self.expiration_date = expiration_date
        self.temp = storage_temp
        self.category = "FOOD"

    def get_public_info(self):
        return {
            "Category": self.category,
            "Product": self.name,
            "Price": f"${self._Product__price}",
            "ExpirationDate": self.expiration_date,
            "StorageTemp": f"{self.temp}C",
            "Discount": f"{self.Discount}%" if self.Discount > 0 else "None"
        }

    def Add_Discount(self):
            Discountt = float(input('Please Enter The Discount On The Item: '))
            self.Discount = Discountt

            print("\n" + "="*42)
            print("         DISCOUNT ADDED SUCCESSFULLY")
            print("="*42)
            print('\n')

    def settinginfo(self,supplier):
        print("\n" + "="*42)
        print("          SET FOOD INFORMATION")
        print("="*42)
        self._Product__Productid = input('\n=== Please Enter Product ID ===\n> ')
        self._Product__supplierID = supplier.getsupplierid()
        price = float(input('\n=== Please Enter Price ===\n> '))
        quantity = int(input('\n=== Please Enter Quantity ===\n> '))
        
        if price > 0 and quantity > 0:
             self._Product__price = price
             self._Product__quantity = quantity
        else:
             raise ValueError('Invalid Input! Both price and quantity must be greater than 0')

        self.name = input('\n=== Please Enter Product Name ===\n> ').upper()
        self.expiration_date = input('\n=== Please Enter Expiration Date ===\n> ')
        self.temp = input('\n=== Please Enter Storage Temperature ===\n> ')

        return self