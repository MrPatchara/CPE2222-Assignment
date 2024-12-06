#โปรแกรมคำนวณค่าเบี่ยงเบนมาตรฐานจากข้อมูลที่ป้อน
import math

def calculate_standard_deviation(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

# รับข้อมูลจากผู้ใช้
data = list(map(float, input("ใส่ข้อมูลตัวเลข (คั่นด้วยช่องว่าง): ").split()))
std_dev = calculate_standard_deviation(data)
print(f"ค่าเบี่ยงเบนมาตรฐานคือ: {std_dev:.2f}")