# โปรแกรมสร้างเมทริกซ์สี่เหลี่ยมจัตุรัสแบบสุ่ม และคำนวณ Determinant 
# โดยใช้ฟังก์ชันแบบ Recursive
import random

def determinant(matrix): # สร้างฟังก์ชันคำนวณ Determinant
    #   คำนวณ Determinant ของ Matrix แบบ Recursive
    if len(matrix) == 1: # กรณี Matrix 1x1
        return matrix[0][0] # ค่าเดียวกัน
    if len(matrix) == 2: # กรณี Matrix 2x2
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] # คำนวณ Determinant ของ Matrix 2x2

    det = 0 # กำหนดค่าเริ่มต้นของ Determinant เป็น 0
    for c in range(len(matrix)): # กรณี Matrix 3x3 ขึ้นไป
        minor = [row[:c] + row[c+1:] for row in matrix[1:]] # สร้าง Minor Matrix
        det += ((-1) ** c) * matrix[0][c] * determinant(minor) # คำนวณ Determinant ของ Matrix 3x3 ขึ้นไป
    return det # คืนค่า Determinant

print("=" * 80) # แสดงข้อความต้อนรับ
rows = int(input("Enter a number of rows: ")) # รับค่าจำนวนแถวของ Matrix

# ใช้เฉพาะ Matrix สี่เหลี่ยมจัตุรัส
matrix_a = [[random.randint(1, 5) for _ in range(rows)] for _ in range(rows)] # สร้าง Matrix สี่เหลี่ยมจัตุรัส แบบสุ่ม
print(f"Matrix A [{rows}x{rows}]: {matrix_a}") # แสดง Matrix A

# คำนวณ Determinant
det = determinant(matrix_a) # คำนวณ Determinant ของ Matrix A
print(f"Determinant: {det}") # แสดงค่า Determinant