class Bank:
    accountNo = ""
    name = ""
    typeOfAccount = ""
    balance = 0

    def __init__(self,accountNo,name,typeOfAccount,balance):
       self.accountNo = accountNo
       self.name = name
       self.typeOfAccount = typeOfAccount
       self.balance = balance

    def deposit(self,amount):
       self.balance = self.balance + amount

    def withdraw(self,amount):
        self.balance = self.balance - amount


acc1 = Bank("ACC12345","John","Savings",25000)
acc2 = Bank("ACC67890","Cena","Current",51000)

acc1.withdraw(5000)
acc2.deposit(10000)

print(acc1.balance)
print(acc2.balance)