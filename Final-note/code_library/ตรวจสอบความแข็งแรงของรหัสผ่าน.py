#โปรแกรมประเมินระดับความแข็งแรงของรหัสผ่านที่ป้อน
def password_strength(password):
    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_+=" for char in password)

    if all([length, has_upper, has_lower, has_digit, has_special]):
        return "แข็งแรงมาก"
    elif length and (has_upper or has_lower) and (has_digit or has_special):
        return "ปานกลาง"
    else:
        return "อ่อนแอ"

# รับข้อมูลจากผู้ใช้
password = input("กรุณาใส่รหัสผ่าน: ")
strength = password_strength(password)
print(f"ระดับความแข็งแรงของรหัสผ่าน: {strength}")