# YuliaTarima_ChapterX_AssignmentCSV

"""
This application aids to an instructor that teaches a class
in which each student takes three exams.

The program allows an instructor to input
first and last name as strings
and three exam grades as integers
per student
for the unlimited number of students.

The information is stored in a grades.csv file for later use.
The csv module is used to write each record into the grades.csv file
with a header of First Name, Last Name, Exam 1, Exam 2 and Exam3.
Each student represents a record in the grades.csv file.

A separate program reads the grades.csv file and displays the data
in tabular format.
"""

import csv


# Function to validate input for student's name (letters only)
def input_valid_name(input_type):
    while True:
        # Prompt user for input
        name = input(
            f"Enter the student's {input_type} name (letters only): ")
        # Check if input contains only alphabetic characters
        if name.isalpha():
            return name  # Return valid name
        else:
            print(
                f"Invalid {input_type} name. "
                f"Please enter letters only.")


# Function to validate input for student's grade
# (numeric and non-negative)
def input_valid_grade(exam_number):
    while True:
        try:
            # Prompt user for input
            grade = float(input(
                f"Enter the student's grade "
                f"for Exam {exam_number}: "))
            # Ensure grade is non-negative
            if grade >= 0:
                return grade  # Return valid grade
            else:
                print(
                    "Invalid grade. "
                    "Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Main function to input student grades and write to grades.csv
def input_student_grades():
    # Open the grades.csv file in write mode
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(
            ["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop to input data for each student
        while True:
            # Get valid first and last names for the student
            first_name = input_valid_name("first")
            last_name = input_valid_name("last")

            # Input grades for three exams
            exam1 = input_valid_grade(1)
            exam2 = input_valid_grade(2)
            exam3 = input_valid_grade(3)

            # Write the student's data as a new row in the CSV file
            writer.writerow(
                [first_name, last_name, exam1, exam2, exam3])

            # Ask if the user wants to add another student
            add_another = input(
                "Do you want to add another student? "
                "(yes/no): ").lower()
            if add_another != 'yes':
                # Exit loop if user another student is not to be added
                break

    # Confirmation message after writing all grades
    print("\n___________________________________________________"
          "\nGrades have been successfully written to grades.csv.")


# Entry point of the program
if __name__ == "__main__":
    input_student_grades()
