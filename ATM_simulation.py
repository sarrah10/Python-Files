#heirarchial inheritence
class account:
    def __init__(self,name,acno,phone):
        self.name=name
        self.acno=acno
        self.phone=phone
        self.balance=1000
    def getinfo(self):
        print(self.name)
        print(self.acno)
        print(self.phone)

class SavingAccount(account):
    def __init__(self, name, acno, phone):
        super().__init__(name, acno, phone)  #super() call function from parent account
        self.balance=1000

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("You deposited: ",self.balance)

    def withdraw(self,amount):
        self.balance = self.balance - amount
        print("You withdraw: ",self.balance)

    def checkbalance(self):
        super().getinfo()    #calls getinfo() from parent class
        print("Your balance is: ",self.balance)    #print balance

class CurrentAccount(account):
    def __init__(self, name, acno, phone):
        super().__init__(name, acno, phone) 
        self.balance=5000

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("You deposited: ",self.balance)

    def withdraw(self,amount):
        self.balance = self.balance - amount
        print("You withdraw: ",self.balance)

    def checkbalance(self):
        super().getinfo()    
        print("Your balance is: ",self.balance)  

print("-------Saving Account Info--------")
s1 = SavingAccount("Rahul",101,123)
s1.deposit(5000)
s1.withdraw(2000)
#s1.getinfo()
s1.checkbalance()

print("-------Current account Info--------")
c1 = CurrentAccount("Namita",121,999)
c1.deposit(2000)
c1.withdraw(1000)
# c1.getinfo()
c1.checkbalance()

