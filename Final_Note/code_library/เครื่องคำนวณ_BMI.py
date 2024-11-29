def calculate_bmi(weight, height):
    """คำนวณ BMI จากน้ำหนัก (kg) และส่วนสูง (m)"""
    return weight / (height ** 2)


def interpret_bmi(bmi):
    """แปลผล BMI"""
    if bmi < 18.5:
        return "น้ำหนักต่ำกว่าเกณฑ์"
    elif 18.5 <= bmi < 24.9:
        return "น้ำหนักปกติ"
    elif 25 <= bmi < 29.9:
        return "น้ำหนักเกิน"
    else:
        return "โรคอ้วน"


# รับข้อมูลจากผู้ใช้
weight = float(input("กรุณาใส่น้ำหนักของคุณ (kg): "))
height = float(input("กรุณาใส่ส่วนสูงของคุณ (m): "))


# คำนวณ BMI
bmi = calculate_bmi(weight, height)
print(f"ค่า BMI ของคุณคือ: {bmi:.2f} ({interpret_bmi(bmi)})")