class BankAccount:
    def __init__(self, firstname, lastname, account_number, account_balance):
        self.account_number= account_number
        self.firstname = firstname
        self.lastname = lastname
        self.account_balance = account_balance

    def withdrawal(self, amount):
        self.amount = amount
        self.account_balance = self.account_balance - self.amount
        return self.account_balance


    def deposit(self,amount):
        self.account_balance = self.account_balance + self.amount
        return self.account_balance



y = BankAccount('chidi', 'emeka', 1209000040, 100000)
print(y.account_balance)


y.withdrawal(40000)
print(y.account_balance)


y.deposit(90000)
print (y.account_balance)
    