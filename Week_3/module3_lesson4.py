class BankAccount:

    account_number = None
    firstname = None
    lastname = None
    account_balance = 0

    def __init__(self):
        pass
    
    def set_details(self, firstname, lastname, account_number, account_balance = 0):
        self.account_number = account_number
        self.firstname = firstname
        self.lastname = lastname
        self.account_balance = account_balance

    def withdrawal(self, amount):
        self.account_balance = self.account_balance - amount
        return self.account_balance


    def deposit(self,amount):
        self.account_balance = self.account_balance + amount
        return self.account_balance


y = BankAccount()
y.set_details('bukola', 'ajayi', '202020202')


#setting to withdrawal
y.withdrawal(40000)
print(y.account_balance)


#setting to deposit
y.deposit(90000)
print (y.account_balance)


    