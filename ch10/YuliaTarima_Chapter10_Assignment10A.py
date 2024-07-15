# YuliaTarima_Chapter9_Assignment9A

"""
Using the inheritance approach, class definition of Money
is implemented so that addition, multiplication,
and subtraction are all supported.

A test function ensures that all the operations
from the Money class work.
"""

# Import the Decimal class from the decimal module
from decimal import Decimal


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


# Define a function to test the Money class
def test_money_class():
    # Create two Money instances with USD units
    m1 = Money('100.50', 'USD')
    m2 = Money('20.75', 'USD')

    # Print the Money instances
    print(f'm1: {m1}')
    print(f'm2: {m2}')

    # Test addition of two Money instances
    m3 = m1 + m2
    print(f'm1 + m2 = {m3}')

    # Test subtraction of two Money instances
    m4 = m1 - m2
    print(f'm1 - m2 = {m4}')

    # Test multiplication of Money instance with an int
    m5 = m1 * 2
    print(f'm1 * 2 = {m5}')

    # Test reflected multiplication of Money instance with an int
    m6 = 3 * m2
    print(f'3 * m2 = {m6}')

    # Test invalid operation:
    # addition of Money instances with different units
    try:
        m7 = m1 + Money('50.25', 'EUR')
    except AssertionError as e:
        # Catch and print the AssertionError message
        print(f"AssertionError: {e}")


# Execute the test function if this script is run directly
if __name__ == "__main__":
    test_money_class()
