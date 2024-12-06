# โปรแกรมคำนวณ Inverse Matrix ขนาด 2x2
import random

print("=" * 80)
rows = int(input("Enter a number of rows: "))
columns = int(input("Enter a number of columns: "))

if rows != 2 or columns != 2:
    print("!!! Error: Inverse calculation only supports 2x2 matrices !!!\n")
else:
    print("=" * 80)
    # สุ่มค่าจำนวนเต็ม 1-9 สำหรับ Matrix A (หลีกเลี่ยง determinant = 0)
    matrix_a = [[random.randint(1, 9) for _ in range(columns)] for _ in range(rows)]
    print(f"Matrix A [{rows}x{columns}]: {matrix_a}")

    # คำนวณ Determinant
    determinant = matrix_a[0][0] * matrix_a[1][1] - matrix_a[0][1] * matrix_a[1][0]
    if determinant == 0:
        print("!!! Error: Matrix is not invertible (Determinant = 0) !!!")
    else:
        # คำนวณ Inverse Matrix
        inverse_matrix = [
            [matrix_a[1][1] / determinant, -matrix_a[0][1] / determinant],
            [-matrix_a[1][0] / determinant, matrix_a[0][0] / determinant],
        ]
        print(f"Inverse of Matrix A: {inverse_matrix}")
    print("=" * 80 + "\n")