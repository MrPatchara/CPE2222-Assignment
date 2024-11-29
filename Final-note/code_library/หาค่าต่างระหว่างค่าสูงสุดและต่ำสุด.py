#โปรแกรมคำนวณส่วนต่างระหว่างค่ามากที่สุดและน้อยที่สุดในชุดข้อมูล
def max_min_difference(data):
    return max(data) - min(data)

# รับข้อมูลจากผู้ใช้
data = list(map(float, input("ใส่ข้อมูลตัวเลข (คั่นด้วยช่องว่าง): ").split()))

difference = max_min_difference(data)
print(f"ค่าต่างระหว่างค่าสูงสุดและต่ำสุดคือ: {difference:.2f}")