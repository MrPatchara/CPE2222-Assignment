# Assignment 10 (X) - Code Assignment X
import re # Regular Expression

def check_password(password):
    # ตรวจสอบความยาวของรหัสผ่านไม่น้อยกว่า 8 
    if len(password) < 8:
        return "!!!ERROR!!! The password must contain at lest 8 characters"
    
    # ตรวจสอบความยาวของรหัสผ่านไม่เกิน 16
    if len(password) > 16:
        return "!!!ERROR!!! The password must not contain more 16 characters"

    # ตรวจสอบว่ามีอักษรตัวพิมพ์ใหญ่
    if not re.search(r"[A-Z]", password): # ตรวจสอบว่ามีอักษรตัวพิมพ์ใหญ่ด้วยการใช้ Regular Expression
        return "!!!ERROR!!! The password must contain at least a capital letter"

    # ตรวจสอบว่ามีอักษรตัวพิมพ์เล็ก
    if not re.search(r"[a-z]", password):
        return "!!!ERROR!!! The password must contain at least a lowercase letter"

    # ตรวจสอบว่ามีตัวเลข
    if not re.search(r"[0-9]", password):
        return "!!!ERROR!!! The password must contain at least a number" 

    # ตรวจสอบรหัสผ่านที่ถูกต้อง
    if password == "Python2021":
        return ":-) Your password is correct (-:)"


# รับค่ารหัสผ่านจากผู้ใช้
user_password = input("Setting your password: ")
print(check_password(user_password)) 
