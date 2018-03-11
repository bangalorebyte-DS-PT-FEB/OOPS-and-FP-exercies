class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print ('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)

user_a = BankAccount()
user_b = BankAccount()

user_c = MinimumBalanceAccount(100)
print(user_c.deposit(500))
print(user_c.withdraw(200))
print(user_c.withdraw(201))



#print(user_a.deposit(100))

#print(user_b.deposit(50))

#print(user_b.withdraw(10))

#print(user_a.withdraw(10))
