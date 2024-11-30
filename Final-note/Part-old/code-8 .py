import random

def main():
    # รับค่าจำนวนแถวและจำนวนสดมภ์
    rows = int(input("Enter a number of rows: "))
    cols = int(input("Enter a number of columns: "))

    # ตรวจสอบข้อกำหนด
    if rows > 3 or cols > 3:
        print("!!! Error in a number of rows or columns !!!")
        return

    # สุ่มค่าให้กับสมาชิกของ Matrix A
    matrix_a = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]

    # แสดง Matrix A
    print("="*58)
    print(f"Matrix A [{rows}x{cols}] with a python LIST structure    : {matrix_a}")

    # คำนวณ Transpose ของ Matrix A
    matrix_at = [[matrix_a[j][i] for j in range(rows)] for i in range(cols)]
    print(f"Its transpose [{cols}x{rows}]")
    print("="*58)

    # คำนวณ A * A^T
    result = [[sum(matrix_a[i][k] * matrix_at[k][j] for k in range(cols)) for j in range(rows)] for i in range(rows)]

    # แสดงรายละเอียดการคำนวณ
    print("Calculation details for a multiplication of matrix A and its transpose\n")
    for i in range(rows):
        for j in range(rows):
            calc = " + ".join([f"({matrix_a[i][k]}x{matrix_at[k][j]})" for k in range(cols)])
            print(f"{calc} = {result[i][j]}", end="\t\t")
        print()

    # แสดงผลลัพธ์
    print(f"\nMultiplication result [{rows}x{rows}]                     : {result}")
    print("="*58)

# เรียกใช้ฟังก์ชันหลัก
main()
