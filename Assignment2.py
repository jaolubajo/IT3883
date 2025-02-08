# Program Name: Assignment2.py
# Course: IT3883/Section W02
# Student Name: Jeffrey Olubajo
# Assignment Number: Assignment2
# Due Date: 2/7/2024
# Purpose: This program grathers the score from the given file and averages them out. The average is then put in descending order.
# List Specific resources used to complete the assignment.
def calculate_avg(scores):
    # calculates the average score of the grades
    return sum(scores) / len(scores)
def process_file(file_name):
    # processes the file and averages their score
    students = []
    with open(file_name, "r") as file:
        for line in file:
            # Split the line into names and scores
            parts = line.strip().split()
            name = parts[0]
            scores = list(map(float, parts[1:]))  # turns the score to a float
            # calculates the average score
            avg = calculate_avg(scores)
            # appends the student name and average to the list
            students.append((name, avg))
    return students
def sort_and_print_students(students):
    # sorts them in descending order
    students.sort(key=lambda x: x[1], reverse=True)
    # prints the results
    for student in students:
        print(f"{student[0]} {student[1]:.2f}")
if __name__ == "__main__":
    file_name = 'input.txt'
    students = process_file(file_name)
    sort_and_print_students(students)
