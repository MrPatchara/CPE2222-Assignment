#โปรแกรมกรองข้อมูลที่มีค่ามากกว่าค่าที่กำหนด
def filter_data(data, threshold):
    return [value for value in data if value > threshold]

# รับข้อมูลจากผู้ใช้
data = list(map(float, input("ใส่ข้อมูลตัวเลข (คั่นด้วยช่องว่าง): ").split()))
threshold = float(input("กรุณาใส่ค่าที่ต้องการกรอง: "))

filtered_data = filter_data(data, threshold)
print(f"ข้อมูลที่ผ่านการกรอง: {filtered_data}")