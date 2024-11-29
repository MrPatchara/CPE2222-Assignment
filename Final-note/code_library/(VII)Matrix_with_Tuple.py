print('*' * 70)
print('Matrix with Tuple'.center(70))
print('*' * 70)

A = ((1, 3, 5), (2, 4, 6))
A_T = tuple(zip(*A))
A_AT = (
    (sum(A[0][k] * A_T[k][0] for k in range(3)), sum(A[0][k] * A_T[k][1] for k in range(3))),
    (sum(A[1][k] * A_T[k][0] for k in range(3)), sum(A[1][k] * A_T[k][1] for k in range(3)))
)

def input_number(matrix, matrix_name, matrix_position):
        row = int(input(f"Enter row number of the {matrix_name}: ")) - 1
        col = int(input(f"Enter column number of the {matrix_name}: ")) - 1
        value = matrix[row][col]
        print(f'The "{matrix_position}{row+1}{col+1}" element in the {matrix_name} matrix is {value}')

input_number(A, '"A" matrix', 'a')
print("-" * 67)

input_number(A_T, 'transposed "A" matrix', 'b')
print("-" * 67)

input_number(A_AT, 'multiplication of matrix "A" and transposed of "A"', 'c')
print("-" * 67 + "\n")
