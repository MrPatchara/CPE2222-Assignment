#โปรแกรมคำนวณค่าสหสัมพันธ์ระหว่างข้อมูล 2 ชุด
import numpy as np

def calculate_correlation(x, y):
    # คำนวณค่าสหสัมพันธ์
    if len(x) != len(y):
        raise ValueError("ข้อมูลทั้งสองชุดต้องมีความยาวเท่ากัน")
    return np.corrcoef(x, y)[0, 1]

# รับข้อมูลจากผู้ใช้
x = list(map(float, input("ใส่ข้อมูลชุดที่ 1 (คั่นด้วยช่องว่าง): ").split()))
y = list(map(float, input("ใส่ข้อมูลชุดที่ 2 (คั่นด้วยช่องว่าง): ").split()))

try:
    correlation = calculate_correlation(x, y)
    print(f"ค่าสหสัมพันธ์ระหว่างข้อมูลสองชุดคือ: {correlation:.2f}")
except ValueError as e:
    print(e)