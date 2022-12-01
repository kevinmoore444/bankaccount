from bankaccount import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.is_loyalty_member = False
        self.account = BankAccount(int_rate=0.04, balance=1000)
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()

customer_1 = User("Kevin Moore", "kevinmoore444@gmail.com")
customer_2 = User("John Doe","johndoe123@hotmail.com")

customer_1.make_withdrawal(100)
customer_1.display_user_balance()

customer_2.make_deposit(200).make_withdrawal(100).display_user_balance()
