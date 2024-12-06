#โปรแกรมนับจำนวนครั้งที่แต่ละค่าปรากฏในชุดข้อมูล
from collections import Counter

def count_frequency(data):
    return Counter(data)

# รับข้อมูลจากผู้ใช้
data = list(map(int, input("ใส่ข้อมูลตัวเลข (คั่นด้วยช่องว่าง): ").split()))
frequency = count_frequency(data)
print("ความถี่ของค่าข้อมูล:")
for value, count in frequency.items():
    print(f"{value}: {count} ครั้ง")