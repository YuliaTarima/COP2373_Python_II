# YuliaTarima_Chapter12_Assignment12A

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
    return np.genfromtxt(filename, delimiter=',', skip_header=1,
                         usecols=(2, 3, 4))


def calculate_statistics(exam_grades):
    """Calculate statistics for a given exam."""
    return np.array([
        np.mean(exam_grades),
        np.median(exam_grades),
        np.std(exam_grades),
        np.min(exam_grades),
        np.max(exam_grades)
    ])


def format_statistics_table(statistics, exam_names, table_title):
    """Format statistics in a tabular format."""
    headers = ["", "Mean", "Median", "Standard Deviation", "Minimum",
               "Maximum"]
    header_row = "{:<8} {:>8} {:>8} {:>19} {:>8} {:>8}".format(
        *headers)
    print(f"\n{table_title}")
    print("-" * len(header_row))
    print(header_row)
    print("-" * len(header_row))

    for exam_name, stats in zip(exam_names, statistics):
        stat_row = ("{:<8} {:>8.2f} {:>8.2f} {:>19.2f} {:>8.2f} {"
                    ":>8.2f}").format(
            exam_name, *stats)
        print(stat_row)
    print("-" * len(header_row))


def format_pass_fail_table(pass_fail_stats, exam_names):
    """Format pass/fail statistics in a tabular format."""
    headers = ["", "Number Passed", "Number Failed"]
    header_row = "{:<8} {:>14} {:>13}".format(*headers)
    print("\nPass/Fail Statistics for Each Exam:")
    print("-" * len(header_row))
    print(header_row)
    print("-" * len(header_row))

    for exam_name, stats in zip(exam_names, pass_fail_stats):
        stat_row = "{:<8} {:>14} {:>13}".format(exam_name, *stats)
        print(stat_row)
    print("-" * len(header_row))


def main():
    # Load data from the CSV file
    grades = load_data('grades.csv')

    # Print the first 3 rows
    print("\nFirst 3 Rows of Data:"
          "\n---------------------")
    for row in grades[:3]:
        print(f"{row}")
    print("---------------------")

    # Calculate statistics for each exam
    exam_names = ['Exam 1', 'Exam 2', 'Exam 3']
    statistics = np.apply_along_axis(calculate_statistics, 0, grades)
    format_statistics_table(statistics.T, exam_names,
                            "Statistics Per Each Exam:")

    # Calculate overall statistics across all exams
    overall_statistics = calculate_statistics(grades.flatten())
    format_statistics_table([overall_statistics], ["All Exams"],
                            "Overall Statistics Across All Exams:")

    # Determine the number of students who passed and failed each exam
    passing_grade = 60
    pass_fail_stats = [(np.sum(grades[:, i] >= passing_grade),
                        np.sum(grades[:, i] < passing_grade)) for i in
                       range(3)]
    format_pass_fail_table(pass_fail_stats, exam_names)

    # Calculate overall pass percentage across all exams
    num_students = grades.size
    num_passed_total = np.sum(grades >= passing_grade)
    pass_percentage = (num_passed_total / num_students) * 100
    print(f"\nOverall Pass Percentage Across All Exams:"
          f"\n---------------------------------------------------"
          f"\n{pass_percentage:.2f}%"
          f"\n---------------------------------------------------\n")


if __name__ == "__main__":
    main()