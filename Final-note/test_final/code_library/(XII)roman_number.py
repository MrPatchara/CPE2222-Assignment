# โปรแกรมแปลงเลขเป็นเลขโรมันและเลขโรมันเป็นเลข
def int_to_roman(number): # ฟังก์ชันแปลงเลขเป็นเลขโรมัน
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

    result = "" # สร้างตัวแปรสำหรับเก็บเลขโรมัน
    for roman, value in roman_numerals: # วนลูปเพื่อแปลงเลขเป็นเลขโรมัน
        while number >= value: # วนลูปเพื่อเพิ่มเลขโรมัน
            result += roman # เพิ่มเลขโรมัน
            number -= value # ลบค่าเลขที่เพิ่มไปแล้ว

    return result


def roman_to_int(roman): # ฟังก์ชันแปลงเลขโรมันเป็นเลข
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


# Interactive conversion loop
while True:
    print("\nRoman Numeral Converter")
    print("1. Convert number to Roman numeral")
    print("2. Convert Roman numeral to number")
    print("3. Exit")
    
    choice = input("Choose an option (1/2/3): ")
    
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
        print("Exiting the converter. Goodbye!")
        break
    
    else:
        print("Invalid option. Please choose again.")
