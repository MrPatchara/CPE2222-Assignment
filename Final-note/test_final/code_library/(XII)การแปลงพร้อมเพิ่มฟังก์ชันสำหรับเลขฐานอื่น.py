# โปรแกรมแปลงเลขฐาน 2 และ 16 เป็น Roman Numeral
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

def base_to_roman(number, base=10):
    """แปลงเลขจากระบบฐานต่าง ๆ เป็น Roman Numeral"""
    try:
        if base != 10:
            number = int(str(number), base)
        return int_to_roman(number) if 0 < number <= 1000000 else "Out of range"
    except ValueError:
        return "Invalid number for base conversion"

# ตัวอย่างการใช้งาน
numbers_base2 = ["110", "1001", "1010"]  # Binary
for binary in numbers_base2:
    print(f"Binary: {binary}, Roman: {base_to_roman(binary, base=2)}")

numbers_base16 = ["A", "1F", "3E8"]  # Hexadecimal
for hex_num in numbers_base16:
    print(f"Hex: {hex_num}, Roman: {base_to_roman(hex_num, base=16)}")
