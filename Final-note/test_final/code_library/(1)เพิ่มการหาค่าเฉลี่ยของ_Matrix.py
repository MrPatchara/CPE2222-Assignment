# โปรแกรมสร้างเมทริกซ์และคำนวณค่าเฉลี่ยของทุกค่าภายในเมทริกซ์
import random

rows, columns = 3, 3

matrix_a = [[random.randint(1, 10) for _ in range(columns)] for _ in range(rows)]
print(f"Matrix A: {matrix_a}")

# คำนวณค่าเฉลี่ย
average = sum(sum(row) for row in matrix_a) / (rows * columns)
print(f"Average value of Matrix A: {average}")