# โปรแกรมนี้สร้าง Matrix Identity (เมทริกซ์เอกลักษณ์) ตามขนาดที่ผู้ใช้ระบุ
# โดย Matrix Identity คือ Matrix ที่มีเลข 1 อยู่บนแนวทแยง และเลข 0 อยู่ที่ตำแหน่งอื่น ๆ
import random

def determinant(matrix):
    """คำนวณ Determinant ของ Matrix แบบ Recursive"""
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(minor)
    return det

print("=" * 80)
rows = int(input("Enter a number of rows: "))

# ใช้เฉพาะ Matrix สี่เหลี่ยมจัตุรัส
matrix_a = [[random.randint(1, 5) for _ in range(rows)] for _ in range(rows)]
print(f"Matrix A [{rows}x{rows}]: {matrix_a}")

# คำนวณ Determinant
det = determinant(matrix_a)
print(f"Determinant: {det}")

# สร้าง Matrix Identity
identity_matrix = [[1 if i == j else 0 for j in range(rows)] for i in range(rows)]
print(f"Identity Matrix [{rows}x{rows}]: {identity_matrix}")