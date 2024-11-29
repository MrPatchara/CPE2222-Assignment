print('*' * 70)
print('Matrix Multiplication from User Input'.center(70))
print('*' * 70)

# ฟังก์ชันรับ Matrix Input จากผู้ใช้
def input_matrix(rows, cols, name):
    print(f"Enter values for {name} ({rows}x{cols}):")
    return [[int(input(f"Enter value for {name}[{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)]

# รับขนาดเมทริกซ์จากผู้ใช้
rows, cols = map(int, input("Enter dimensions of the matrix (rows cols): ").split())

# รับค่าเมทริกซ์
matrix_1 = input_matrix(rows, cols, "Matrix 1")
matrix_2 = input_matrix(cols, rows, "Matrix 2")  # ต้องการเพื่อให้สามารถคูณได้

# คำนวณผลคูณ
result = [[sum(matrix_1[i][k] * matrix_2[k][j] for k in range(cols)) for j in range(rows)] for i in range(rows)]

# แสดงผล
print("\nMatrix 1:")
for row in matrix_1:
    print(row)

print("\nMatrix 2:")
for row in matrix_2:
    print(row)

print("\nResult of Multiplication:")
for row in result:
    print(row)
