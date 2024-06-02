# YuliaTarima_Chapter3_Assignment3A

"""
This application prompts for a list of user's monthly expenses:
type of expense and the amount.
It uses the reduce method to analyze the expenses
and display the total expense,
the highest expense and the lowest expense.
It labels what is the highest and lowest expense.
"""

from functools import reduce


def get_expenses():
    """
    Function to get the list of expenses from the user.
    Returns a list of tuples where each tuple contains (expense_type, amount).
    """
    expenses = []  # Initialize an empty list to store the expenses
    while True:
        # Prompt the user to enter the type of expense
        expense_type = input(
            "Enter the type of expense (or 'done' to finish): ")

        # Check if the user wants to finish input
        if expense_type.lower() == 'done':
            break

        try:
            # Prompt the user to enter the amount for the expense
            amount = float(
                input(f"Enter the amount for {expense_type}: "))
            # Append the expense as a tuple to the expenses list
            expenses.append((expense_type, amount))
        except ValueError:
            # Handle invalid amount value
            print("Invalid amount. Please enter a number.")
    # Return the list of expenses
    return expenses


# Function to analyze the expenses
def analyze_expenses(expenses):
    if not expenses:
        # If no expenses, return zero and None for highest and lowest
        return 0, None, None

    # Calculate the total expense using reduce
    total_expense = reduce(lambda acc, exp: acc + exp[1], expenses, 0)

    # Find the highest expense using reduce
    highest_expense = reduce(
        lambda acc, exp: acc if acc[1] > exp[1] else exp, expenses)

    # Find the lowest expense using reduce
    lowest_expense = reduce(
        lambda acc, exp: acc if acc[1] < exp[1] else exp, expenses)

    # Return tuple of (total_expense, highest_expense, lowest_expense)
    return total_expense, highest_expense, lowest_expense


# Main function to execute the program
# It gets the expenses, analyzes them, and prints the results.
def main():
    # Get the list of expenses from the user
    expenses = get_expenses()

    # Analyze expenses to get the total, highest, and lowest expenses
    total, highest, lowest = analyze_expenses(expenses)

    # Print the total expense
    print(f"\nTotal expense: ${total:.2f}")

    # Print the highest expense with a label
    if highest:
        print(f"Highest expense: {highest[0]} - ${highest[1]:.2f}")

    # Print the lowest expense with a label
    if lowest:
        print(f"Lowest expense: {lowest[0]} - ${lowest[1]:.2f}")


# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    # Run the main function
    main()