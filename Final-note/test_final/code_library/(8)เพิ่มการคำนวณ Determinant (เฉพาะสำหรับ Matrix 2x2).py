# โปรแกรมคำนวณ Determinant ของ Matrix ขนาด 2x2
import random

print("=" * 80)
rows = int(input("Enter a number of rows: "))
columns = int(input("Enter a number of columns: "))

if rows != 2 or columns != 2:
    print("!!! Error: Determinant calculation only supports 2x2 matrices !!!\n")
else:
    print("=" * 80)
    # สุ่มค่าจำนวนเต็ม 0-9 สำหรับ Matrix A
    matrix_a = [[random.randint(0, 9) for _ in range(columns)] for _ in range(rows)]
    print(f"Matrix A [{rows}x{columns}]: {matrix_a}")

    # คำนวณ Determinant
    determinant = matrix_a[0][0] * matrix_a[1][1] - matrix_a[0][1] * matrix_a[1][0]
    print(f"Determinant of Matrix A: {determinant}")
    print("=" * 80 + "\n")