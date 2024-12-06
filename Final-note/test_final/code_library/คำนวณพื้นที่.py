# โปรแกรมสำหรับคำนวณพื้นที่สี่เหลี่ยม, สามเหลี่ยม, และทฤษฎีพีทาโกรัส
import tkinter as tk  # นำเข้า tkinter สำหรับสร้าง GUI
from tkinter import ttk  # นำเข้า ttk สำหรับ widget สไตล์พิเศษ (ใช้ในบางกรณี)
from math import sqrt  # นำเข้า sqrt สำหรับคำนวณรากที่สอง

class CPE2222App:
    # ฟังก์ชันช่วยในการแสดงผลโดยตรวจสอบทศนิยมหรือจำนวนเต็ม
    def format_number(self, value):
        # หากค่าเป็นจำนวนเต็มให้แสดงเป็นจำนวนเต็ม หากไม่ใช่ให้แสดงเป็นทศนิยม
        return int(value) if value.is_integer() else value

    def __init__(self, root):
        self.root = root  # เก็บอ้างอิงของหน้าต่างหลัก
        self.root.title("CPE2222")  # ตั้งชื่อหน้าต่างโปรแกรม
        
        # ตัวเลือกการคำนวณ (จะมี 3 ตัวเลือก: สี่เหลี่ยม, สามเหลี่ยม, พีทาโกรัส)
        self.choice = tk.StringVar(value="Pythagorean")  # ค่าเริ่มต้นเป็น Pythagorean
        
        # หัวข้อฝั่งซ้าย สำหรับเลือกประเภทการคำนวณ
        frame_area = tk.LabelFrame(root, text="Calculation")  # LabelFrame สำหรับหมวดหมู่การคำนวณ
        frame_area.grid(row=0, column=0, padx=10, pady=10)  # วาง frame ที่แถว 0 คอลัมน์ 0

        # Radio Buttons สำหรับเลือกประเภทการคำนวณ
        tk.Radiobutton(frame_area, text="Area of Rectangle", variable=self.choice, value="Rectangle", command=self.update_labels).pack(anchor='w')
        tk.Radiobutton(frame_area, text="Area of Triangle", variable=self.choice, value="Triangle", command=self.update_labels).pack(anchor='w')
        tk.Radiobutton(frame_area, text="Pythagorean", variable=self.choice, value="Pythagorean", command=self.update_labels).pack(anchor='w')

        # ส่วนของ Parameter Setting สำหรับกรอกขนาดที่ต้องการคำนวณ
        frame_param = tk.LabelFrame(root, text="Parameter Setting")  # LabelFrame สำหรับตั้งค่าพารามิเตอร์
        frame_param.grid(row=0, column=1, rowspan=2, padx=10, pady=10)  # วาง frame ที่แถว 0 คอลัมน์ 1

        # Labels สำหรับขนาด
        self.label1 = tk.Label(frame_param, text="The 1st size:")  # Label สำหรับขนาดที่ 1
        self.label1.grid(row=0, column=0, padx=5, sticky='e')  # วาง label ที่แถว 0 คอลัมน์ 0
        self.label2 = tk.Label(frame_param, text="The 2nd size:")  # Label สำหรับขนาดที่ 2
        self.label2.grid(row=1, column=0, padx=5, sticky='e')  # วาง label ที่แถว 1 คอลัมน์ 0
        
        # Spinbox สำหรับขนาด (ตัวเลือกให้กรอกขนาดที่ต้องการ)
        self.size1_entry = tk.Spinbox(frame_param, from_=0, to=200, width=10)  # Spinbox สำหรับขนาด 1
        self.size1_entry.grid(row=0, column=1, padx=5)
        self.size1_entry.delete(0, "end")  # ลบค่าภายใน Spinbox
        self.size1_entry.insert(0, "1")  # ใส่ค่าเริ่มต้นเป็น 1

        self.size2_entry = tk.Spinbox(frame_param, from_=0, to=200, width=10)  # Spinbox สำหรับขนาด 2
        self.size2_entry.grid(row=1, column=1, padx=5)
        self.size2_entry.delete(0, "end")  # ลบค่าภายใน Spinbox
        self.size2_entry.insert(0, "1")  # ใส่ค่าเริ่มต้นเป็น 1

        # ปุ่มคำนวณเมื่อคลิก
        self.calc_button = tk.Button(frame_param, text="Area", command=self.calculate)  # ปุ่ม "Area" หรือ "Pythagorean Theory"
        self.calc_button.grid(row=2, column=0, columnspan=2, pady=5)  # วางปุ่มในแถวที่ 2

        # Label สำหรับแสดงผลลัพธ์
        self.result_label = tk.Label(root, text="")  # Label สำหรับแสดงผลลัพธ์การคำนวณ
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)  # วางผลลัพธ์ที่แถว 2 คอลัมน์ 0-1

        # เรียก update_labels เพื่ออัพเดตข้อความเริ่มต้น
        self.update_labels()

    def update_labels(self):
        # อัพเดตข้อความ label ตามตัวเลือกการคำนวณที่เลือก
        if self.choice.get() == "Rectangle":
            self.label1.config(text="Length:")  # เปลี่ยนข้อความของ label1 เป็น "Length"
            self.label2.config(text="Width:")  # เปลี่ยนข้อความของ label2 เป็น "Width"
            self.calc_button.config(text="Area")  # เปลี่ยนข้อความปุ่มเป็น "Area" สำหรับการคำนวณพื้นที่สี่เหลี่ยม
        elif self.choice.get() == "Triangle":
            self.label1.config(text="Base:")  # เปลี่ยนข้อความของ label1 เป็น "Base"
            self.label2.config(text="Height:")  # เปลี่ยนข้อความของ label2 เป็น "Height"
            self.calc_button.config(text="Area")  # เปลี่ยนข้อความปุ่มเป็น "Area" สำหรับการคำนวณพื้นที่สามเหลี่ยม
        elif self.choice.get() == "Pythagorean":
            self.label1.config(text="The 1st size:")  # เปลี่ยนข้อความของ label1
            self.label2.config(text="The 2nd size:")  # เปลี่ยนข้อความของ label2
            self.calc_button.config(text="Pythagorean Theory")  # เปลี่ยนข้อความปุ่มเป็น "Pythagorean Theory"

    def calculate(self):
        # รับค่าขนาดจาก Spinbox
        try:
            size1 = float(self.size1_entry.get())  # รับค่าจาก Spinbox และแปลงเป็น float
            size2 = float(self.size2_entry.get())  # รับค่าจาก Spinbox และแปลงเป็น float
        except ValueError:  # หากค่าไม่สามารถแปลงเป็น float ได้
            self.result_label.config(text="ERROR!!!!!!!!!!!!!!.")  # แสดงข้อความข้อผิดพลาด
            return

        # คำนวณตามตัวเลือกที่เลือก
        if self.choice.get() == "Rectangle":
            result = size1 * size2  # คำนวณพื้นที่สี่เหลี่ยมผืนผ้า
            self.result_label.config(text=f"The area of rectangle with length {self.format_number(size1)} and width {self.format_number(size2)} is {self.format_number(result):.1f}")
        elif self.choice.get() == "Triangle":
            result = 0.5 * size1 * size2  # คำนวณพื้นที่สามเหลี่ยม
            self.result_label.config(text=f"The area of triangle with base {self.format_number(size1)} and height {self.format_number(size2)} is {self.format_number(result):.1f}")
        elif self.choice.get() == "Pythagorean":
            result = sqrt(size1**2 + size2**2)  # คำนวณใช้ทฤษฎีพีทาโกรัส
            self.result_label.config(text=f"The longest side of right triangle with ({self.format_number(size1)},{self.format_number(size2)}) is {self.format_number(result):.1f}")

# ส่วนของการเริ่มต้นโปรแกรม
if __name__ == "__main__":  # เมื่อโปรแกรมทำงานเป็นหลัก
    root = tk.Tk()  # สร้างหน้าต่างหลัก
    app = CPE2222App(root)  # สร้างแอปพลิเคชัน CPE2222App
    root.mainloop()  # เริ่มการทำงานของ loop GUI
