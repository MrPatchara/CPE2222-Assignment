# Assignment VII: การใช้ Tuple ในการจัดการเมทริกซ์
def create_matrix(rows, cols, elements): 
    matrix = []
    for i in range(rows): # วนลูปเพื่อสร้างแถวของเมทริกซ์
        row = elements[i*cols:(i+1)*cols] # แบ่งข้อมูลใน elements ออกเป็นแถว
        matrix.append(tuple(row)) # เพิ่มแถวลงในเมทริกซ์
    return tuple(matrix) 
# ฟังก์ชันนี้สร้างเมทริกซ์จากค่าของจำนวนแถว (rows), จำนวนคอลัมน์ (cols), และข้อมูลทั้งหมดในเมทริกซ์ (elements)

def transpose_matrix(matrix): 
    transposed = []
    for j in range(cols): # วนลูปเพื่อสร้างคอลัมน์ของเมทริกซ์
        column = [row[j] for row in matrix] # ดึงค่าของคอลัมน์ในแต่ละแถว
        transposed.append(tuple(column)) # เพิ่มคอลัมน์ลงในทรานสโพสเมทริกซ์
    return tuple(transposed)
# ฟังก์ชันนี้สร้างทรานสโพสของเมทริกซ์ โดยวนซ้ำตามคอลัมน์ของเมทริกซ์เดิม (matrix) และดึงค่าของคอลัมน์ในแต่ละแถวมาสร้างเป็นแถวในทรานสโพสเมทริกซ์

def multiply_matrices(matrix1, matrix2): # ฟังก์ชันคูณเมทริกซ์
    rows1, cols1 = len(matrix1), len(matrix1[0]) # จำนวนแถวและคอลัมน์ของ matrix1
    rows2, cols2 = len(matrix2), len(matrix2[0]) # จำนวนแถวและคอลัมน์ของ matrix2
    result = [[0] * cols2 for _ in range(rows1)] # สร้างเมทริกซ์ผลลัพธ์ที่เริ่มต้นด้วยค่า 0 ทั้งหมด
    for i in range(rows1): # วนลูปเพื่อคำนวณค่าในแต่ละตำแหน่งของเมทริกซ์ผลลัพธ์
        for j in range(cols2): # วนลูปเพื่อคำนวณค่าในแต่ละคอลัมน์ของเมทริกซ์ผลลัพธ์
            for k in range(cols1): # วนลูปเพื่อคำนวณค่าในแต่ละคอลัมน์ของ matrix1 และแถวของ matrix2
                result[i][j] += matrix1[i][k] * matrix2[k][j] 
    return tuple(map(tuple, result))
# ฟังก์ชันนี้คูณเมทริกซ์ 2 เมทริกซ์ (matrix1 และ matrix2)
# สร้างเมทริกซ์ผลลัพธ์ (result) ที่เริ่มต้นด้วยค่า 0 ทั้งหมด และมีขนาดตามแถวของ matrix1 และคอลัมน์ของ matrix2
# ใช้การวนซ้ำ 3 ชั้น (i, j, และ k) เพื่อคำนวณค่าที่แต่ละตำแหน่งของเมทริกซ์ผลลัพธ์


# กำหนดค่าเมทริกซ์ A
elements = (1, 3, 5, 2, 4, 6)
rows, cols = 2, 3

# คำนวณเมทริกซ์ A , A^T และ AA^T
matrix_A = create_matrix(rows, cols, elements) # สร้างเมทริกซ์ A
matrix_AT = transpose_matrix(matrix_A) # สร้างเมทริกซ์ A^T
matrix_AAT = multiply_matrices(matrix_A, matrix_AT) # คูณเมทริกซ์ A และ A^T


# รับค่าดัชนีและแสดงผล
print("*"*95)

# แสดงผลลัพธ์เมทริกซ์ A
# print("Matrix A:") center คำว่า Matrix A ให้อยู่ตรงกลางของ 
print("Matrix with Tuple:".center(95))
print("*"*95)
print('Enter row number of the "A" matrix:', end='')
row = int(input())
print('Enter column number of the "A" matrix:', end='')
col = int(input())
print(f'The "a{row}{col}" element in the "A" matrix is {matrix_A[row-1][col-1]}')
print("-"*95)

# แสดงผลลัพธ์เมทริกซ์ A^T
print('Enter row number of the transposed "A" matrix:', end='')
row = int(input())
print('Enter column number of the transposed "A" matrix:', end='')
col = int(input())
print(f'The "b{row}{col}" element in the transposed "A" matrix is {matrix_AT[row-1][col-1]}')
print("-"*95)

# แสดงผลลัพธ์เมทริกซ์ AA^T
print('Enter row number of the multiplication of matrices "A" and transpose of "A":', end='')
row = int(input())
print('Enter column number of the multiplication of matrices "A" and transpose of "A":', end='')
col = int(input())
print(f'The "c{row}{col}" element in the multiplication of the "A" matrix and the transposed "A" matrix is {matrix_AAT[row-1][col-1]}')
print("-"*95)