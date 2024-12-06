# โปรแกรมตรวจสอบความปลอดภัยของรหัสผ่าน
import re

while True:
    password = input("Set your password:")

    if 8 <= len(password) <= 16:
        if re.search(r'\d{4,}', password):  # Check for sequential digits
            print("!!!ERROR!!! The password must not contain more than 3 consecutive digits\n")
        elif (re.search(r'[A-Z]', password) and
              re.search(r'[a-z]', password) and
              re.search(r'[0-9]', password) and
              re.search(r'[!@#$%^&*]', password)):
            print(":-) Your password is valid and secure (-: ")
            break
        else:
            print("!!!ERROR!!! Your password does not meet the complexity requirements\n")
    elif len(password) < 8:
        print("!!!ERROR!!! The password must contain at least 8 characters\n")
    elif len(password) > 16:
        print("!!!ERROR!!! The password must not contain more than 16 characters\n")
