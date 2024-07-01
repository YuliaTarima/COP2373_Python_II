# YuliaTarima_Chapter9_Assignment9A

"""
This program creates a BankAcct Class
with the following state information:
    name,
    account number,
    amount
    interest rate.

In addition to an __init__ method,
the BankAcct Class supports methods for:
    adjusting the interest rate,
    withdrawing and depositing,
    giving a balance,
    calculating the interest earned based on the number of days.
The __str__ method is used to display balances and interest amounts.

The program contains unit tests for methods in the BankAcct Class.
"""
import unittest


# Define the BankAcct class to describe/represent a bank account
class BankAcct:
    def __init__(self, name, account_number, initial_amount,
                 interest_rate):
        # Initialize the bank account with the provided details
        self.name = name
        self.account_number = account_number
        self.amount = initial_amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        # Adjust the interest rate to a new value
        self.interest_rate = new_rate

    def withdraw(self, amount):
        # Withdraw from the account if sufficient balance is available
        if 0 < amount <= self.amount:
            self.amount -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        # Deposit an amount into the account if the amount is positive
        if amount > 0:
            self.amount += amount
            return True
        else:
            return False

    def balance(self):
        # Return the current balance of the account
        return self.amount

    def calculate_interest(self, days):
        # Calculate interest earned over a given number of days
        daily_interest = self.amount * (
                self.interest_rate / 100) / 365
        return daily_interest * days

    def __str__(self):
        # Return a string representation of the account information
        return (f"Account Summary:"
                f"\n____________________"
                f"\nName: {self.name}"
                f"\nAccount Number: {self.account_number}"
                f"\nCurrent Balance: ${self.amount}"
                f"\nInterest Rate: {self.interest_rate}%")


# Define the TestBankAcct class
# to test the functionalities of the BankAcct class
class TestBankAcct(unittest.TestCase):
    def setUp(self):
        # Set up the test case with an initial bank account instance
        self.account = BankAcct("John Doe", "1234567890", 1000.0, 2.5)

    def test_initial_balance(self):
        # Test if the initial balance is correctly set
        self.assertEqual(self.account.balance(), 1000.0,
                         "Initial balance should be 1000.0"
                         )

    def test_adjust_interest_rate(self):
        # Test if the interest rate adjustment works correctly
        self.account.adjust_interest_rate(3.0)
        self.assertEqual(self.account.interest_rate, 3.0,
                         "Interest rate should be adjusted to 3.0"
                         )

    def test_deposit(self):
        # Test if deposit functionality works correctly
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance(), 1500.0,
                         "Balance should be 1500.0 "
                         "after depositing 500.0"
                         )

    def test_deposit_zero(self):
        # Test if depositing zero amount is handled correctly
        success = self.account.deposit(0)
        self.assertFalse(success, "Depositing zero should fail")
        self.assertEqual(self.account.balance(), 1000.0,
                         "Balance should remain unchanged after "
                         "attempting to deposit zero"
                         )

    def test_deposit_negative(self):
        # Test if depositing a negative amount is handled correctly
        success = self.account.deposit(-100)
        self.assertFalse(success,
                         "Depositing a negative amount should fail")
        self.assertEqual(self.account.balance(), 1000.0,
                         "Balance should remain unchanged after "
                         "attempting to deposit a negative amount"
                         )

    def test_withdraw(self):
        # Test if withdrawal functionality works correctly
        self.account.withdraw(200.0)
        self.assertEqual(self.account.balance(), 800.0,
                         "Balance should be 800.0 after "
                         "withdrawing 200.0"
                         )

    def test_withdraw_more_than_available(self):
        # Test if withdrawing more than the available balance
        # is handled correctly
        success = self.account.withdraw(1500.0)
        self.assertFalse(success,
                         "Withdrawal of amount greater than "
                         "available balance should fail"
                         )
        self.assertEqual(self.account.balance(), 1000.0,
                         "Balance should remain unchanged "
                         "after failed withdrawal"
                         )

    def test_calculate_interest(self):
        # Test interest calculation over a given number of days
        interest = self.account.calculate_interest(30)
        expected_interest = self.account.amount * (
                2.5 / 100) / 365 * 30
        self.assertAlmostEqual(interest, expected_interest,
                               msg="Calculated interest should match "
                                   "the expected interest for 30 days"
                               )

    def test_str(self):
        # Test the string representation of the account summary
        account_str = str(self.account)
        expected_str = (f"Account Summary:"
                        f"\n____________________"
                        f"\nName: John Doe"
                        f"\nAccount Number: 1234567890"
                        f"\nCurrent Balance: $1000.0"
                        f"\nInterest Rate: 2.5%")
        self.assertEqual(account_str, expected_str,
                         "String representation of the account "
                         "should match the expected format"
                         )


# Define the main function to run the tests
def main():
    # Running the tests
    unittest.main()


# If the script is run directly, execute the main function
if __name__ == "__main__":
    main()
