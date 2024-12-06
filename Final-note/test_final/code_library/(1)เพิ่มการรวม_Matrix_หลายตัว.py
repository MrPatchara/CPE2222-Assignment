# โปรแกรมสร้างเมทริกซ์ 2 ตัว และคำนวณผลรวมของเมทริกซ์ A และ B

import random

print("=" * 80)
rows, columns = 3, 3 # กำหนดขนาดของเมทริกซ์

# สร้าง Matrix A และ B
matrix_a = [[random.randint(0, 5) for _ in range(columns)] for _ in range(rows)]
matrix_b = [[random.randint(0, 5) for _ in range(columns)] for _ in range(rows)]
print(f"Matrix A: {matrix_a}")
print(f"Matrix B: {matrix_b}")

# รวม Matrix
combined = [[matrix_a[i][j] + matrix_b[i][j] for j in range(columns)] for i in range(rows)] # คำนวณผลรวมของเมทริกซ์ A และ B
print(f"Combined Matrix A+B: {combined}")