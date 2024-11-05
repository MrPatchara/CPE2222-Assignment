import tkinter as tk
from tkinter import ttk, messagebox
import math

# ฟังก์ชันการคำนวณ
def calculate():
    if formula_var.get() == "triangle":
        try:
            base = float(base_entry.get())
            height = float(height_entry.get())
            area = 0.5 * base * height
            result_text = f"The area of triangle with base of {base:g} and height of {height:g} is {area:.1f}" 
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for Base and Height.")
    elif formula_var.get() == "rectangle":
        try:
            length = float(length_entry.get())
            width = float(width_entry.get())
            area = length * width
            result_text = f"The area of rectangle with length of {length:g} and width of {width:g} is {area:.1f}"
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for Length and Width.")
    elif formula_var.get() == "pythagorean":
        try:
            a = float(a_entry.get())
            b = float(b_entry.get())
            hypotenuse = math.sqrt(a**2 + b**2)
            result_text = f"The longest size of right triangle with ({a:g},{b:g}) is {hypotenuse:.1f}"
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for Side a and Side b.")
    result_label.config(text=result_text)

# ฟังก์ชันแสดง/ซ่อนพารามิเตอร์
def show_parameters():
    for widget in param_frame.winfo_children():
        widget.grid_remove()

    if formula_var.get() == "triangle":
        base_label.grid(row=0, column=0)
        base_entry.grid(row=0, column=1)
        height_label.grid(row=1, column=0)
        height_entry.grid(row=1, column=1)
        triangle_button.grid(row=2, column=0, columnspan=2)
    elif formula_var.get() == "rectangle":
        length_label.grid(row=0, column=0)
        length_entry.grid(row=0, column=1)
        width_label.grid(row=1, column=0)
        width_entry.grid(row=1, column=1)
        rectangle_button.grid(row=2, column=0, columnspan=2)
    elif formula_var.get() == "pythagorean":
        a_label.grid(row=0, column=0)
        a_entry.grid(row=0, column=1)
        b_label.grid(row=1, column=0)
        b_entry.grid(row=1, column=1)
        pythagorean_button.grid(row=2, column=0, columnspan=2)

# ตั้งค่า GUI หลัก
root = tk.Tk()
root.title("CPE2222")

# ตั้งค่าเฟรม
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky="NSEW")

# การเลือกสูตรการคำนวณ
formula_var = tk.StringVar(value="triangle")
calculation_frame = ttk.LabelFrame(main_frame, text="Calculation", padding="10")
calculation_frame.grid(row=0, column=0, padx=5, pady=5, sticky="N")

ttk.Radiobutton(calculation_frame, text="Area of Rectangle", variable=formula_var, value="rectangle", command=show_parameters).grid(sticky="W")
ttk.Radiobutton(calculation_frame, text="Area of Triangle", variable=formula_var, value="triangle", command=show_parameters).grid(sticky="W")
ttk.Radiobutton(calculation_frame, text="Pythagorean", variable=formula_var, value="pythagorean", command=show_parameters).grid(sticky="W")

# ตั้งค่าพารามิเตอร์
param_frame = ttk.LabelFrame(main_frame, text="Parameter Setting", padding="10")
param_frame.grid(row=0, column=1, padx=5, pady=5, sticky="N")

# พารามิเตอร์สำหรับสามเหลี่ยม
base_label = ttk.Label(param_frame, text="Base:")
base_entry = ttk.Entry(param_frame)
height_label = ttk.Label(param_frame, text="Height:")
height_entry = ttk.Entry(param_frame)
triangle_button = ttk.Button(param_frame, text="Area", command=calculate)

# พารามิเตอร์สำหรับสี่เหลี่ยม
length_label = ttk.Label(param_frame, text="Length:")
length_entry = ttk.Entry(param_frame)
width_label = ttk.Label(param_frame, text="Width:")
width_entry = ttk.Entry(param_frame)
rectangle_button = ttk.Button(param_frame, text="Area", command=calculate)

# พารามิเตอร์สำหรับพีทาโกรัส
a_label = ttk.Label(param_frame, text="Side a:")
a_entry = ttk.Entry(param_frame)
b_label = ttk.Label(param_frame, text="Side b:")
b_entry = ttk.Entry(param_frame)
pythagorean_button = ttk.Button(param_frame, text="Hypotenuse", command=calculate)

# แสดงผลลัพธ์
result_label = ttk.Label(main_frame, text="The result will be shown here")
result_label.grid(row=1, column=0, columnspan=2, pady=10)

# เริ่มต้นแสดงพารามิเตอร์สำหรับสามเหลี่ยม
show_parameters()

root.mainloop()
