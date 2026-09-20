
class Supplier:
    def __init__(self,supplier_id="" , company_name="" , phone_number="" ,Companyemail=""):
        self.__supplierid = supplier_id
        self.company = company_name
        self.__phone = phone_number
        self.email = Companyemail
        self.Allinfo = []
        self.publicsupplierinfo = []


    def findspecificSupplier(self,Companyname):
        for item in self.publicsupplierinfo:
            if item["CompanyName"] == Companyname:
                return
        else: print("No Company Name Found Matching!")
        
    def AddSupplierInfo(self,employee):
        if employee.authenticated():
            print("\n" + "="*42)
            print("          SET SUPPLIER INFORMATION")
            print("="*42)
            self.company = input('\n=== Please Enter Company Name ===\n> ')
            self.email = input('\n=== Please Enter Company Email ===\n> ')
            self.__supplierid = input('\n=== Please Enter Supplier ID ===\n> ')
            self.__phone = input('\n=== Please Enter Supplier Hotline ===\n> ')
            
            ALLinfo = {
                "SupplierID": self.__supplierid,
                "SupplierHotLine": self.__phone,
                "CompanyName": self.company,
                "CompanyEmail": self.email
            }
            public_info = {
                "CompanyName": self.company,
                "CompanyEmail": self.email
            }
            self.Allinfo.append(ALLinfo)
            self.publicsupplierinfo.append(public_info)
            
            print("\n" + "="*42)
            print("         SUPPLIER ADDED SUCCESSFULLY")
            print("="*42)
            print('\n')

        else:
            raise PermissionError('Must be employee to add a supplier')

    def getsupplierid(self):
        return self.__supplierid

        
    def _print_supplier_info(self, info_dict, info_type="Public"):
        print(f"\n--- {info_dict.get('CompanyName', 'Unknown Company')} ({info_type} Info) ---")
        for key, value in info_dict.items():
            if key not in ['CompanyName']:
                print(f" {key+':':<16} {value}")

    def getAllinfo(self, employee):
            if not employee.authenticated():
                raise PermissionError('Must be employee to view all supplier details')
            else: 
                print("\n" + "="*42)
                print("          ALL SUPPLIER INFORMATION")
                print("="*42)
                for item in self.Allinfo:
                    self._print_supplier_info(item, "All")
                print("\n" + "="*42)


    def getPublicinfo(self):
        print("\n" + "="*42)
        print("         PUBLIC SUPPLIER INFORMATION")
        print("="*42)
        print('\n')
        for item in self.publicsupplierinfo:
            self._print_supplier_info(item, "Public")
        print("\n" + "="*42)