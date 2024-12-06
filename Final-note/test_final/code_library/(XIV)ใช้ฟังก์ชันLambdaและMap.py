# สร้าง Pascal Triangle โดยใช้ Lambda และ Map
def pascal_triangle_lambda(n): # ฟังก์ชันสร้าง Pascal Triangle
    triangle = [[1]]  # เริ่มต้นด้วยแถวแรก

    for _ in range(n): # วนลูปเพื่อสร้างแถว
        # ใช้ map เพื่อคำนวณค่าของแถวใหม่
        next_row = list(map(lambda x, y: x + y, [0] + triangle[-1], triangle[-1] + [0])) # คำนวณค่าของแถวใหม่
        triangle.append(next_row) # เพิ่มแถวใหม่เข้าไปในรายการ

    return triangle

# รับค่าระดับ
n = int(input("Enter the number of rows for Pascal Triangle: "))
result = pascal_triangle_lambda(n)

# แสดงผล Pascal Triangle
for row in result:
    print(row)
