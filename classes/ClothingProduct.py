from classes.Product import Product
from Interfaces.IDiscountable import Discount

class ClothingProduct(Product, Discount):
    def __init__(self, ProductID="", name="", price=0.0, Quantity=0, supplier_id="", size="", color="", material=""):
        Product.__init__(self, ProductID, name, price, Quantity, supplier_id)
        Discount.__init__(self, 0.0)
        self.size = size
        self.color = color
        self.material = material
        self.category = "CLOTHING"

    def get_public_info(self):
        return {
            "Category": self.category,
            "Product": self.name,
            "Price": f"${self._Product__price}",
            "Size": self.size,
            "Color": self.color,
            "Material": self.material,
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
        print("        SET CLOTHING INFORMATION")
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
        self.size = input('\n=== Please Enter Size ===\n> ')
        self.color = input('\n=== Please Enter Color ===\n> ')
        self.material = input('\n=== Please Enter Material ===\n> ')

        return self
