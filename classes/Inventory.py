from classes.Employee import Employee


class Inventory:
    def __init__(self):
        self.food_products = []
        self.electronic_products = []
        self.clothing_products = []
        

     

    def AddProduct(self, product , employee):
        if not employee.authenticated():
            raise PermissionError("Must be a logged-in employee to add products")
        else:
            if product.category == "FOOD":
                self.food_products.append(product)    
            elif product.category == "ELECTRONIC":
                self.electronic_products.append(product)  
            elif product.category == "CLOTHING":
                self.clothing_products.append(product)
            else:
                print("Unknown product category!")

    def _print_product_info(self, info_dict):
        print(f"\n--- {info_dict.get('Product', 'Unknown')} ({info_dict.get('Category', 'Unknown')}) ---")
        for key, value in info_dict.items():
            if key not in ['Product', 'Category']:
                print(f" {key+':':<16} {value}")


    def FindAllProduct(self,category,name):
        search_list = []

        if category == "FOOD": search_list = self.food_products
        elif category == "ELECTRONIC": search_list = self.electronic_products
        elif category == "CLOTHING": search_list = self.clothing_products


        for product in search_list:
             if product.name == name:
                print("\n" + "="*42)
                print("              PRODUCT FOUND")
                print("="*42)
                full_info = {**product.get_public_info(), **product.get_private_info()}
                self._print_product_info(full_info)
                print("\n" + "="*42)
                return
        print("\n[!] Product Not Found!") 


    def FindPublicProduct(self, category, name):
        search_list = []
        if category == "FOOD": search_list = self.food_products
        elif category == "ELECTRONIC": search_list = self.electronic_products
        elif category == "CLOTHING": search_list = self.clothing_products

        
        
        for product in search_list:
            if product.name == name:
                print("\n" + "="*42)
                print("              PRODUCT FOUND")
                print("="*42)
                self._print_product_info(product.get_public_info())
                print("\n" + "="*42)
                return
        print("\n[!] Product Not Found!")

    def ViewInv(self):
        all_lists = [self.food_products, self.electronic_products, self.clothing_products]
        for category_list in all_lists:
            for product in category_list:
                self._print_product_info(product.get_public_info())

        print("\n" + "="*42)

    def AddQuantity(self, category, name, quantity, employee):
        if not employee.authenticated():
            raise PermissionError("Must be a logged-in employee to add products")
        else:
            if category == "FOOD":
                for item in self.food_products:
                    if item.name == name:
                        item._Product__quantity += quantity
                
                        print("\n" + "="*42)
                        print("         Quantity Increased SUCCESSFULLY")
                        print("="*42)
                        print('\n')
                        return
                print('\nProduct Not Found!')
                
            elif category == "ELECTRONIC":
                for item in self.electronic_products:
                    if item.name == name:
                        item._Product__quantity += quantity
                
                        print("\n" + "="*42)
                        print("         Quantity Increased SUCCESSFULLY")
                        print("="*42)
                        print('\n')
                        return
                print('\nProduct Not Found!')
                
            elif category == "CLOTHING":
                for item in self.clothing_products:
                    if item.name == name:
                        item._Product__quantity += quantity
                
                        print("\n" + "="*42)
                        print("         Quantity Increased SUCCESSFULLY")
                        print("="*42)
                        print('\n')
                        return
                print('\nProduct Not Found!')
                
            else:
                print("Unknown product category!")

    def ViewAllInv(self,employee):
         if employee.authenticated():
              print("\n" + "="*42)
              print("         ALL INVENTORY INFORMATION")
              print("="*42)
              all_lists = [self.food_products, self.electronic_products, self.clothing_products]
              for category_list in all_lists:
                  for product in category_list:
                      full_info = {**product.get_public_info(), **product.get_private_info()}
                      self._print_product_info(full_info)
              print("\n" + "="*42)
         else:
            raise PermissionError("Permission Denied: Must be employee to view all inventory information.")