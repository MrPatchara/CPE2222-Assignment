def create_matrix(rows, cols, elements): 
    matrix = []
    for i in range(rows):
        row = elements[i*cols:(i+1)*cols]
        matrix.append(tuple(row))
    return tuple(matrix)

def transpose_matrix(matrix): 
    transposed = []
    for j in range(cols):
        column = [row[j] for row in matrix]
        transposed.append(tuple(column))
    return tuple(transposed)

def multiply_matrices(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    result = [[0] * cols2 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return tuple(map(tuple, result))

# กำหนดค่าเมทริกซ์ A
elements = (1, 3, 5, 2, 4, 6)
rows, cols = 2, 3

# คำนวณเมทริกซ์ A , A^T และ AA^T
matrix_A = create_matrix(rows, cols, elements)
matrix_AT = transpose_matrix(matrix_A)
matrix_AAT = multiply_matrices(matrix_A, matrix_AT)


# รับค่าดัชนีและแสดงผล
print("*"*95)
# print("Matrix A:") center คำว่า Matrix A ให้อยู่ตรงกลางของ * 80 ตัว
print("Matrix with Tuple:".center(95))
print("*"*95)
print('Enter row number of the "A" matrix:', end='')
row = int(input())
print('Enter column number of the "A" matrix:', end='')
col = int(input())
print(f'The "a{row}{col}" element in the "A" matrix is {matrix_A[row-1][col-1]}')
print("-"*95)

print('Enter row number of the transposed "A" matrix:', end='')
row = int(input())
print('Enter column number of the transposed "A" matrix:', end='')
col = int(input())
print(f'The "b{row}{col}" element in the transposed "A" matrix is {matrix_AT[row-1][col-1]}')
print("-"*95)

print('Enter row number of the multiplication of matrices "A" and transpose of "A":', end='')
row = int(input())
print('Enter column number of the multiplication of matrices "A" and transpose of "A":', end='')
col = int(input())
print(f'The "c{row}{col}" element in the multiplication of the "A" matrix and the transposed "A" matrix is {matrix_AAT[row-1][col-1]}')
print("-"*95)