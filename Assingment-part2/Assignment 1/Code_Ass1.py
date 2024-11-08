import tkinter as tk
from tkinter import messagebox
import random

class BullsAndCowsGame:
    def __init__(self, root):
        self.root = root 
        self.root.title("Bull and Cow guessing game")
        
        # สุ่มเลข 4 หลักที่ไม่ซ้ำกัน
        self.target_number = self.generate_number()

        # สร้างส่วนประกอบของ GUI
        self.setup_gui()
        # ปรับขนาดหน้าต่างโปรแกรม 350x100 พิกเซล
        self.root.geometry("350x100")

    def generate_number(self):
        # สุ่มเลข 4 หลักที่ไม่ซ้ำกันและคืนค่าเป็นสตริง
        return ''.join(random.sample("0123456789", 4))

    def setup_gui(self):
        # สร้างเฟรมหลักสำหรับวางส่วนประกอบ
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # ส่วนของช่องให้ผู้ใช้ใส่ตัวเลข
        tk.Label(frame, text="Guessing:").grid(row=0, column=0)
        
        # สร้างช่องใส่ตัวเลข 4 หลัก
        self.guess_entries = [tk.Entry(frame, width=2, font=("Helvetica", 14), justify="center") for _ in range(4)]
        for i, entry in enumerate(self.guess_entries): # วางช่องใส่ตัวเลขในเฟรม
            entry.grid(row=0, column=i+1) 

        # ปุ่ม Submit 
        submit_button = tk.Button(frame, text="Submit", command=self.check_guess)
        submit_button.grid(row=0, column=5, padx=10) 

        # ปุ่ม Show Answer 
        answer_button = tk.Button(frame, text="Show Answer", command=self.show_answer)
        answer_button.grid(row=1, column=0, columnspan=6, pady=5)

        # ส่วนของคำใบ้ (Hint) เพื่อแสดงจำนวน Bulls และ Cows
        tk.Label(frame, text="Hint:" ).grid(row=0, column=6)
        self.hint_label = tk.Label(frame, text="")
        self.hint_label.grid(row=1, column=6)

    def check_guess(self):
        # ดึงค่าการทายจากช่องใส่ข้อมูลและรวมเป็นสตริง
        guess = ''.join(entry.get() for entry in self.guess_entries)
        
        # ตรวจสอบความถูกต้องของการทาย
        if not self.is_valid_guess(guess):
            messagebox.showerror("Error", "Please enter 4 unique digits.")
            return

        # คำนวณ Bulls และ Cows
        bulls, cows = self.calculate_bulls_and_cows(guess)

        # ถ้าทายถูกต้องทั้งหมด (4 Bulls)
        if bulls == 4:
            self.hint_label.config(text="*** CORRECT ***")
        else:
            self.hint_label.config(text=f"Bulls:{bulls} and Cows:{cows}")
            # ล้างข้อมูลในช่องกรอกตัวเลข
            for entry in self.guess_entries:
                entry.delete(0, tk.END)

    def is_valid_guess(self, guess):
        # ตรวจสอบว่าเป็นตัวเลข 4 หลักที่ไม่ซ้ำกัน
        return len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4

    def calculate_bulls_and_cows(self, guess):
        # คำนวณจำนวน Bulls และ Cows จากการทาย
        bulls = sum(1 for i in range(4) if guess[i] == self.target_number[i])
        cows = sum(1 for i in range(4) if guess[i] in self.target_number and guess[i] != self.target_number[i])
        return bulls, cows

    def show_answer(self):
        messagebox.showinfo("Answer", f"The correct number is: {self.target_number}")

if __name__ == "__main__":
    root = tk.Tk()
    game = BullsAndCowsGame(root)
    root.mainloop()
