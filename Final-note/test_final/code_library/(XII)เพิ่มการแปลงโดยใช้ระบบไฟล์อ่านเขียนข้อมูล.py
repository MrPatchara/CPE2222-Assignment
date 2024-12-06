# โปรแกรมแปลงตัวเลขเป็น Roman Numeral และกลับกัน
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

def write_roman_to_file(number, filename="roman_output.txt"):
    """แปลงตัวเลขเป็น Roman Numeral และบันทึกในไฟล์"""
    roman = int_to_roman(number)
    with open(filename, "w") as file:
        file.write(f"Number: {number}\nRoman Numeral: {roman}")
    return f"Result written to {filename}"


def read_roman_from_file(filename="roman_input.txt"):
    """อ่านไฟล์ที่มี Roman Numeral และแปลงกลับเป็นตัวเลข"""
    try:
        with open(filename, "r") as file:
            roman = file.read().strip()
            result = roman_to_int(roman)
            return f"Roman: {roman}\nNumber: {result}"
    except FileNotFoundError:
        return f"File {filename} not found."
    except Exception as e:
        return f"An error occurred: {e}"


# โหมดไฟล์
while True:
    print("\nRoman Numeral Converter (File Mode)")
    print("1. Convert number to Roman numeral and save to file")
    print("2. Read Roman numeral from file and convert to number")
    print("3. Exit")
    
    choice = input("Choose an option (1/2/3): ")
    
    if choice == "1":
        try:
            number = int(input("Enter a number (1 - 1,000,000): "))
            print(write_roman_to_file(number))
        except ValueError:
            print("Please enter a valid number.")
    
    elif choice == "2":
        filename = input("Enter the filename to read Roman numeral from: ")
        print(read_roman_from_file(filename))
    
    elif choice == "3":
        print("Exiting the converter. Goodbye!")
        break
    
    else:
        print("Invalid option. Please choose again.")
