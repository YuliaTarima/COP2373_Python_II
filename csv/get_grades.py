import csv
"""
This Python script reads and displays the contents of a CSV file 
named grades.csv in a tabular format. 
"""
def read_and_display_grades():
    # Open the grades.csv file in read mode
    with open('grades.csv', 'r') as file:
        reader = csv.reader(file)
        # Read the header
        header = next(reader)
        # Print the header
        print("-" * 55)
        print(f"{header[0]:<15} {header[1]:<15} "
              f"{header[2]:<7} {header[3]:<7} {header[4]:<7}")
        print("-" * 55)

        # Loop through each row in the CSV file
        for row in reader:
            # Print the student data in tabular format
            print(
                f"{row[0]:<15} {row[1]:<15} {row[2]:<7} {row[3]:<7} {row[4]:<7}")


if __name__ == "__main__":
    read_and_display_grades()
