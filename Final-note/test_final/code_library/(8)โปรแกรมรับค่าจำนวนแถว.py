#โปรแกรมสร้าง Matrix และคำนวณผลคูณ A x A^T

import random

print("=" * 80)
rows = int(input("Enter a number of rows: "))
columns = int(input("Enter a number of columns: "))

if rows > 3 or columns > 3:
    print("!!!   Error in a number of rows or columns   !!!\n")
else:
    print("=" * 80)
    # สุ่มค่าจำนวนเต็ม 0-9 สำหรับ Matrix A
    matrix_a = [[random.randint(0, 9) for _ in range(columns)] for _ in range(rows)]
    
    print(f"Matrix A [{rows}x{columns}] with a python LIST structure  : {matrix_a}")
    
    # คำนวณ Transpose ของ Matrix A
    matrix_a_t = [[matrix_a[j][i] for j in range(rows)] for i in range(columns)]
    print(f"Its transpose [{columns}x{rows}]                          : {matrix_a_t}")
    print("=" * 80)

    # คำนวณผลคูณ A x A^T
    result = [[sum(matrix_a[i][k] * matrix_a_t[k][j] for k in range(columns)) for j in range(rows)] for i in range(rows)]

    print("Calculation details for a multiplication of a matrix A and its transpose\n")
    for i in range(rows):
        row_details = []
        for j in range(rows):
            # แสดงรายละเอียดการคำนวณ
            detail = "+".join(
                f"({matrix_a[i][k]}x{matrix_a_t[k][j]})" for k in range(columns)
            )
            total = sum(matrix_a[i][k] * matrix_a_t[k][j] for k in range(columns))
            row_details.append(f"{detail} = {total:<3}")
        print("    ".join(row_details))  # แยกแต่ละคอลัมน์ด้วยระยะห่างที่เหมาะสม
    
    print("\nMultiplication result [{}x{}]                  : {}".format(rows, rows, result))
    print("=" * 80 + "\n")