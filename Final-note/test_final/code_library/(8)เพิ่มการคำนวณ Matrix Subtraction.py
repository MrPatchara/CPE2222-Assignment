# โปรแกรมสำหรับการลบ Matrix ที่มีขนาดไม่เกิน 3x3
import random

print("=" * 80)
rows = int(input("Enter a number of rows: "))
columns = int(input("Enter a number of columns: "))

if rows > 3 or columns > 3:
    print("!!! Error: Maximum supported size is 3x3 !!!\n")
else:
    matrix_a = [[random.randint(0, 9) for _ in range(columns)] for _ in range(rows)]
    matrix_b = [[random.randint(0, 9) for _ in range(columns)] for _ in range(rows)]

    print(f"Matrix A: {matrix_a}")
    print(f"Matrix B: {matrix_b}")

    matrix_diff = [[matrix_a[i][j] - matrix_b[i][j] for j in range(columns)] for i in range(rows)]
    print(f"Matrix A - Matrix B: {matrix_diff}")
    print("=" * 80 + "\n")