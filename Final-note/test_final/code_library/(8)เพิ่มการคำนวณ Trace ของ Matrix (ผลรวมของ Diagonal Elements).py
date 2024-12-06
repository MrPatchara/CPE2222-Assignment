# โปรแกรมนี้เป็นโปรแกรมที่ใช้สำหรับหา Trace ของ Matrix ขนาด n x n โดยที่ n คือขนาดของ Matrix และ Trace คือผลรวมของ Elements ที่อยู่บน Diagonal ของ Matrix
import random

print("=" * 80)
size = int(input("Enter the size of the square matrix: "))

if size > 3:
    print("!!! Error: Maximum supported size is 3x3 !!!\n")
else:
    matrix = [[random.randint(0, 9) for _ in range(size)] for _ in range(size)]
    print(f"Matrix: {matrix}")

    trace = sum(matrix[i][i] for i in range(size))
    print(f"Trace of the Matrix: {trace}")
    print("=" * 80 + "\n")