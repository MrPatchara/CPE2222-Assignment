# โปรแกรมแปลงตัวเลขเป็น Roman Numerals และแปลง Roman Numerals เป็นตัวเลข
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

def convert_range_to_roman(start, end):
    """แปลงช่วงตัวเลขเป็น Roman Numerals"""
    if start > end:
        return "Invalid range. Start number must be less than or equal to end number."
    roman_list = {i: int_to_roman(i) for i in range(start, end + 1)}
    return roman_list


# เพิ่มโหมดการแปลงช่วงตัวเลข
while True:
    print("\nRoman Numeral Converter (With Range Conversion)")
    print("1. Convert single number to Roman numeral")
    print("2. Convert Roman numeral to number")
    print("3. Convert range of numbers to Roman numerals")
    print("4. Exit")
    
    choice = input("Choose an option (1/2/3/4): ")
    
    if choice == "1":
        try:
            number = int(input("Enter a number (1 - 1,000,000): "))
            print(f"The Roman numeral of {number} is: {int_to_roman(number)}")
        except ValueError:
            print("Please enter a valid number.")
    
    elif choice == "2":
        roman = input("Enter a Roman numeral: ").upper()
        result = roman_to_int(roman)
        print(f"The number of Roman numeral '{roman}' is: {result}")
    
    elif choice == "3":
        try:
            start = int(input("Enter the start number: "))
            end = int(input("Enter the end number: "))
            roman_range = convert_range_to_roman(start, end)
            print("Roman numerals in the range:")
            for num, roman in roman_range.items():
                print(f"{num}: {roman}")
        except ValueError:
            print("Please enter valid numbers.")
    
    elif choice == "4":
        print("Exiting the converter. Goodbye!")
        break
    
    else:
        print("Invalid option. Please choose again.")
