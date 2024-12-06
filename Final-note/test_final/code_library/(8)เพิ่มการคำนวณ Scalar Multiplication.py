# โปรแกรมคูณเมทริกซ์ด้วยสคาลาร์
import random

print("=" * 80)
rows = int(input("Enter a number of rows: "))
columns = int(input("Enter a number of columns: "))

if rows > 3 or columns > 3:
    print("!!! Error: Maximum supported size is 3x3 !!!\n")
else:
    scalar = int(input("Enter a scalar value: "))
    matrix_a = [[random.randint(0, 9) for _ in range(columns)] for _ in range(rows)]
    print(f"Matrix A: {matrix_a}")

    scaled_matrix = [[scalar * matrix_a[i][j] for j in range(columns)] for i in range(rows)]
    print(f"Scalar Multiplication Result: {scaled_matrix}")
    print("=" * 80 + "\n")