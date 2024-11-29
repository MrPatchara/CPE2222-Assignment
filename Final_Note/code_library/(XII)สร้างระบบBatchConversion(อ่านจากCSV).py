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

import csv

def batch_convert_to_roman(input_file, output_file):
    """แปลงตัวเลขในไฟล์ CSV เป็น Roman Numerals"""
    try:
        with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            writer.writerow(["Number", "Roman Numeral"])
            
            for row in reader:
                try:
                    number = int(row[0])
                    roman = int_to_roman(number)
                    writer.writerow([number, roman])
                except ValueError:
                    writer.writerow([row[0], "Invalid"])
        return f"Results written to {output_file}"
    except FileNotFoundError:
        return "Input file not found."

# Example การเรียกใช้ฟังก์ชัน
input_csv = "numbers.csv"  # ไฟล์ต้องมีแค่ตัวเลขในแต่ละแถว
output_csv = "roman_results.csv"
print(batch_convert_to_roman(input_csv, output_csv))
