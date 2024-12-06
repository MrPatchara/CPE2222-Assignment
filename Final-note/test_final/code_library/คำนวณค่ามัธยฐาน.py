#โปรแกรมคำนวณค่ามัธยฐานจากชุดข้อมูลที่ป้อน
import statistics

def calculate_median(data):
    return statistics.median(data)

# รับข้อมูลจากผู้ใช้
data = list(map(float, input("ใส่ข้อมูลตัวเลข (คั่นด้วยช่องว่าง): ").split()))
median = calculate_median(data)
print(f"ค่ามัธยฐานคือ: {median}")