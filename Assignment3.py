# Program Name: Assignment3.py
# Course: IT3883/Section W02
# Student Name: Jeffrey Olubajo
# Assignment Number: Assignment3
# Due Date: 2/23/2024
# Purpose: This program is a GUI application that converts miles per gallon to kilometers per liter.
# List Specific resources used to complete the assignment.

import tkinter as tk
# Conversion
def mpg_kpl(mpg):
    try:
        input_mpg = float(mpg)
        kpl = input_mpg * .425143707
        return round(kpl,2)
    except ValueError:
        return "Invalid input"

# Updating the result when an input is placed
def result(*args):
    mpg = mpg_entry.get()
    result = mpg_kpl(mpg)
    kpl_label.config(text= f"{result} Kilometers per Liter")
# Create window
root = tk.Tk()
# Title
root.title("MPG to KPL")
# Size
root.geometry("500x250")
# Input call
instruction_label = tk.Label(root, text= "Miles per Gallon (mpg):")
instruction_label.pack(pady=10)
# Where the user inputs entry
mpg_entry = tk.Entry(root, font=("Arial", 12))
mpg_entry.pack(pady=10)
# Result display
kpl_label= tk.Label(root, text= "0.00 Kilometers per Liter", font=("Arial",12))
kpl_label.pack(pady=20)
mpg_entry.bind("<KeyRelease>", result)
root.mainloop()
