#โปรแกรมคำนวณหาค่าหรม. (GCD) และพ.ร.น. (LCM) ของตัวเลขสองตัว
# การหาค่า GCD และ LCM
import math

def calculate_gcd_lcm(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a * b) // gcd
    return gcd, lcm

# รับข้อมูลจากผู้ใช้
a = int(input("ใส่ตัวเลขตัวแรก: "))
b = int(input("ใส่ตัวเลขตัวที่สอง: "))

gcd, lcm = calculate_gcd_lcm(a, b)
print(f"ค่า GCD ของ {a} และ {b} คือ {gcd}")
print(f"ค่า LCM ของ {a} และ {b} คือ {lcm}")