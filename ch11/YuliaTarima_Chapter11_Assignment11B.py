# YuliaTarima_Chapter11_Assignment11B

"""
Using the inheritance approach, class definition of Money
is implemented so that addition, multiplication,
and subtraction are all supported.

A test function ensures that all the operations
from the Money class work.
"""

import math


def calculate_hypotenuse(angle_degrees, adjacent_side):
    """
    Calculate the length of the hypotenuse of a right triangle.

    :param angle_degrees: The angle in degrees adjacent to the given side.
    :param adjacent_side: The length of the side adjacent to the given angle.
    :return: The length of the hypotenuse.
    """
    # Convert the angle from degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate the hypotenuse using the cosine function
    hypotenuse = adjacent_side / math.cos(angle_radians)

    return hypotenuse


def get_valid_angle():
    """
    Prompt the user to enter a valid angle (more than 0 and less than 90 degrees).
    :return: A valid angle in degrees.
    """
    while True:
        try:
            angle_degrees = float(input(
                "Enter the angle in degrees (more than 0 and less than 90): "))
            if 0 < angle_degrees < 90:
                return angle_degrees
            else:
                print(
                    "Invalid angle. Must be more than 0 and less than 90 degrees.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    # Get a valid angle from the user
    angle_degrees = get_valid_angle()

    # Input the length of the adjacent side
    while True:
        try:
            adjacent_side = float(
                input("Enter the length of the adjacent side: "))
            if adjacent_side > 0:
                break
            else:
                print(
                    "The length of the side "
                    "must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Calculate the hypotenuse
    hypotenuse = calculate_hypotenuse(angle_degrees, adjacent_side)

    # Print the result
    print(f"The length of the hypotenuse is: {hypotenuse:.2f}")


if __name__ == "__main__":
    main()
