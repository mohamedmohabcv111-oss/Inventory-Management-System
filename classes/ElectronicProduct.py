from classes.Product import Product
from Interfaces.IDiscountable import Discount

class ElectronicProduct(Product, Discount):
    def __init__(self, ProductID="", name="", price=0.0, quantity=0, supplier_id="", warranty_period="", power_rating=""):
        Product.__init__(self, ProductID, name, price, quantity, supplier_id)
        Discount.__init__(self, 0.0)
        self.power_rating = power_rating
        self.warranty_period = warranty_period
        self.category = "ELECTRONIC"

    def get_public_info(self):
        return {
            "Category": self.category,
            "Product": self.name,
            "Price": f"${self._Product__price}",
            "WarrantyPeriod": self.warranty_period,
            "PowerRating": f"{self.power_rating}VW",
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
        print("       SET ELECTRONIC INFORMATION")
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
        self.warranty_period = input('\n=== Please Enter Warranty Period ===\n> ')
        self.power_rating = input('\n=== Please Enter Power Rating ===\n> ')

        return self