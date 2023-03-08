# Task №1. Create class
class BankAccount:
    """A class that represents a bank account"""

    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Method for replenishing the balance"""
        self.balance += amount
        return f'Deposit of {amount} successful. New balance is  = {self.balance}'

    def withdrawal(self, withdraw):
        """Method for withdrawing funds"""
        if self.balance >= withdraw:
            self.balance -= withdraw
            return f'Withdrawal of {withdraw} successful. New balance is = {self.balance}'
        else:
            return 'Insufficient balance'

    def bank_fes(self):
        """Method for withdrawing a bank commission in the amount of 5% of the account balance"""
        commission = self.balance * 5 / 100
        self.balance -= commission
        return f'Bank commission in the amount of {commission} deducted from your account. ' \
               f'New balance is = {self.balance}'

    def display(self):
        """Method for displaying account information"""
        return f'Name - {self.name}\n' \
               f'Account number = {self.account_number}\n' \
               f'Balance = {self.balance}'


person_1 = BankAccount(1001, 'Kristina', 45000)
print(person_1.display())
print()
print(person_1.deposit(5000))
print()
print(person_1.withdrawal(3000))
print()
print(person_1.bank_fes())
