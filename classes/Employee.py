import random

class Employee:
    def __init__(self, name="", password=""):
        self.randomizer = 'asd123hbdnsaid243'
        self.name = name
        self.__EmoployeeID = self.randomization()
        self.__password = password
        self.__islogged = False
      

    def randomization(self):
        id = ''

        for i in range(5):
            id += random.choice(self.randomizer)

        return id

    def createaccount(self):
        namee = input('\n=== Please Enter Name Of Your Account: ').upper()
        self.name = namee
        passwordd = input('\n=== Please Enter Password Of Your Account: ').upper()
        self.__password = passwordd

        self.__islogged = True

        print("\n" + "="*42)
        print("         Account Created Successfully!")
        print("="*42)
        print('\n')

        return self


    def getemployeeinfo(self):
        print("\n" + "="*42)
        print("           EMPLOYEE INFORMATION")
        print("="*42)
        print(f" Name:       {self.name}")
        print(f" EmployeeID:         {self.__EmoployeeID}")
        

    def login(self,entered_password):
        if entered_password == self.__password:
            self.__islogged = True
            print('\n')
            print(f"Welcome back, {self.name}!")
        else:
            self.__islogged = False
            raise ValueError("Incorrect password!")


    def logout(self):
        self.__islogged = False
        print(f"{self.name} logged out.")

    def authenticated(self):
       return self.__islogged
