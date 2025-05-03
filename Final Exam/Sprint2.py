# Program Name: Sprint1.py
# Course: IT3883/Section W02
# Student Name: Jeffrey Olubajo
# Assignment Number: Final Exam
# Due Date: 5/3/2025

# Sprint 2
def calc_total(sentence):
    coins = {
        "penny": 0.01,
        "nickel": 0.05,
        "dime": 0.10,
        "quarter": 0.25
    }
    # split the sentence with 'and'
    sentence = sentence.replace(" and ", ", ")
    phrases = sentence.split(", ")
    total = 0.0

    for phrase in phrases:
        parts = phrase.strip().split()
        quantity = int(parts[0])
        denom = parts[1].lower()

        # adjust plural denominations
        if denom.endswith('ies'):  # e.g., pennies
            denom = denom[:-3] + 'y' # removes the last 3 characters
        elif denom.endswith('s'):  # e.g., nickels
            denom = denom[:-1] # removes the last character
        value = coins.get(denom, 0)
        total += quantity * value
    return f"{total: .2f}"

# Tests
print(calc_total("1 nickel and 17 quarters"))  # 4.30
print(calc_total("21 pennies and 17 dimes and 52 quarters"))  # 14.91
print(calc_total("1 dime and 1 nickel and 1 penny and 1 quarter"))  # 0.41
print(calc_total("21 nickels and 15 pennies "))  # 1.2
print(calc_total("4 dimes and 7 quarters "))  # 2.15
