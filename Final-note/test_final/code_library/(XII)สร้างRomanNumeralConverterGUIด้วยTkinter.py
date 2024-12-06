# โปรแกรมแปลงตัวเลขเป็น Roman Numeral และแปลง Roman Numeral เป็นตัวเลข ด้วย Tkinter
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

import tkinter as tk
from tkinter import messagebox

def convert_to_roman():
    """แปลงตัวเลขเป็น Roman Numeral"""
    try:
        number = int(entry_number.get())
        if number <= 0 or number > 1000000:
            messagebox.showerror("Error", "Number out of range (1 - 1,000,000)")
        else:
            roman = int_to_roman(number)
            result_label.config(text=f"Roman Numeral: {roman}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def convert_to_number():
    """แปลง Roman Numeral เป็นตัวเลข"""
    roman = entry_roman.get().upper()
    result = roman_to_int(roman)
    if isinstance(result, int):
        result_label.config(text=f"Number: {result}")
    else:
        messagebox.showerror("Error", result)

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("Roman Numeral Converter")

# ส่วนของการแปลง
frame = tk.Frame(root)
frame.pack(pady=20)

# Input สำหรับแปลงตัวเลขเป็น Roman
tk.Label(frame, text="Number (1 - 1,000,000):").grid(row=0, column=0, pady=5, padx=5)
entry_number = tk.Entry(frame)
entry_number.grid(row=0, column=1, pady=5, padx=5)
tk.Button(frame, text="Convert to Roman", command=convert_to_roman).grid(row=0, column=2, pady=5, padx=5)

# Input สำหรับแปลง Roman เป็นตัวเลข
tk.Label(frame, text="Roman Numeral:").grid(row=1, column=0, pady=5, padx=5)
entry_roman = tk.Entry(frame)
entry_roman.grid(row=1, column=1, pady=5, padx=5)
tk.Button(frame, text="Convert to Number", command=convert_to_number).grid(row=1, column=2, pady=5, padx=5)

# แสดงผลลัพธ์
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# เริ่ม GUI
root.mainloop()
