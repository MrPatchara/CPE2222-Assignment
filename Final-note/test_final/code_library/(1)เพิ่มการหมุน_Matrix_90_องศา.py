# โปรแกรมสร้างเมทริกซ์และหมุนเมทริกซ์ 90 องศา

import random

print("=" * 80)
rows = int(input("Enter a number of rows: "))
columns = int(input("Enter a number of columns: "))

matrix_a = [[random.randint(0, 9) for _ in range(columns)] for _ in range(rows)]
print(f"Original Matrix: {matrix_a}")

# หมุน 90 องศา
rotated = [[matrix_a[rows-1-j][i] for j in range(rows)] for i in range(columns)]
print(f"Matrix rotated 90 degrees: {rotated}")