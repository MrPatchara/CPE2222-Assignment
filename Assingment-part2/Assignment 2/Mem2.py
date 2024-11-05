import tkinter as tk # นำเข้าโมดูล tkinter โดยใช้ชื่อย่อ tk
from tkinter import ttk, messagebox # นำเข้าโมดูล ttk และ messagebox จาก tkinter
import math # นำเข้าโมดูล math

# ฟังก์ชันคำนวณพื้นที่ของสามเหลี่ยม, สี่เหลี่ยม และพีทาโกรัส
def calculate():
    if formula_var.get() == "triangle": # ถ้าเลือกสูตรสามเหลี่ยม
        try: # ใช้ try เพื่อจับข้อผิดพลาด
            base = float(base_entry.get()) # รับค่าจาก base_entry และแปลงเป็น float
            height = float(height_entry.get()) # รับค่าจาก height_entry และแปลงเป็น float
            area = 0.5 * base * height
            result_text = f"The area of triangle with base of {base:g} and height of {height:g} is {area:.1f}"
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for Base and Height.")
    elif formula_var.get() == "rectangle": # ถ้าเลือกสูตรสี่เหลี่ยม
        try:
            length = float(length_entry.get())
            width = float(width_entry.get())
            area = length * width 
            result_text = f"The area of rectangle with length of {length:g} and width of {width:g} is {area:.1f}"
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for Length and Width.")
    elif formula_var.get() == "pythagorean": # ถ้าเลือกสูตรพีทาโกรัส
        try:
            a = float(a_entry.get())
            b = float(b_entry.get())
            hypotenuse = math.sqrt(a**2 + b**2)
            result_text = f"The longest size of right triangle with ({a:g},{b:g}) is {hypotenuse:.1f}"
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for Side a and Side b.")
    result_label.config(text=result_text) # แสดงผลลัพธ์

# ฟังก์ชันแสดง/ซ่อนพารามิเตอร์
def show_parameters():
    for widget in param_frame.winfo_children(): # วนลูปเพื่อซ่อนพารามิเตอร์ทั้งหมด โดยใช้ winfo_children() เพื่อเรียกวิดเจ็ตทั้งหมดใน param_frame 
        widget.grid_remove() # ซ่อนพารามิเตอร์ทั้งหมดโดยใช้ grid_remove()

    # แสดงพารามิเตอร์ตามสูตรที่เลือก
    if formula_var.get() == "triangle": # ถ้าเลือกสูตรสามเหลี่ยม
        base_label.grid(row=0, column=0)  # แสดง base_label ที่อยู่ในตำแหน่ง (0,0)
        base_entry.grid(row=0, column=1) # แสดง base_entry ที่อยู่ในตำแหน่ง (0,1)
        height_label.grid(row=1, column=0) # แสดง height_label ที่อยู่ในตำแหน่ง (1,0)
        height_entry.grid(row=1, column=1) # แสดง height_entry ที่อยู่ในตำแหน่ง (1,1)
        triangle_button.grid(row=2, column=0, columnspan=2) # แสดง triangle_button ที่อยู่ในตำแหน่ง (2,0) และครอบคลุม 2 คอลัมน์
    elif formula_var.get() == "rectangle": # ถ้าเลือกสูตรสี่เหลี่ยม
        length_label.grid(row=0, column=0) # แสดง length_label ที่อยู่ในตำแหน่ง (0,0)
        length_entry.grid(row=0, column=1) # แสดง length_entry ที่อยู่ในตำแหน่ง (0,1)
        width_label.grid(row=1, column=0) # แสดง width_label ที่อยู่ในตำแหน่ง (1,0)
        width_entry.grid(row=1, column=1) # แสดง width_entry ที่อยู่ในตำแหน่ง (1,1)
        rectangle_button.grid(row=2, column=0, columnspan=2) # แสดง rectangle_button ที่อยู่ในตำแหน่ง (2,0) และครอบคลุม 2 คอลัมน์
    elif formula_var.get() == "pythagorean": # ถ้าเลือกสูตรพีทาโกรัส
        a_label.grid(row=0, column=0) # แสดง a_label ที่อยู่ในตำแหน่ง (0,0)
        a_entry.grid(row=0, column=1) # แสดง a_entry ที่อยู่ในตำแหน่ง (0,1)
        b_label.grid(row=1, column=0) # แสดง b_label ที่อยู่ในตำแหน่ง (1,0)
        b_entry.grid(row=1, column=1) # แสดง b_entry ที่อยู่ในตำแหน่ง (1,1)
        pythagorean_button.grid(row=2, column=0, columnspan=2) # แสดง pythagorean_button ที่อยู่ในตำแหน่ง (2,0) และครอบคลุม 2 คอลัมน์

# ตั้งค่า GUI หลัก
root = tk.Tk() # สร้างหน้าต่าง GUI โดยใช้คำสั่ง Tk() และเก็บไว้ในตัวแปร root
root.title("CPE2222") # ตั้งชื่อหน้าต่าง GUI เป็น "CPE2222"

# ตั้งค่าเฟรม 
main_frame = ttk.Frame(root, padding="10") # สร้างเฟรมโดยใช้ ttk.Frame() และเก็บไว้ในตัวแปร main_frame
main_frame.grid(row=0, column=0, sticky="NSEW") # แสดง main_frame ที่อยู่ในตำแหน่ง (0,0) และให้ยืดตามขนาดของหน้าต่าง GUI ทั้งแนวนอนและแนวตั้ง

# การเลือกสูตรการคำนวณ 
formula_var = tk.StringVar(value="triangle") # สร้างตัวแปร formula_var โดยใช้คำสั่ง StringVar() และกำหนดค่าเริ่มต้นเป็น "triangle" 
calculation_frame = ttk.LabelFrame(main_frame, text="Calculation", padding="10") # สร้างเฟรม calculation_frame โดยใช้ ttk.LabelFrame() และเก็บไว้ในตัวแปร calculation_frame
calculation_frame.grid(row=0, column=0, padx=5, pady=5, sticky="N") # แสดง calculation_frame ที่อยู่ในตำแหน่ง (0,0) และให้ติดด้านบน

ttk.Radiobutton(calculation_frame, text="Area of Rectangle", variable=formula_var, value="rectangle", command=show_parameters).grid(sticky="W") # สร้างปุ่มเลือกสูตรการคำนวณ rectangle โดยใช้ ttk.Radiobutton() และเก็บไว้ในตัวแปร formula_var

ttk.Radiobutton(calculation_frame, text="Area of Triangle", variable=formula_var, value="triangle", command=show_parameters).grid(sticky="W") # สร้างปุ่มเลือกสูตรการคำนวณ triangle โดยใช้ ttk.Radiobutton() และเก็บไว้ในตัวแปร formula_var

ttk.Radiobutton(calculation_frame, text="Pythagorean", variable=formula_var, value="pythagorean", command=show_parameters).grid(sticky="W") # สร้างปุ่มเลือกสูตรการคำนวณ pythagorean โดยใช้ ttk.Radiobutton() และเก็บไว้ในตัวแปร formula_var

# ตั้งค่าพารามิเตอร์
param_frame = ttk.LabelFrame(main_frame, text="Parameter Setting", padding="10") # สร้างเฟรม param_frame โดยใช้ ttk.LabelFrame() และเก็บไว้ในตัวแปร param_frame 
param_frame.grid(row=0, column=1, padx=5, pady=5, sticky="N") # แสดง param_frame ที่อยู่ในตำแหน่ง (0,1) และให้ติดด้านบน 

# พารามิเตอร์สำหรับสามเหลี่ยม
base_label = ttk.Label(param_frame, text="Base:") 
base_entry = ttk.Entry(param_frame) 
height_label = ttk.Label(param_frame, text="Height:")
height_entry = ttk.Entry(param_frame)
triangle_button = ttk.Button(param_frame, text="Area", command=calculate) # สร้างปุ่ม triangle_button โดยใช้ ttk.Button() และเก็บไว้ในตัวแปร triangle_button

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
result_label = ttk.Label(main_frame, text="The result will be shown here") # สร้าง result_label โดยใช้ ttk.Label() และเก็บไว้ในตัวแปร result_label
result_label.grid(row=1, column=0, columnspan=2, pady=10) # แสดง result_label ที่อยู่ในตำแหน่ง (1,0) และครอบคลุม 2 คอลัมน์ และให้มีระยะห่างด้านบน 10

# เริ่มต้นแสดงพารามิเตอร์
show_parameters()

root.mainloop() # แสดง GUI โดยใช้คำสั่ง mainloop() บรรทัดนี้จะต้องอยู่บรรทัดสุดท้ายเสมอ
