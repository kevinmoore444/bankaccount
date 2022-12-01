class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        self.balance = self.balance * (1 + self.int_rate)
        return self

type_1 = BankAccount(0.04, 0)
type_2 = BankAccount(0.05, 200)


type_1.deposit(100).deposit(200).deposit(300).withdraw(100).yield_interest().display_account_info()
type_2.deposit(500).deposit(800).withdraw(600).withdraw(300).withdraw(500).yield_interest().display_account_info()
