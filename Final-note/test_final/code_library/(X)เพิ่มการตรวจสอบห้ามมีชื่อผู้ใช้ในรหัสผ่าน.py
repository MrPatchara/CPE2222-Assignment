# โปรแกรมตรวจสอบความปลอดภัยของรหัสผ่าน
import re

username = input("Enter your username:")

while True:
    password = input("Set your password:")

    if username.lower() in password.lower():  # Check if username is part of the password
        print("!!!ERROR!!! Your password must not contain your username\n")
    elif 8 <= len(password) <= 16:
        if (re.search(r'[A-Z]', password) and
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
