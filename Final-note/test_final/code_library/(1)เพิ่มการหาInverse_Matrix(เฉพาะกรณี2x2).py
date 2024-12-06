# โปรแกรมสร้างเมทริกซ์ขนาด 2x2 และคำนวณ Inverse Matrix หากมี Determinant ไม่เท่ากับ 0
import random

print("=" * 80)
rows = 2
columns = 2

matrix_a = [[random.randint(1, 5) for _ in range(columns)] for _ in range(rows)]
print(f"Matrix A [{rows}x{columns}]: {matrix_a}")

# คำนวณ Determinant
det = matrix_a[0][0] * matrix_a[1][1] - matrix_a[0][1] * matrix_a[1][0]
if det == 0:
    print("Matrix A is not invertible!")
else:
    inverse = [[matrix_a[1][1] / det, -matrix_a[0][1] / det],
               [-matrix_a[1][0] / det, matrix_a[0][0] / det]]
    print(f"Inverse of Matrix A: {inverse}")