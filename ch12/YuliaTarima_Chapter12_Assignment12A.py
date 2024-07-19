"""
This program loads the student data from the CSV file 
into a numpy array and prints the first 3 rows in a tabular format.

It calculates and prints the following statistics for each exam
(columns):
    Mean (average)
    Median
    Standard deviation
    Minimum
    Maximum

Then it calculates and print the overall statistics 
for the entire dataset (all exams combined):
    Mean (average) grade across all exams 
    Median grade across all exams 
    Standard deviation of grades across all exams 
    Minimum grade across all exams 
    Maximum grade across all exams 

It determines and prints the number of students who passed and failed 
each exam considering a passing grade as 60 or above.

It also calculates and print the overall pass percentage 
across all exams.
"""

import csv
import numpy as np


def load_data(filename):
    """Load data from a CSV file and return as a NumPy array."""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append([float(row['Exam 1']), float(row['Exam 2']),
                         float(row['Exam 3'])])
        return np.array(data)


def print_statistics(exam_grades, exam_name):
    """Print statistics for a given exam."""
    print(f"\n{exam_name}:")
    print(f"  Mean: {np.mean(exam_grades):.2f}")
    print(f"  Median: {np.median(exam_grades):.2f}")
    print(f"  Standard deviation: {np.std(exam_grades):.2f}")
    print(f"  Minimum: {np.min(exam_grades):.2f}")
    print(f"  Maximum: {np.max(exam_grades):.2f}")


def main():
    # Load data from the CSV file
    grades = load_data('grades.csv')

    # Print the first 3 rows
    print("\n-----------------------\n"
          "First 3 rows of the data:"
          "\n-----------------------")
    for row in grades[:3]:
        print(f"{row}")

    # Calculate and print statistics for each exam
    print("\n----------------------\n"
          "Statistics for each exam:"
          "\n----------------------")
    exam_names = ['Exam 1', 'Exam 2', 'Exam 3']
    for i, exam_name in enumerate(exam_names):
        exam_grades = grades[:, i]
        print_statistics(exam_grades, exam_name)

    # Calculate overall statistics across all exams
    all_grades = grades.flatten()
    print("\n----------------------------------\n"
          "Overall statistics across all exams:"
          "\n----------------------------------")
    print_statistics(all_grades, "All Exams")

    # Determine the number of students who passed and failed each exam
    passing_grade = 60
    print("\n---------------------------------\n"
          "Pass/Fail statistics for each exam:"
          "\n---------------------------------")
    for i, exam_name in enumerate(exam_names):
        exam_grades = grades[:, i]
        num_passed = np.sum(exam_grades >= passing_grade)
        num_failed = len(exam_grades) - num_passed
        print(f"\n{exam_name}:")
        print(f"  Number passed: {num_passed}")
        print(f"  Number failed: {num_failed}")

    # Calculate overall pass percentage across all exams
    num_students = len(all_grades)
    num_passed_total = np.sum(all_grades >= passing_grade)
    pass_percentage = (num_passed_total / num_students) * 100
    print(
        f"\n--------------------------------------\n"
        "Overall pass percentage across all exams:"
        "\n---------------------------------------\n"
        f"{pass_percentage:.2f}%"
    )


if __name__ == "__main__":
    main()