# โปรแกรมตรวจสอบความปลอดภัยของรหัสผ่าน
import re

while True:
    password = input("Set your password:")

    if 8 <= len(password) <= 16:
        # Check first and last character requirements
        if not (re.match(r'[A-Za-z0-9!@#$%^&*]', password[0]) and 
                re.match(r'[A-Za-z0-9!@#$%^&*]', password[-1])):
            print("!!!ERROR!!! The password must start and end with a valid character (no spaces or special symbols other than allowed)\n")
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
