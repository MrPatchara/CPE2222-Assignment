# ฟังก์ชันสร้าง Pascal Triangle แบบ Iterative
def pascal_triangle_iterative(n):
    triangle = []  # เริ่มต้นเป็นลิสต์ว่าง
    for i in range(n + 1):  # สำหรับแต่ละแถว
        row = [1]  # เริ่มด้วย 1
        if i > 0:  # ถ้าไม่ใช่แถวแรก
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])  # คำนวณค่าใหม่จากแถวก่อนหน้า
            row.append(1)  # เพิ่ม 1 ที่ท้ายแถว
        triangle.append(row)  # เพิ่มแถวนี้ใน Triangle
    return triangle

# รับค่าระดับจากผู้ใช้
n = int(input("Enter the number of rows for Pascal Triangle: "))
result = pascal_triangle_iterative(n)

# แสดงผล
for row in result:
    print(row)
