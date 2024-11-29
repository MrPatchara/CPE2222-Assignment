import numpy as np

# ใช้ NumPy ในการสร้าง Pascal Triangle
def pascal_triangle_numpy(n):
    triangle = np.zeros((n + 1, n + 1), dtype=int)  # สร้าง array ที่มีค่าเริ่มต้นเป็น 0
    for i in range(n + 1):
        triangle[i][0] = 1  # เริ่มแถวแต่ละแถวด้วย 1
        for j in range(1, i + 1):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]  # คำนวณค่ากลาง
    return triangle

# รับค่าระดับ
n = int(input("Enter the number of rows for Pascal Triangle (NumPy): "))
result = pascal_triangle_numpy(n)

# แสดงผล
for row in result:
    print(row[row > 0])  # แสดงเฉพาะค่าในแถวที่ไม่เป็น 0
