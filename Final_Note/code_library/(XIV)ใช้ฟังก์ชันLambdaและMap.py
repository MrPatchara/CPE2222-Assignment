# สร้าง Pascal Triangle โดยใช้ Lambda และ Map
def pascal_triangle_lambda(n):
    triangle = [[1]]  # เริ่มต้นด้วยแถวแรก

    for _ in range(n):
        # ใช้ map เพื่อคำนวณค่าของแถวใหม่
        next_row = list(map(lambda x, y: x + y, [0] + triangle[-1], triangle[-1] + [0]))
        triangle.append(next_row)

    return triangle

# รับค่าระดับ
n = int(input("Enter the number of rows for Pascal Triangle: "))
result = pascal_triangle_lambda(n)

# แสดงผล Pascal Triangle
for row in result:
    print(row)
