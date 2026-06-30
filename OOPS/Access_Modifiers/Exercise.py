class BankAccount:
    bank_name = "HDFC Bank"         #Public class Attribute

    def __init__(self,name,balance,pin):
        self.name=name  #public attribute
        self._balance=balance   #protected attribute
        self.__pin=pin  #private attribute

    #Public Method
    def show_details(self):
        print(f"Account Holder: {self.name}")
        print(f"Bank: {BankAccount.bank_name}")
        print(f"Balance: {self._balance}") #Accessing protected attribute
    
    #Protected Method
    def _update_balance(self,amount):
        self._balance+=amount

    #Private Method
    def __verify_pin(self,pin):
        return pin == self.__pin

    #Public Method that uses private method Internally
    def withdraw(self,amount,pin):
        if self.__verify_pin(pin):
            if amount<=self._balance:
                self._update_balance(-amount)
                print(f"Withdrawn amount: {amount}. New balance: {self._balance}")
                self.show_details()
            else:
                print("Insufficient Funds")
        else:
            print("Invalid PIN")


BA1=BankAccount("Rita",250,"asdf")
print("Displaying Account Holders details: ")
BA1.show_details()
BA1._update_balance(500)
BA1.show_details()
BA1.withdraw(100,"asdf")

#Private Attributes accessing exercise
class Student:
    def __init__(self,name,age):
        self.__name=name
        self.age=age
    def show_details(self):
        print(f"Name: {self.__name},age: {self.age}")

S1=Student("Nihi",6)
S1.show_details()

