# โปรแกรมตรวจสอบความปลอดภัยของรหัสผ่าน
# โดยรหัสผ่านจะต้องมีความยาวระหว่าง 8 ถึง 16 ตัวอักษร
# และต้องประกอบด้วยอักษรตัวใหญ่ อักษรตัวเล็ก ตัวเลข และอักขระพิเศษ
# โดยใช้ Regular Expression ในการตรวจสอบ
# ถ้ารหัสผ่านไม่ผ่านเงื่อนไขใด ๆ จะ
# แสดงข้อความแจ้งเตือนและให้ผู้ใช้ป้อนรหัสผ่านใหม่
# ถ้ารหัสผ่านผ่านเงื่อนไขทั้งหมด จะแสดงข้อความยินดีและจบการทำงาน
# โปรแกรมจะวนลูปไปเรื่อย ๆ จนกว่ารห
# สผ่านที่ผู้ใช้ป้อนจะผ่านเงื่อนไขทั้งหมด
# หรือจนกว่าผู้ใช้จะป้อนรหัสผ่านที่ตรงตามเงื่อนไข
# หรือกด Ctrl+C เพื่อหยุดการทำงานของโปรแกรม
import re

while True:
    password = input("Set your password:")
    confirm_password = input("Confirm your password:")

    if password != confirm_password:  # Check if passwords match
        print("!!!ERROR!!! The passwords do not match\n") # Print error message
    elif 8 <= len(password) <= 16: # Check if password length is between 8 and 16 characters
        if (re.search(r'[A-Z]', password) and # Check if password meets complexity requirements
              re.search(r'[a-z]', password) and # using regular expressions (regex) to match patterns 
              re.search(r'[0-9]', password) and # for uppercase letters, lowercase letters, numbers, and special characters
              re.search(r'[!@#$%^&*]', password)):
            print(":-) Your password is valid and secure (-: ")
            break
        else:
            print("!!!ERROR!!! Your password does not meet the complexity requirements\n")
    elif len(password) < 8:
        print("!!!ERROR!!! The password must contain at least 8 characters\n")
    elif len(password) > 16:
        print("!!!ERROR!!! The password must not contain more than 16 characters\n")
