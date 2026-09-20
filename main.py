from classes.Supplier import Supplier
from classes.FoodProduct import FoodProduct
from classes.Product import Product
from classes.ElectronicProduct import ElectronicProduct
from classes.ClothingProduct import ClothingProduct
from classes.Employee import Employee
from classes.Inventory import Inventory

choice = '0'

def main():
    global choice
    E = Employee()
    I = Inventory()
    S = Supplier()
    Employees = []
    current_employee = None
    FoodProducts = []
    ElectronicProducts = []
    ClothingProducts = []

    print('\n')
    print('WELCOME')
    print('\nHere Are Your Options!')

    
    while True:
        
        
        if choice == '0':
            print('\n')
            print("="*42)
            print('1. Create Your Employee Account')
            print('2. Login')
            print('3. Continue As Guest')
            print('\n')
            choice = input("Enter your choice: ")


            print("="*42)
            print('\n')

        if choice == '1':
            E = Employee()
            E.createaccount()
            Employees.append(E)

            if E:
                while True:
                    print('\n')
                    print('1)See Your Personal Employee Information')
                    print('2)Add New Product')
                    print('3)Add Discount On Product')
                    print('4)Add Product Quantity')
                    print('5)View All The Inventory')
                    print("6)View All Suppliers List")
                    print('7)Search For Specific Product')
                    print('8)Logout')
                    print('\nPress Q(Quit)')
                    
                    choice2 = input('\nANSWER: ').upper()
            
                    if choice2 == '1':
                        print('\n')
                        E.getemployeeinfo()



                    elif choice2 == '2':
                        S.AddSupplierInfo(E)
                        
                        Category = input('Choose Which Type Of Product You Want To Add From The Available Choices [Food, Electronic, Clothing]: ').upper()
                        if Category == 'FOOD':
                            new_product = FoodProduct()
                            new_product.settinginfo(S)
                            FoodProducts.append(new_product)
            
                            try: 
                                I.AddProduct(new_product, E)
                                print("\n" + "="*42)
                                print("         PRODUCT ADDED SUCCESSFULLY!")
                                print("="*42)
                                print('\n')
                            except PermissionError as e:
                                print(f"Access denied: {e}")
                        
                        elif Category == 'ELECTRONIC':
                            new_product = ElectronicProduct()
                            new_product.settinginfo(S)
                            ElectronicProducts.append(new_product)
            
                            try: 
                                I.AddProduct(new_product, E)
                                print("\n" + "="*42)
                                print("         PRODUCT ADDED SUCCESSFULLY!")
                                print("="*42)
                                print('\n')
                            except PermissionError as e:
                                print(f"Access denied: {e}")
                        
                        elif Category == 'CLOTHING':
                            new_product = ClothingProduct()
                            new_product.settinginfo(S)
                            ClothingProducts.append(new_product)
            
                            try: 
                                I.AddProduct(new_product, E)
                                print("\n" + "="*42)
                                print("         PRODUCT ADDED SUCCESSFULLY")
                                print("="*42)
                                print('\n')
                            except PermissionError as e:
                                print(f"Access denied: {e}")
                        
                        else:
                            print('Invalid Category Selected!')


                    elif choice2 == '3':
                        print("="*42)
                        cat = input('Please Enter The Category From The Following Choices [Food, Electronic, Clothing]: ').upper()
                        name = input('Please Enter The Name Of The Product You Want To Disocunt: ').upper()

                        if cat == 'FOOD':
                            for prod in FoodProducts:
                                if prod.name == name:
                                    prod.Add_Discount()
                        elif cat == 'ELECTRONIC':
                            for prod in ElectronicProducts:
                                if prod.name == name:
                                    prod.Add_Discount()
                        elif cat == 'CLOTHING':
                            for prod in ClothingProducts:
                                if prod.name == name:
                                    prod.Add_Discount()

                        else: print('Invalid Category!')

                        print('\n')


                    elif choice2 == '4':
                        print("="*42)
                        cat = input('Please Enter The Category From The Following Choices [Food, Electronic, Clothing]: ').upper()
                        name = input('Please Enter The Name Of The Product You Want To Increase Its Quantity: ').upper()
                        number = int(input('\nPlease Enter The Quantity Increase You Want: '))

                        
                        I.AddQuantity(cat,name,number,E)
                                    


                    elif choice2 == '5':
                        print('\n All Inventory Information')
                        I.ViewAllInv(E)
                        print('\n')


                    elif choice2 == '6':
                        S.getAllinfo(E)


                    elif choice2 == '7':
                        print("="*42)
                        Cat = input('Please Enter The Category You Want: ').upper()
                        name = input('Please Enter The Name Of The Product You Are Looking For: ').upper()
                        
                        I.FindAllProduct(Cat,name)


                    elif choice2 == '8':
                        E.logout()
                        choice = '0'
                        break  
                    elif choice2 == 'Q':
                        print('\nBYE BYE :(')
                        print('\n')
                        exit()
                        
                    else: 
                        print('No Other Choices!')

        elif choice == '2':
            print('\n')
            print("="*42)
            print('         LOGGING IN...')
            print("="*42)
            print('\n')

            empname = input('Please Enter The Acoounts Name: ').upper()
            emppass = input('Please Enter The Password: ').upper()

            for emp in Employees:
                if emp.name == empname:
                    try:
                        emp.login(emppass)
                        current_employee = emp
                    except ValueError as e:
                        print(f"Login failed: {e}")
                    break
            else: print('\nAccount Was Not Found!')

            if current_employee:
                while True:
                    print('\n')
                    print('1)See Your Personal Employee Information')
                    print('2)Add New Product')
                    print('3)Add Discount On Product')
                    print('4)Add Quantity')
                    print('5)View All The Inventory')
                    print("6)View All Suppliers List")
                    print('7)Search For Specific Product')
                    print('8)Logout')
                    print('\nPress Q(Quit)')
                    choice2 = input('\nANSWER: ').upper()
            
                    if choice2 == '1':
                        print('\n')
                        current_employee.getemployeeinfo()


                    elif choice2 == '2':
                        S.AddSupplierInfo(current_employee)
                        
                        Category = input('Choose Which Type Of Product You Want To Add From The Available Choices[FOOD , ElECTRONIC , CLOTHING]: ').upper()
                        if Category == 'FOOD':
                            new_product = FoodProduct()
                            new_product.settinginfo(S)
                            FoodProducts.append(new_product)
            
                            try: 
                                I.AddProduct(new_product, current_employee)
                                print("\n" + "="*42)
                                print("         PRODUCT ADDED SUCCESSFULLY")
                                print("="*42)
                                print('\n')
                            except PermissionError as e:
                                print(f"Access denied: {e}")
                        
                        elif Category == 'ELECTRONIC':
                            new_product = ElectronicProduct()
                            new_product.settinginfo(S)
                            ElectronicProducts.append(new_product)
            
                            try: 
                                I.AddProduct(new_product, current_employee)
                                print("\n" + "="*42)
                                print("         PRODUCT ADDED SUCCESSFULLY")
                                print("="*42)
                                print('\n')
                            except PermissionError as e:
                                print(f"Access denied: {e}")
                        
                        elif Category == 'CLOTHING':
                            new_product = ClothingProduct()
                            new_product.settinginfo(S)
                            ClothingProducts.append(new_product)
            
                            try: 
                                I.AddProduct(new_product, current_employee)
                                print("\n" + "="*42)
                                print("         PRODUCT ADDED SUCCESSFULLY")
                                print("="*42)
                                print('\n')
                            except PermissionError as e:
                                print(f"Access denied: {e}")
                        
                        else:
                            print('Invalid Category Selected!')



                    elif choice2 == '3':
                        print("="*42)
                        cat = input('Please Enter The Category From The Following Choices [Food, Electronic, Clothing]: ').upper()
                        name = input('Please Enter The Name Of The Product You Want To Disocunt: ').upper()
                        
                        if cat == 'FOOD':
                            for prod in FoodProducts:
                                if prod.name == name:
                                        prod.Add_Discount()
                        elif cat == 'ELECTRONIC':
                            for prod in ElectronicProducts:
                                if prod.name == name:
                                    prod.Add_Discount()
                        elif cat == 'CLOTHING':
                            for prod in ClothingProducts:
                                if prod.name == name:
                                    prod.Add_Discount()
                        
                        else: print('Invalid Category!')
                                                
                        print('\n')

                    elif choice2 == '4':
                        print("="*42)
                        cat = input('Please Enter The Category From The Following Choices [Food, Electronic, Clothing]: ').upper()
                        name = input('Please Enter The Name Of The Product You Want To Increase Its Quantity: ').upper()
                        number = int(input('\nPlease Enter The Quantity Increase You Want: '))
                        
                                                
                        I.AddQuantity(cat,name,number,current_employee)


                    elif choice2 == '5':
                        print('\n All Inventory Information')
                        I.ViewAllInv(current_employee)
                        print('\n')


                    elif choice2 == '6':
                        S.getAllinfo(current_employee)


                    elif choice2 == '7':
                        print("="*42)
                        Cat = input('Please Enter The Ctaegory You Want: ').upper()
                        name = input('Please Enter The Name Of The Product You Are Looking For: ').upper()
                        
                        I.FindAllProduct(Cat,name)


                    elif choice2 == '8':
                        current_employee.logout()
                        current_employee = None
                        choice = '0'
                        break 
                    elif choice2 == 'Q':
                        print('\nBYE BYE :(')
                        print('\n')
                        exit()
                        
                    else: 
                        print('No Other Choices!')
            else:
                choice = '0'

        elif choice == '3':
            print('\n')
            print("Continuing as Guest...")
            print('\n')

            while True:
                print('\n')
                print('1)View Public Inventory Information')
                print("2)View Public Supplier List")
                print('3)Search For Specific Product')
                print('4)<- GO BACK')
                print('Press Q(Quit)')
                choice3 = input('\n"ANSWER: ').upper()

                if choice3 == '1':
                    I.ViewInv()
                elif choice3 == '2':
                    S.getPublicinfo()
                elif choice3 == '3':
                    print("="*42)
                    Cat = input('Please Enter The Category You Want: ').upper()
                    name = input('Please Enter The Name Of The Product You Are Looking For: ').upper()
                    I.FindPublicProduct(Cat,name)
                elif choice3 == '4':
                    choice = '0'
                    break 
                elif choice3 == 'Q':
                    print('\nBYE BYE :(')
                    print('\n')
                    exit()
                    
                else: 
                    print('No Other Choices!')

if __name__ == "__main__":
    main()