import tkinter as tk # นำเข้าโมดูล tkinter โดยใช้ชื่อย่อ tk
from tkinter import messagebox # นำเข้าฟังก์ชัน messagebox จากโมดูล tkinter
import random # นำเข้าโมดูล random เพื่อใช้สุ่มเลข

class BullsAndCowsGame: # สร้างคลาส BullsAndCowsGame
    def __init__(self, root): 
        self.root = root 
        self.root.title("Bull and Cow guessing game") # กำหนดชื่อหน้าต่างโปรแกรม
        
        # สุ่มเลข 4 หลักที่ไม่ซ้ำกัน โดยเรียกใช้ฟังก์ชัน generate_number
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
        frame.pack(pady=10)  # กำหนดระยะห่างขอบของเฟรม

        # ส่วนของช่องให้ผู้ใช้ใส่ตัวเลข
        tk.Label(frame, text="Guessing:").grid(row=0, column=0) # สร้างป้ายชื่อ Guessing และวางไว้ที่แถว 0 คอลัมน์ 0
        
        # สร้างช่องใส่ตัวเลข 4 หลัก
        self.guess_entries = [tk.Entry(frame, width=2, font=("Helvetica", 14), justify="center") for _ in range(4)] # สร้างช่องใส่ตัวเลข 4 ช่อง และกำหนดขนาดและรูปแบบตัวอักษร และจัดวางตรงกลาง 
        for i, entry in enumerate(self.guess_entries): # วางช่องใส่ตัวเลขในเฟรม โดยวนลูปเพื่อวางช่องใส่ตัวเลข 
            entry.grid(row=0, column=i+1) 

        # ปุ่ม Submit เพื่อยืนยันการทาย
        submit_button = tk.Button(frame, text="Submit", command=self.check_guess)
        submit_button.grid(row=0, column=5, padx=10) # สร้างปุ่ม Submit และวางไว้ที่แถว 0 คอลัมน์ 5 โดยกำหนดระยะห่างจากขอบของเฟรม 10 พิกเซล

        # ปุ่ม Show Answer เพื่อแสดงเฉลย
        answer_button = tk.Button(frame, text="Show Answer", command=self.show_answer) # สร้างปุ่ม Show Answer และกำหนดให้เรียกฟังก์ชัน show_answer เมื่อคลิก
        answer_button.grid(row=1, column=0, columnspan=6, pady=5) # วางปุ่ม Show Answer ที่แถว 1 คอลัมน์ 0 และกว้างเท่ากับ 6 คอลัมน์ โดยกำหนดระยะห่างจากขอบของเฟรม 5 พิกเซล

        # ส่วนของคำใบ้ (Hint) เพื่อแสดงจำนวน Bulls และ Cows
        tk.Label(frame, text="Hint:" ).grid(row=0, column=6) # สร้างป้ายชื่อ Hint และวางไว้ที่แถว 0 คอลัมน์ 6
        self.hint_label = tk.Label(frame, text="") # สร้างป้ายชื่อ Hint และกำหนดให้เป็นสตริงว่าง  และวางไว้ที่แถว 1 คอลัมน์ 6
        self.hint_label.grid(row=1, column=6)

    def check_guess(self): # สร้างฟังก์ชัน check_guess เพื่อตรวจสอบการทาย
        # ดึงค่าการทายจากช่องใส่ข้อมูลและรวมเป็นสตริง
        guess = ''.join(entry.get() for entry in self.guess_entries)
        
        # ตรวจสอบความถูกต้องของการทาย โดยเรียกใช้ฟังก์ชัน is_valid_guess และถ้าไม่ถูกต้องให้แสดงข้อความแจ้งเตือน
        if not self.is_valid_guess(guess):
            messagebox.showerror("Error", "Please enter 4 unique digits.") # แสดงข้อความแจ้งเตือนว่ากรุณาใส่ตัวเลข 4 หลักที่ไม่ซ้ำกัน
            return

        # คำนวณ Bulls และ Cows โดยเรียกใช้ฟังก์ชัน calculate_bulls_and_cows
        bulls, cows = self.calculate_bulls_and_cows(guess)

        # ถ้าทายถูกต้องทั้งหมด (4 Bulls) ให้แสดงข้อความว่าถูกต้อง
        if bulls == 4:
            self.hint_label.config(text="*** CORRECT ***")
        else:
            self.hint_label.config(text=f"Bulls:{bulls} and Cows:{cows}") # แสดงจำนวน Bulls และ Cows ที่ทายถูก
            # ล้างข้อมูลในช่องกรอกตัวเลข
            for entry in self.guess_entries: # วนลูปเพื่อล้างข้อมูลในช่องกรอกตัวเลข 
                entry.delete(0, tk.END) 

    def is_valid_guess(self, guess): # สร้างฟังก์ชัน is_valid_guess เพื่อตรวจสอบความถูกต้องของการทาย
        # ตรวจสอบว่าเป็นตัวเลข 4 หลักที่ไม่ซ้ำกัน
        return len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4 # คืนค่าเป็นจริงถ้าเป็นตัวเลข 4 หลักที่ไม่ซ้ำกัน มิฉะนั้นคืนค่าเป็นเท็จ 

    def calculate_bulls_and_cows(self, guess): # สร้างฟังก์ชัน calculate_bulls_and_cows เพื่อคำนวณจำนวน Bulls และ Cows 
        # คำนวณจำนวน Bulls และ Cows จากการทาย
        bulls = sum(1 for i in range(4) if guess[i] == self.target_number[i]) # นับจำนวน Bulls โดยเรียกใช้ฟังก์ชัน sum และใช้การวนลูปเพื่อนับจำนวน Bulls 
        cows = sum(1 for i in range(4) if guess[i] in self.target_number and guess[i] != self.target_number[i]) # นับจำนวน Cows โดยเรียกใช้ฟังก์ชัน sum และใช้การวนลูปเพื่อนับจำนวน Cows 
        return bulls, cows # คืนค่าจำนวน Bulls และ Cows

    def show_answer(self): # สร้างฟังก์ชัน show_answer เพื่อแสดงเฉลย
        # แสดงเฉลยให้ผู้ใช้
        messagebox.showinfo("Answer", f"The correct number is: {self.target_number}") 

# สร้างหน้าต่างหลักของโปรแกรม 
if __name__ == "__main__":
    root = tk.Tk()
    game = BullsAndCowsGame(root)
    root.mainloop()
