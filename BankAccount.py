
class BankAccount:

    def __init__(self, balance):
        self.balance = int(balance)

    def get_balance(self):
        return self.balance

    def balance_withdrawl(self, amount):
        if self.balance < int(amount):
            return self.balance
        else:
            self.balance = self.balance - amount
            return self.balance

    def balance_deposit(self):
        self.balance = int(self.balance) + int(input())
        return self.balance


