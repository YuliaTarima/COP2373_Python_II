# YuliaTarima_Chapter6_Assignment6A

"""
This program prompts the user for a phone number, SSN, and zip code
to be entered in a specific format.
Then it validates the entries using regular expressions and displays
the validation results to the user.
"""

import re


# Function to validate phone numbers
def validate_phone_number(phone):
    # Regular expression for phone numbers in the format XXX-XXX-XXXX
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    # If phone number matches with pattern return, otherwise False
    return bool(pattern.match(phone))


# Function to validate social security numbers
def validate_ssn(ssn):
    # Regular expression pattern for SSNs in the format XXX-XX-XXXX
    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    # Match SSN with pattern, return True for match, otherwise False
    return bool(pattern.match(ssn))


# Function to validate zip codes
def validate_zip_code(zip_code):
    # Regular expression for zip codes formated XXXXX or XXXXX-XXXX
    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    # If zip code matches with pattern return True, otherwise False
    return bool(pattern.match(zip_code))


# Main function to get user input and display validation results
def main():
    # Prompt the user to enter a phone number
    phone = input("Enter a phone number (format: XXX-XXX-XXXX): ")
    # Prompt the user to enter a social security number
    ssn = input(
        "Enter a social security number (format: XXX-XX-XXXX): ")
    # Prompt the user to enter a zip code
    zip_code = input(
        "Enter a zip code (format: XXXXX or XXXXX-XXXX): ")

    print("\nHere are the validation results for your entries:")
    # Validate user phone number and display the result
    if validate_phone_number(phone):
        # If the phone number is valid, print a valid message
        print(f"\nThe phone number {phone} is valid.")
    else:
        # If the phone number is not valid, print an invalid message
        print(f"The phone number {phone} is invalid.")

    # Validate user SSN and display the result
    if validate_ssn(ssn):
        # If the SSN is valid, print a valid message
        print(f"The social security number {ssn} is valid.")
    else:
        # If the SSN is not valid, print an invalid message
        print(f"The social security number {ssn} is invalid.")

    # Validate user zip code and display the result
    if validate_zip_code(zip_code):
        # If the zip code is valid, print a valid message
        print(f"The zip code {zip_code} is valid.")
    else:
        # If the zip code is not valid, print an invalid message
        print(f"The zip code {zip_code} is invalid.")


# Test validation functions with various inputs
def test_validation_functions():
    # List of test phone numbers (both valid and invalid)
    test_phones = ["123-456-7890", "1234567890", "123-45-6789",
                   "987-654-3210"]
    # List of test social security numbers (both valid and invalid)
    test_ssns = ["123-45-6789", "123456789", "12-345-6789",
                 "987-65-4321"]
    # List of test zip codes (both valid and invalid)
    test_zip_codes = ["12345", "1234", "123456", "12345-6789",
                      "1234-5678"]

    # Test phone numbers
    print("\nTesting phone number validation:")
    for phone in test_phones:
        if validate_phone_number(phone):
            print(f"The phone number {phone} is valid.")
        else:
            print(f"The phone number {phone} is invalid.")

    # Test social security numbers
    print("\nTesting SSN validation:")
    for ssn in test_ssns:
        if validate_ssn(ssn):
            print(f"The social security number {ssn} is valid.")
        else:
            print(f"The social security number {ssn} is invalid.")

    # Test zip codes
    print("\nTesting zip code validation:")
    for zip_code in test_zip_codes:
        if validate_zip_code(zip_code):
            print(f"The zip code {zip_code} is valid.")
        else:
            print(f"The zip code {zip_code} is invalid.")


# Entry point of the script
if __name__ == "__main__":
    # Call the main function to execute the program
    main()
    # Call the testing function to test validation functions
    test_validation_functions()
