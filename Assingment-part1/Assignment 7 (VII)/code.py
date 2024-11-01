
# สร้าง Matrix A, A Transpose และ A * A^T
A = ((1, 3, 5), (2, 4, 6)) 
A_T = tuple(zip(*A)) # สร้าง A Transpose จากการใช้ zip และ *A ที่เป็นการแปลงคอลัมน์เป็นแถวและแถวเป็นคอลัมน์
A_AT = (
    (sum(A[0][k] * A_T[k][0] for k in range(3)), sum(A[0][k] * A_T[k][1] for k in range(3))),
    (sum(A[1][k] * A_T[k][0] for k in range(3)), sum(A[1][k] * A_T[k][1] for k in range(3)))
) # คูณ Matrix A และ A Transpose โดยใช้การวนซ้ำเพื่อคำนวณค่าในแต่ละตำแหน่งของ Matrix ผลลัพธ์

# ฟังก์ชันสำหรับแสดงค่าใน Matrix ตามตำแหน่งที่ต้องการ
def get_matrix_value(matrix, matrix_name, element_prefix):
        row = int(input(f"Enter row number of the {matrix_name}: ")) - 1
        col = int(input(f"Enter column number of the {matrix_name}: ")) - 1
        value = matrix[row][col]
        print(f'The "{element_prefix}{row+1}{col+1}" element in the {matrix_name} matrix is {value}')

# แสดงผลลัพธ์ตามรูปแบบที่ต้องการ
print("*" * 67)
print("Matrix with Tuple:".center(67))
print("*" * 67)
get_matrix_value(A, '"A" matrix', 'a')

print("-" * 67)
get_matrix_value(A_T, 'transposed "A" matrix', 'b')

print("-" * 67)
get_matrix_value(A_AT, 'multiplication of matrices "A" and transpose of "A"', 'c')
