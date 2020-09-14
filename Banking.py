from BankAccount import BankAccount
ba = BankAccount(4000)
Currency = "DKK"
check = ba.balance
ba.balance_withdrawl(10)
if(ba.balance == check):
    print("Not enough money")
