# โปรแกรมตั้งรหัสผ่านที่มีความปลอดภัย
import re

while True:
    password = input("Setting your password:")

    if 8 <= len(password) <= 16:
        if (re.search(r'[A-Z]', password)) and (re.search(r'[a-z]', password)) and (re.search(r'[0-9]', password)):
            print(':-) Your password is correct (-:')
            break
        
        elif (re.search(r'[a-z]', password)) and (re.search(r'[0-9]', password)):
            print('!!!ERROR!!! The password must contain at least a capital letter\n')

        elif (re.search(r'[A-Z]', password)) and (re.search(r'[0-9]', password)):
            print('!!!ERROR!!! The password must contain at least a lowercase letter\n')

        elif (re.search(r'[A-Z]', password)) and (re.search(r'[a-z]', password)):
            print('!!!ERROR!!! The password must contain at least a number\n')



    elif len(password) < 8:
        print('!!!ERROR!!! The password must contain at least 8 characters\n')
    elif len(password) > 16:
        print('!!!ERROR!!! The password must not contain more than 16 character\n')