#โปรแกรมค้นหาค่าที่ไม่ซ้ำในชุดข้อมูลที่ป้อน
def find_unique_values(data):
    return list(set(data))

# รับข้อมูลจากผู้ใช้
data = list(map(int, input("ใส่ข้อมูลตัวเลข (คั่นด้วยช่องว่าง): ").split()))
unique_values = find_unique_values(data)
print(f"ค่าที่ไม่ซ้ำในชุดข้อมูล: {unique_values}")