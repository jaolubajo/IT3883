# Program Name: Assignment1.py
# Course: IT3883/Section W02
# Student Name: Jeffrey Olubajo
# Assignment Number: Assignment1
# Due Date: 1/27/2024
# Purpose: What does the program do (in a few sentences)? This [rpgram implements a text based menu. With 4 option as well.
# List Specific resources used to complete the assignment.
def text_menu():
    input_buffer =""
    while True:
        # this part of the code displays the menu
        print("\nText-Based Menu:")
        print("1. Append data to the input buffer")
        print("2. Clear the input buffer")
        print("3. Display the input buffer")
        print("4. Exit the program")
        # this gathers a user choice
        try:
            choice = int(input("\nEnter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Enter a number between 1 and 4.")
            continue
        # this processes user choice
        if choice == 1:
            data = input("Enter string to append: ")
            input_buffer += data
            print("Data appended.")
        elif choice == 2:
            input_buffer = ""
            print("Input buffer has been cleared.")
        elif choice == 3:
            print("\nCurrent input buffer:")
            if input_buffer:
                print(input_buffer)
            else:
                print("The input buffer is empty.")
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")
if __name__ == "__main__":
    text_menu()
