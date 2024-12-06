# โปรแกรมที่สุ่มสร้าง Matrix ขนาด n x n และตรวจสอบว่า Matrix นั้นเป็น Diagonal Matrix หรือไม่
import random

print("=" * 80)
rows = int(input("Enter a number of rows: "))
columns = int(input("Enter a number of columns: "))

if rows != columns:
    print("!!! Error: Only square matrices can be diagonal !!!\n")
else:
    matrix = [[random.randint(0, 9) if i == j else random.choice([0, 0]) for j in range(columns)] for i in range(rows)]
    print(f"Generated Matrix: {matrix}")

    is_diagonal = all(matrix[i][j] == 0 for i in range(rows) for j in range(columns) if i != j)
    print("Matrix is diagonal." if is_diagonal else "Matrix is not diagonal.")
    print("=" * 80 + "\n")