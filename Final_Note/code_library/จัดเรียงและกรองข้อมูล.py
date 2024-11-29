#โปรแกรมจัดเรียงข้อมูลและกรองค่าที่มากกว่าค่ากำหนด
def sort_and_filter(data, threshold):
    sorted_data = sorted(data)
    filtered_data = [x for x in sorted_data if x > threshold]
    return filtered_data

# รับข้อมูลจากผู้ใช้
data = list(map(int, input("ใส่ข้อมูลตัวเลข (คั่นด้วยช่องว่าง): ").split()))
threshold = int(input("กรุณาใส่ค่าที่ต้องการกรอง: "))

result = sort_and_filter(data, threshold)
print(f"ข้อมูลที่จัดเรียงและกรองแล้ว: {result}")