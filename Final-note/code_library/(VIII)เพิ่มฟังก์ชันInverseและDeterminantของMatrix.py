import numpy as np  # ใช้ numpy เพื่อช่วยในงานคำนวณที่ซับซ้อน

print('*' * 70)
print('Matrix Operations with NumPy'.center(70))
print('*' * 70)

# นิยามเมทริกซ์ A (สามารถเปลี่ยนค่าได้ตามต้องการ)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]])

# ฟังก์ชันคำนวณ Determinant
def determinant(matrix):
    det = np.linalg.det(matrix)
    return round(det, 2)  # ปัดค่าทศนิยมเหลือ 2 ตำแหน่ง

# ฟังก์ชันคำนวณ Inverse
def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        return "Matrix is singular (no inverse)"  # กรณีที่ determinant เป็น 0
    return np.linalg.inv(matrix)

# แสดงผล
print("Matrix A:")
print(A)
print("\nDeterminant of A:", determinant(A))
print("\nInverse of A:")
print(inverse(A))
