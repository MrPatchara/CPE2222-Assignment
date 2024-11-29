import re

while True:
    password = input("Set your password:")

    def has_sequential_chars(password):
        """Check if the password contains sequential characters like 'abc' or '123'."""
        for i in range(len(password) - 2):
            if password[i:i+3].isdigit() or password[i:i+3].isalpha():
                if ord(password[i]) + 1 == ord(password[i+1]) and ord(password[i+1]) + 1 == ord(password[i+2]):
                    return True
        return False

    if 8 <= len(password) <= 16:
        if has_sequential_chars(password):
            print("!!!ERROR!!! The password must not contain 3 or more sequential characters like 'abc' or '123'\n")
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
