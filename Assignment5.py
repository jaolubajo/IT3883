# Program Name: Assignment5.py
# Course: IT3883/Section W02
# Student Name: Jeffrey Olubajo
# Assignment Number: Assignment 5
# Due Date: 4/18/2025
# Purpose: What does the program do (in a few sentences)?This program uses the text file to compute the average temperature.
# List Specific resources used to complete the assignment.
import sqlite3

# connecting to sql database
connect = sqlite3.connect("temperature_readings.db")
cursor = connect.cursor()

# table creation
cursor.execute("""
    CREATE TABLE IF NOT EXISTS TemperatureData (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT,
        Temperature_Value REAL
    )
""")

# uses the linked file
with open("Assignment5input.txt", "r") as file:
    for line in file:
        if line.strip():
            try:
                Day_Of_Week, Temperature_Value = line.strip().split()
                cursor.execute(
                    "INSERT INTO TemperatureData (Day_Of_Week, Temperature_Value) VALUES (?, ?)",
                    (Day_Of_Week, float(Temperature_Value))
                )
            except ValueError:
                print(f"Skipped (invalid format): {line.strip()}")

# helps print and calculate averages temp.
for day in ['Sunday', 'Thursday']:
    cursor.execute("SELECT AVG(Temperature_Value) FROM TemperatureData WHERE Day_Of_Week = ?", (day,))
    avg = cursor.fetchone()[0]
    if avg is not None:
        print(f"Average temperature for {day}: {avg:.2f}°F")
    else:
        print(f"No data available for {day}.")

# Save and close
connect.commit()
connect.close()

