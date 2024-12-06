# โปรแกรมตรวจสอบความแข็งแรงของรหัสผ่าน
import re

while True:
    password = input("Set your password:")

    # Check password length
    if 8 <= len(password) <= 16:
        # Check if password meets all criteria
        if (re.search(r'[A-Z]', password) and  # At least one uppercase letter
            re.search(r'[a-z]', password) and  # At least one lowercase letter
            re.search(r'[0-9]', password) and  # At least one digit
            re.search(r'[!@#$%^&*]', password)):  # At least one special character
            print(":-) Your password is strong (-: ")
            break
        
        # Check missing criteria
        missing_criteria = []
        if not re.search(r'[A-Z]', password):
            missing_criteria.append("an uppercase letter")
        if not re.search(r'[a-z]', password):
            missing_criteria.append("a lowercase letter")
        if not re.search(r'[0-9]', password):
            missing_criteria.append("a digit")
        if not re.search(r'[!@#$%^&*]', password):
            missing_criteria.append("a special character")

        print(f"!!!ERROR!!! Your password is missing {', '.join(missing_criteria)}\n")

    elif len(password) < 8:
        print("!!!ERROR!!! The password must contain at least 8 characters\n")
    elif len(password) > 16:
        print("!!!ERROR!!! The password must not contain more than 16 characters\n")
