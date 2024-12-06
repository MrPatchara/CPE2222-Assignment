# โปรแกรมตรวจสอบรหัสผ่านที่ผู้ใช้ป้อนเข้ามาว่ามีความปลอดภัยหรือไม่
import re

password = input()

if 3 <= len(password) <= 20:
  if (re.search(r'[A-Z]', password) and
     re.search(r'[a-z]', password) and
     re.search(r'[0-9]', password) and
     re.search(r'[!@#$%^&*_+.,\/;]', password)):
     print("Valid")
  else:
     print("Invalid")
       
else:
  print("Invalid")