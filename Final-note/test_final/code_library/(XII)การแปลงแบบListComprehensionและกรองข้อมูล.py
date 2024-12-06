# โปรแกรมแปลงตัวเลขเป็น Roman Numerals และแปลง List ของตัวเลขเป็น Roman Numerals
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

def convert_list_to_roman(numbers):
    """แปลง List ของตัวเลขเป็น Roman Numerals"""
    return [
        (number, int_to_roman(number)) if 0 < number <= 1000000 else (number, "Out of range")
        for number in numbers
    ]

# ตัวอย่างการใช้งาน
numbers = [1, 4, 10, 1000, 500000, -1, 1000001]
results = convert_list_to_roman(numbers)
for number, roman in results:
    print(f"Number: {number}, Roman Numeral: {roman}")
