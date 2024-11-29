print('*' * 70)
print('Matrix File Operations'.center(70))
print('*' * 70)

file_name = "matrix_data.txt"

# สร้างเมทริกซ์และบันทึกลงไฟล์
with open(file_name, "w") as file:
    for i in range(1, 4):
        row = [i * j for j in range(1, 4)]
        file.write(" ".join(map(str, row)) + "\n")

print(f"Matrix written to {file_name}")

# อ่านเมทริกซ์จากไฟล์
matrix = []
with open(file_name, "r") as file:
    for line in file:
        matrix.append(list(map(int, line.split())))

# คำนวณ Transpose
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transpose:
    print(row)
