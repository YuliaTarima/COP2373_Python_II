# YuliaTarima_Chapter13_Assignment13_DB
"""
Using Python SQLite3 module this program creates a database
called population_YT containing a table named population with the
following fields:
    1. city,
    2. year,
    3. population.

The city-population data pairs of 10 most visited cities in Florida
are inserted into the population table for the year 2023:

    1. city = key from "cities"
    2. year = 2023
    3. population = value from "Cities"

    cities = {
        "Miami": 467963,
        "Orlando": 307573,
        "Tampa": 406000,
        "Fort Lauderdale": 193000,
        "Jacksonville": 949611,
        "Naples": 22100,
        "Sarasota": 58200,
        "West Palm Beach": 117600,
        "Key West": 28200,
        "St. Petersburg": 258000
    }


The program uses a function to simulate population growth
for the next 20 years at a 2% growth rate for each year.
Then it insert this data into the population table.

Via the function that uses matplotlib, the program shows the
population growth for a city. The user is displayed the 10 cities
as options and prompted to choose one, after which the population
growth for the city is displayed to the user visually.
"""
import sqlite3
import os
import matplotlib.pyplot as plt

# Path to the SQLite database file
db_path = 'population_YT.db'

"""Delete the existing SQLite database file if it exists."""


def delete_existing_db(db_path):
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Deleted existing database: {db_path}")
    else:
        print("No existing database to delete.")


"""Create a new SQLite database and populate it with data."""


def create_and_populate_db():
    delete_existing_db(db_path)

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
        ''')

        # Data to be inserted into the database
        cities = {
            "Miami": 467963,
            "Orlando": 307573,
            "Tampa": 406000,
            "Fort Lauderdale": 193000,
            "Jacksonville": 949611,
            "Naples": 22100,
            "Sarasota": 58200,
            "West Palm Beach": 117600,
            "Key West": 28200,
            "St. Petersburg": 258000
        }

        # Clear the table to remove old data for the year 2023
        cursor.execute('DELETE FROM population WHERE year = 2023')

        # Insert the city-population data into the table for the
        # year 2023
        for city, population in cities.items():
            cursor.execute('''
            INSERT INTO population (city, year, population)
            VALUES (?, ?, ?)
            ''', (city, 2023, population))

        # Simulate population growth for the next 20 years at a 2%
        # growth rate
        simulate_population_growth(cursor, cities, start_year=2024,
                                   num_years=20, growth_rate=0.02)

        # Commit the transaction
        conn.commit()

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    finally:
        if conn:
            conn.close()


def simulate_population_growth(cursor, cities, start_year, num_years,
                               growth_rate):
    """Simulate population growth for the given number of years and
    insert the data into the database."""
    try:
        for city, initial_population in cities.items():
            population = initial_population
            for year in range(start_year, start_year + num_years):
                population = int(population * (1 + growth_rate))
                cursor.execute('''
                INSERT INTO population (city, year, population)
                VALUES (?, ?, ?)
                ''', (city, year, population))
    except sqlite3.Error as e:
        print(f"SQLite error during simulation: {e}")


def print_table_contents(cursor, city=None, year=None,
                         population=None):
    """
    Print the contents of the table based on optional filters.

    :param cursor: The SQLite cursor object.
    :param city: Filter by city name (optional).
    :param year: Filter by year (optional).
    :param population: Filter by population (optional).
    """
    query = 'SELECT * FROM population WHERE 1=1'
    params = []

    if city:
        if not isinstance(city, str):
            raise ValueError("City must be a string.")
        query += ' AND city = ?'
        params.append(city)

    if year:
        if not isinstance(year, int):
            raise ValueError("Year must be an integer.")
        query += ' AND year = ?'
        params.append(year)

    if population:
        if not isinstance(population, int):
            raise ValueError("Population must be an integer.")
        query += ' AND population = ?'
        params.append(population)

    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()

        print("Population Table:")
        print("{:<20} {:<4} {:<10}".format('City', 'Year',
                                           'Population'))
        print('-' * 34)
        for row in rows:
            print(
                "{:<20} {:<4} {:<10}".format(row[0], row[1], row[2]))

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")


def plot_population_growth(city):
    """Plot the population growth for the selected city."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
        SELECT year, population FROM population WHERE city = ?
        ORDER BY year
        ''', (city,))
        rows = cursor.fetchall()

        if not rows:
            print(f"No data found for city: {city}")
            return

        # Extract years and populations
        years, populations = zip(*rows)

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(years, populations, marker='o')
        plt.title(f"Population Growth for {city}")
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.grid(True)
        plt.show()

    except sqlite3.Error as e:
        print(f"SQLite error during plotting: {e}")

    finally:
        if conn:
            conn.close()


def select_city_and_plot():
    """Prompt user to select a city, print the table for that city,
    and display the population growth."""
    cities = [
        "Miami", "Orlando", "Tampa", "Fort Lauderdale",
        "Jacksonville", "Naples", "Sarasota", "West Palm Beach",
        "Key West", "St. Petersburg"
    ]

    print("\nAvailable Cities:")
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city}")

    while True:
        try:
            choice = int(input(
                "\nEnter the number of the city to plot its "
                "population growth: "))
            if 1 <= choice <= len(cities):
                selected_city = cities[choice - 1]
                # Print table for the selected city
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                print_table_contents(cursor, city=selected_city)
                conn.close()
                # Plot the population growth for the selected city
                plot_population_growth(selected_city)
                break
            else:
                print(
                    "Invalid choice. Please enter a number between "
                    "1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    # Create and populate the database
    create_and_populate_db()

    # Prompt user to select a city and display the population growth
    select_city_and_plot()


if __name__ == "__main__":
    main()