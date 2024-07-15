# YuliaTarima_Chapter10_Assignment10B

"""
Using the inheritance approach, class definition of Money
is implemented so that addition, multiplication,
and subtraction are all supported.

A test function ensures that all the operations
from the Money class work.
"""

# Import the Decimal class from the decimal module
from decimal import Decimal
import unittest


# Define a Money class that inherits from Decimal
class Money(Decimal):
    # Define a custom __new__ method for object creation
    def __new__(cls, v, units='USD'):
        # Call the parent class's __new__ method
        # to create a new instance
        return super(Money, cls).__new__(cls, v)

    # Define the initialization method
    def __init__(self, v, units='USD'):
        # Initialize the Decimal part without any arguments
        super().__init__()
        # Set the amount as a Decimal
        self._amount = Decimal(v)
        # Set the currency units
        self.units = units

    # Define a custom string representation method
    def __repr__(self):
        # Return a string that includes the class name, amount,
        # and units
        return f'{self.__class__.__name__}({float(self)}, {self.units})'

    # Define the addition method
    def __add__(self, other):
        # Check if the other operand is a Money instance
        if isinstance(other, Money):
            # Ensure both Money instances have the same currency units
            assert self.units == other.units, \
                "Cannot add money with different units"
            # Return a new Money instance with the summed amount
            return Money(self._amount + other._amount, self.units)
        # If the other operand is not a Money instance,
        # return NotImplemented
        return NotImplemented

    # Define the subtraction method
    def __sub__(self, other):
        # Check if the other operand is a Money instance
        if isinstance(other, Money):
            # Ensure both Money instances have the same currency units
            assert self.units == other.units, \
                "Cannot subtract money with different units"
            # Return a new Money instance with the subtracted amount
            return Money(self._amount - other._amount, self.units)
        # If the other operand is not a Money instance,
        # return NotImplemented
        return NotImplemented

    # Define the multiplication method
    def __mul__(self, other):
        # Check if the other operand is an int or float
        if isinstance(other, (int, float)):
            # Return a new Money instance with the multiplied amount
            return Money(self._amount * Decimal(other), self.units)
        # If the other operand is not an int or float,
        # return NotImplemented
        return NotImplemented

    # Define the reflected multiplication method
    def __rmul__(self, other):
        # Use the __mul__ method for reflected multiplication
        return self.__mul__(other)


class BankAcct(Money):
    def __new__(cls, name, account_number, initial_amount,
                interest_rate):
        # Call the parent class's __new__ method to create a new instance
        return super(BankAcct, cls).__new__(cls, initial_amount)

    def __init__(self, name, account_number, initial_amount,
                 interest_rate):
        # Initialize using parent class Money's __init__
        super().__init__(initial_amount, 'USD')
        self.name = name
        self.account_number = account_number
        self.interest_rate = Decimal(str(interest_rate))

    def adjust_interest_rate(self, new_rate):
        # Adjust the interest rate to a new value
        self.interest_rate = new_rate

    def withdraw(self, amount):
        # Withdraw from the account if sufficient balance is available
        amount = Money(amount, 'USD')
        if amount > Money(0, 'USD') and amount <= self:
            self._amount -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        # Deposit an amount into the account if the amount is positive
        amount = Money(amount, 'USD')
        if amount > Money(0, 'USD'):
            self._amount += amount
            return True
        else:
            return False

    def balance(self):
        # Return the current balance of the account
        return self._amount

    def calculate_interest(self, days):
        # Calculate interest earned over a given number of days
        daily_interest = self._amount * (
                    self.interest_rate / Decimal('100')) / Decimal(
            '365')
        return daily_interest * days

    def __str__(self):
        # Return a string representation of the account information
        return (f"Account Summary:"
                f"\n____________________"
                f"\nName: {self.name}"
                f"\nAccount Number: {self.account_number}"
                f"\nCurrent Balance: ${self._amount:.1f}"
                f"\nInterest Rate: {self.interest_rate}%")


# Define the TestBankAcct class
# to test the functionalities of the BankAcct class
class TestBankAcct(unittest.TestCase):
    separator = "____________________________________\n"

    def setUp(self):
        # Set up the test case with an initial bank account instance
        self.account = BankAcct("John Doe", "1234567890", 1000.0, 2.5)

    def test_initial_balance(self):
        print(self.separator + "Testing initial balance")
        # Compare expected and actual results; Print error message
        # if test fails
        self.assertEqual(self.account.balance(), 1000.0,
                         "Error: Initial balance should be 1000.0")
        # Print success message if test passes
        print("Success: test_initial_balance passed")

    def test_adjust_interest_rate(self):
        print(self.separator + "Testing interest rate adjustment")
        self.account.adjust_interest_rate(3.0)
        # Compare expected and actual results; Print error message
        # if test fails
        self.assertEqual(self.account.interest_rate, 3.0,
                         "Error: Interest rate should be adjusted "
                         "to 3.0")
        # Print success message if test passes
        print("Success: test_adjust_interest_rate passed")

    def test_deposit(self):
        print(self.separator + "Testing deposit functionality")
        self.account.deposit(500.0)
        # Compare expected and actual results; Print error message
        # if test fails
        self.assertEqual(self.account.balance(), 1500.0,
                         "Error: Balance should be 1500.0 after "
                         "depositing 500.0")
        # Print success message if test passes
        print("Success: test_deposit passed")

    def test_deposit_zero(self):
        print(self.separator + "Testing deposit of zero amount")
        success = self.account.deposit(0)
        # Compare expected and actual results; Print error message
        # if test fails
        self.assertFalse(success,
                         "Error: Depositing zero should fail")
        self.assertEqual(self.account.balance(), 1000.0,
                         "Balance should remain unchanged after "
                         "attempting to deposit zero")
        # Print success message if test passes
        print("Success: test_deposit_zero passed")

    def test_deposit_negative(self):
        print(self.separator + "Testing deposit of negative amount")
        success = self.account.deposit(-100)
        # Compare expected and actual results; Print error message
        # if test fails
        self.assertFalse(success,
                         "Error: Depositing a negative amount "
                         "should fail")
        self.assertEqual(self.account.balance(), 1000.0,
                         "Error: Balance should remain unchanged "
                         "after attempting to deposit a negative "
                         "amount")
        # Print success message if test passes
        print("Success: test_deposit_negative passed")

    def test_withdraw(self):
        print(self.separator + "Testing withdrawal functionality")
        self.account.withdraw(200.0)
        # Compare expected and actual results; Print error message
        # if test fails
        self.assertEqual(self.account.balance(), 800.0,
                         "Error: Balance should be 800.0 after "
                         "withdrawing 200.0")
        # Print success message if test passes
        print("Success: test_withdraw passed")

    def test_withdraw_more_than_available(self):
        print(
            self.separator + "Testing withdrawal of amount greater "
                             "than available balance")
        success = self.account.withdraw(1500.0)
        # Compare expected and actual results; Print error message
        # if test fails
        self.assertFalse(success,
                         "Error: Withdrawal of amount greater than "
                         "available balance should fail")
        self.assertEqual(self.account.balance(), 1000.0,
                         "Error: Balance should remain unchanged "
                         "after failed withdrawal")
        # Print success message if test passes
        print("Success: test_withdraw_more_than_available passed")

    def test_calculate_interest(self):
        print(
            self.separator + "Testing interest calculation over a "
                             "given number of days")
        interest = self.account.calculate_interest(30)
        expected_interest = self.account.balance() * (
                Decimal('2.5') / Decimal('100')) / Decimal(
            '365') * Decimal('30')
        # Compare expected and actual results; Print error message
        # if test fails
        self.assertAlmostEqual(interest, expected_interest,
                               msg="Error: Calculated interest "
                                   "should match the expected "
                                   "interest for 30 days")
        # Print success message if test passes
        print("Success: test_calculate_interest passed")

    def test_str(self):
        print(
            self.separator + "Testing string representation of the "
                             "account summary")
        account_str = str(self.account)
        expected_str = (f"Account Summary:"
                        f"\n____________________"
                        f"\nName: John Doe"
                        f"\nAccount Number: 1234567890"
                        f"\nCurrent Balance: $1000.0"
                        f"\nInterest Rate: 2.5%")
        # Compare expected and actual results; Print error message
        # if test fails
        self.assertEqual(account_str, expected_str,
                         "Error: String representation of the "
                         "account should match the expected format")
        # Print success message if test passes
        print("Success: test_str passed")


# Define the main function to run the tests
def main():
    # Running the tests
    unittest.main()


# If the script is run directly, execute the main function
if __name__ == "__main__":
    main()
