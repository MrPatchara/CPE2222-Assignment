# โปรแกรมนี้สร้างเมทริกซ์ 2 ตัว และคำนวณผลต่างของเมทริกซ์ A และ B

import random # เรียกใช้งานโมดูล random

rows, columns = 3, 3 # กำหนดขนาดของเมทริกซ์

matrix_a = [[random.randint(0, 9) for _ in range(columns)] for _ in range(rows)] # สร้างเมทริกซ์ A
matrix_b = [[random.randint(0, 9) for _ in range(columns)] for _ in range(rows)] # สร้างเมทริกซ์ B
print(f"Matrix A: {matrix_a}") # แสดงเมทริกซ์ A
print(f"Matrix B: {matrix_b}") # แสดงเมทริกซ์ B

# คำนวณผลต่าง
difference = [[matrix_a[i][j] - matrix_b[i][j] for j in range(columns)] for i in range(rows)] # คำนวณผลต่างของเมทริกซ์ A และ B
print(f"Matrix A-B: {difference}") # แสดงผลต่างของเมทริกซ์ A และ B