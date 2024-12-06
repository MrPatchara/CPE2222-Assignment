# โปรแกรมแปลง Binary เป็น Roman Numerals
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

def binary_to_decimal(binary):
    """แปลง Binary เป็น Decimal"""
    try:
        return int(binary, 2)
    except ValueError:
        return "Invalid binary number."


def binary_to_roman(binary):
    """แปลง Binary เป็น Roman Numeral"""
    decimal = binary_to_decimal(binary)
    if isinstance(decimal, int):
        return int_to_roman(decimal)
    return decimal


# โหมด Binary
while True:
    print("\nRoman Numeral Converter (Binary Mode)")
    print("1. Convert binary to Roman numeral")
    print("2. Exit")
    
    choice = input("Choose an option (1/2): ")
    
    if choice == "1":
        binary = input("Enter a binary number: ")
        result = binary_to_roman(binary)
        if isinstance(result, str):
            print(f"Result: {result}")
        else:
            print("Conversion failed.")
    
    elif choice == "2":
        print("Exiting the converter. Goodbye!")
        break
    
    else:
        print("Invalid option. Please choose again.")
