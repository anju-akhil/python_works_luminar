from datetime import datetime
class Bank:
    bank_name:str
    acno:str
    person_name:str
    ac_type:str
    balance:int

    def create(self,b_name,acno,p_name,ac_type,bal):
        self.bank_name=b_name
        self.acno=acno
        self.person_name=p_name
        self.ac_type=ac_type
        self.balance=bal

    def deposit(self,amount):
        self.balance+=amount
        print(f"Your {self.bank_name}has been credited with {amount} available balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Transaction failed","\n""Insufficient balance")
        else:
            self.balance-=amount
            print(f"Your {self.bank_name} has been debited with {amount} avlailable balance is {self.balance}")

    def get_balance(self):
        print(f"Your {self.bank_name} A/c {self.acno} balance on {datetime.today()} is {self.balance}")

obj1=Bank()
obj1.create("sbi","10248","anu","savings",5000)

obj1.deposit(2000)

obj1.withdraw(1000)

obj1.get_balance()

obj2=Bank()
obj2.create("sbi","10548","john","savings",5000)

