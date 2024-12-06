# โปรแกรมแปลงเลขฐาน 10 เป็นเลขโรมัน และเลขโรมันเป็นเลขฐาน 10
def int_to_roman(number):
    if number <= 0 or number > 1000000:
        return "Number out of range (must be 1 - 1,000,000)"
    
    roman_numerals = [
        ('M̅', 1000000), ('C̅M̅', 900000), ('D̅', 500000), ('C̅D̅', 400000),
        ('C̅', 100000), ('X̅C̅', 90000), ('L̅', 50000), ('X̅L̅', 40000),
        ('X̅', 10000), ('I̅X̅', 9000), ('V̅', 5000), ('I̅V̅', 4000),
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4),
        ('I', 1)
    ]

    result = ""
    for roman, value in roman_numerals:
        while number >= value:
            result += roman
            number -= value

    return result


def roman_to_int(roman):
    roman_numerals = {
        'M̅': 1000000, 'C̅M̅': 900000, 'D̅': 500000, 'C̅D̅': 400000,
        'C̅': 100000, 'X̅C̅': 90000, 'L̅': 50000, 'X̅L̅': 40000,
        'X̅': 10000, 'I̅X̅': 9000, 'V̅': 5000, 'I̅V̅': 4000,
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4,
        'I': 1
    }
    
    index = 0
    result = 0
    while index < len(roman):
        # Check for two-character symbols
        if index + 1 < len(roman) and roman[index:index + 2] in roman_numerals:
            result += roman_numerals[roman[index:index + 2]]
            index += 2
        # Check for one-character symbols
        elif roman[index] in roman_numerals:
            result += roman_numerals[roman[index]]
            index += 1
        else:
            return "Invalid Roman numeral"
    return result

import random

def roman_guessing_game():
    """เกมเดา Roman Numeral"""
    number = random.randint(1, 100)
    roman = int_to_roman(number)
    print("Welcome to the Roman Numeral Guessing Game!")
    print(f"Roman Numeral: {roman}")
    
    attempts = 3
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts}: Guess the number: "))
            if guess == number:
                print("Congratulations! Your guess is correct.")
                return
            elif guess < number:
                print("Hint: The number is higher.")
            else:
                print("Hint: The number is lower.")
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Sorry, you've used all attempts. The correct number was {number}.")

# โหมดเกม
while True:
    print("\nRoman Numeral Converter (Game Mode)")
    print("1. Play Roman Numeral Guessing Game")
    print("2. Exit")
    
    choice = input("Choose an option (1/2): ")
    
    if choice == "1":
        roman_guessing_game()
    
    elif choice == "2":
        print("Exiting the converter. Goodbye!")
        break
    
    else:
        print("Invalid option. Please choose again.")
