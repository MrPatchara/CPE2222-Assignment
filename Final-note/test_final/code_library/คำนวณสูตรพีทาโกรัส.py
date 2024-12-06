#โปรแกรมคำนวณความยาวด้านของสามเหลี่ยมมุมฉากโดยใช้สูตรพีทาโกรัส
import math

def calculate_pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

# รับข้อมูลจากผู้ใช้
a = float(input("กรุณาใส่ความยาวด้านสั้นด้านแรก: "))
b = float(input("กรุณาใส่ความยาวด้านสั้นด้านที่สอง: "))

c = calculate_pythagoras(a, b)
print(f"ความยาวด้านตรงข้ามมุมฉากคือ: {c:.2f}")