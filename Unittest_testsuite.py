import unittest
from BankAccount import BankAccount
BankAccount2 = BankAccount("20000")
BankAccount1 = BankAccount("10000")


class BankingUnitTest(unittest.TestCase):

    def test_balance(self):
    #    balance = BankAccount2.get_balance()
        self.assertEqual(BankAccount1.get_balance(), 10000)

    def test_Withdraw(self):
        amount = 10
        self.assertEqual(BankAccount2.balance_withdrawl(int(amount)), 19990)



if __name__ == '__main__':
    unittest.main()
