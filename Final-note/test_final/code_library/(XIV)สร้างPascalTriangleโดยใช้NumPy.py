# โปรแกรมสร้าง Pascal Triangle ด้วย NumPy
import numpy as np

# ใช้ NumPy ในการสร้าง Pascal Triangle
def pascal_triangle_numpy(n): # ฟังก์ชันสร้าง Pascal Triangle
    triangle = np.zeros((n + 1, n + 1), dtype=int)  # สร้าง array ที่มีค่าเริ่มต้นเป็น 0
    for i in range(n + 1): # วนลูปเพื่อสร้างแถว
        triangle[i][0] = 1  # เริ่มแถวแต่ละแถวด้วย 1
        for j in range(1, i + 1): # วนลูปเพื่อสร้างตัวเลขใหม่
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]  # คำนวณค่ากลาง
    return triangle # ส่งค่ากลับ

# รับค่าระดับ
n = int(input("Enter the number of rows for Pascal Triangle (NumPy): ")) # รับค่าจากผู้ใช้
result = pascal_triangle_numpy(n) # เรียกใช้ฟังก์ชัน

# แสดงผล
for row in result: # วนลูปเพื่อแสดงผล
    print(row[row > 0])  # แสดงเฉพาะค่าในแถวที่ไม่เป็น 0
