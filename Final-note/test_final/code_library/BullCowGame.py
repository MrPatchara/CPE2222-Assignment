# โปรแกรมเกมทายเลข Bull and Cow โดยใช้ tkinter
import tkinter as tk  # นำเข้า tkinter สำหรับสร้าง GUI
from tkinter import messagebox  # นำเข้า messagebox สำหรับแสดงข้อความเตือน
import random  # นำเข้า random สำหรับสุ่มเลขลับ

class BullCowGame:
    def __init__(self, root):  # ตัวสร้างของคลาส BullCowGame รับ root เป็นตัวแปร
        self.root = root  # เก็บอ้างอิงของหน้าต่างหลัก
        self.root.title("Bull and Cow guessing game")  # กำหนดชื่อหน้าต่างหลัก

        # สร้างเลขลับ 4 หลักแบบสุ่ม
        self.secret_number = [str(random.randint(0, 9)) for _ in range(4)]  # สุ่มเลข 4 หลักจาก 0 ถึง 9
        print("Secret number:", self.secret_number)  # พิมพ์เลขลับเพื่อใช้ในการ debug (สามารถลบออกหลังจากเสร็จสิ้น)

        # Label และ Entry สำหรับการทายเลข
        self.label_guess = tk.Label(root, text="Guessing:")  # สร้าง label สำหรับข้อความ "Guessing:"
        self.label_guess.grid(row=0, column=0, padx=10, pady=10)  # วาง label ในตำแหน่งแถวที่ 0 คอลัมน์ที่ 0

        # สร้าง Entry 4 ช่องสำหรับกรอกตัวเลข
        self.entries = [tk.Entry(root, width=3, font=("Arial", 16)) for _ in range(4)]  # สร้าง entry จำนวน 4 ช่องสำหรับกรอกเลข
        for i, entry in enumerate(self.entries):  # วาง entry ในแต่ละช่อง
            entry.grid(row=0, column=i+1)  # วางในแถวที่ 0 คอลัมน์ที่ i+1

        # ปุ่ม Submit
        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess)  # สร้างปุ่ม "Submit"
        self.submit_button.grid(row=0, column=5, padx=10)  # วางปุ่มในตำแหน่งแถวที่ 0 คอลัมน์ที่ 5

        # Label สำหรับแสดงผล Bull และ Cow
        self.hint_label = tk.Label(root, text="Hint:")  # สร้าง label สำหรับแสดงผลลัพธ์ Bull และ Cow
        self.hint_label.grid(row=1, column=0, columnspan=6, pady=10)  # วาง label ในแถวที่ 1 ครอบคลุมคอลัมน์ที่ 0-5

    def check_guess(self):  # ฟังก์ชันสำหรับตรวจสอบการทาย
        guess = [entry.get() for entry in self.entries]  # รับค่าจาก Entry ทั้ง 4 ช่องเป็นรายการ

        # ตรวจสอบว่ากรอกครบ 4 หลัก และเป็นตัวเลข
        if len(guess) != 4 or not all(g.isdigit() for g in guess):  # ตรวจสอบว่าเป็นตัวเลขและกรอกครบ 4 ตัว
            messagebox.showwarning("Invalid input", "Please enter a 4-digit number.")  # หากไม่ครบหรือไม่ใช่ตัวเลขให้แสดงข้อความเตือน
            return

        # คำนวณ Bulls และ Cows
        bulls = sum(1 for i in range(4) if guess[i] == self.secret_number[i])  # คำนวณ Bulls (ตรงทั้งตัวเลขและตำแหน่ง)
        cows = sum(1 for g in guess if g in self.secret_number) - bulls  # คำนวณ Cows (ตัวเลขตรงแต่ตำแหน่งไม่ตรง)

        # แสดงผล
        if bulls == 4:  # ถ้าผู้เล่นทายถูกหมด
            self.hint_label.config(text="*** CORRECT ***")  # แสดงข้อความว่า "ถูกต้อง"
        else:  # หากทายผิด
            self.hint_label.config(text=f"Bulls: {bulls} and Cows: {cows}")  # แสดงผล Bulls และ Cows

# ส่วนของการเริ่มต้นโปรแกรม
if __name__ == "__main__":  # เมื่อโปรแกรมทำงานเป็นหลัก
    root = tk.Tk()  # สร้างหน้าต่างหลัก
    game = BullCowGame(root)  # สร้างเกมโดยส่ง root ไปให้คลาส BullCowGame
    root.mainloop()  # เริ่มการทำงานของ loop GUI
