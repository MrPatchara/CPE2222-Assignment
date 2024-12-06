# โปรแกรมตรวจสอบความซับซ้อนของรหัสผ่าน
import re

while True:
    password = input("Set your password:")

    if 8 <= len(password) <= 16:
        if (re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'[0-9]', password) and
            not re.search(r'(.)\1{2,}', password)):  # Check for repeated characters
            print(":-) Your password is valid (-: ")
            break

        elif re.search(r'(.)\1{2,}', password):  # Error for repeated characters
            print("!!!ERROR!!! The password must not contain three consecutive identical characters\n")
        else:
            print("!!!ERROR!!! Your password does not meet the complexity requirements\n")
    elif len(password) < 8:
        print("!!!ERROR!!! The password must contain at least 8 characters\n")
    elif len(password) > 16:
        print("!!!ERROR!!! The password must not contain more than 16 characters\n")
