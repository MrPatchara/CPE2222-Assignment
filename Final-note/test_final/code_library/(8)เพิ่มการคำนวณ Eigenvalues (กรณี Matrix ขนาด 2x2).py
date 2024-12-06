# โปรแกรมคำนวณ Eigenvalues ของ Matrix ขนาด 2x2
import random
import math

print("=" * 80)
rows = int(input("Enter a number of rows: "))
columns = int(input("Enter a number of columns: "))

if rows != 2 or columns != 2:
    print("!!! Error: Eigenvalue calculation only supports 2x2 matrices !!!\n")
else:
    matrix = [[random.randint(0, 9) for _ in range(columns)] for _ in range(rows)]
    print(f"Matrix: {matrix}")

    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]

    trace = a + d
    determinant = a * d - b * c

    eigenvalue1 = (trace + math.sqrt(trace**2 - 4 * determinant)) / 2
    eigenvalue2 = (trace - math.sqrt(trace**2 - 4 * determinant)) / 2

    print(f"Eigenvalues: {eigenvalue1:.2f}, {eigenvalue2:.2f}")
    print("=" * 80 + "\n")