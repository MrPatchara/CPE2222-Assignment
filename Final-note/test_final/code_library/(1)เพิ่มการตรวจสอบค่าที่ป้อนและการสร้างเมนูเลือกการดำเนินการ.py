# โปรแกรมสร้างเมทริกซ์และสามารถเลือกดำเนินการได้ 2 แบบ: 
# 1. สร้างเมทริกซ์และหา Transpose 
# 2. สร้างเมทริกซ์และคำนวณ Determinant (เฉพาะกรณีเมทริกซ์สี่เหลี่ยมจัตุรัส)
import random

print("=" * 80)
try:
    rows = int(input("Enter a number of rows: ")) # รับขนาดของ Matrix
    columns = int(input("Enter a number of columns: ")) # รับขนาดของ Matrix
except ValueError: # กรณีป้อนข้อมูลผิดพลาด
    print("Invalid input! Please enter integers only.") # แสดงข้อความแจ้งเตือน
    exit()

# ตรวจสอบว่าขนาดอยู่ในขอบเขตที่กำหนด
if rows < 1 or columns < 1:
    print("!!! Number of rows and columns must be at least 1 !!!") # แสดงข้อความแจ้งเตือน
    exit()

# เมนูการดำเนินการ
print("Choose an operation:") 
print("1. Generate matrix and transpose")
print("2. Generate matrix and compute determinant (if square matrix)")
choice = input("Enter your choice (1 or 2): ")

if choice == "1": # กรณีเลือก 1
    # สุ่มค่าจำนวนเต็มสำหรับ Matrix A
    matrix_a = [[random.randint(0, 9) for _ in range(columns)] for _ in range(rows)] # สร้าง Matrix แบบสุ่ม
    print(f"Matrix A [{rows}x{columns}]  : {matrix_a}") # แสดง Matrix A

    # คำนวณ Transpose
    matrix_a_t = [[matrix_a[j][i] for j in range(rows)] for i in range(columns)]
    print(f"Transpose [{columns}x{rows}]: {matrix_a_t}")

elif choice == "2" and rows == columns:
    # สุ่มค่าจำนวนเต็มสำหรับ Matrix A (ต้องเป็น Matrix สี่เหลี่ยมจัตุรัส)
    matrix_a = [[random.randint(1, 9) for _ in range(rows)] for _ in range(rows)] # สร้าง Matrix แบบสุ่ม
    print(f"Matrix A [{rows}x{rows}]: {matrix_a}") # แสดง Matrix A

    # คำนวณ Determinant (เฉพาะกรณี 2x2 หรือ 3x3)
    if rows == 2: # กรณี Matrix 2x2
        det = matrix_a[0][0] * matrix_a[1][1] - matrix_a[0][1] * matrix_a[1][0] # คำนวณ Determinant ของ Matrix 2x2
    elif rows == 3: # กรณี Matrix 3x3
        det = (
            matrix_a[0][0] * (matrix_a[1][1] * matrix_a[2][2] - matrix_a[1][2] * matrix_a[2][1])
            - matrix_a[0][1] * (matrix_a[1][0] * matrix_a[2][2] - matrix_a[1][2] * matrix_a[2][0])
            + matrix_a[0][2] * (matrix_a[1][0] * matrix_a[2][1] - matrix_a[1][1] * matrix_a[2][0])
        )
    else:
        print("Determinant calculation for matrices larger than 3x3 is not implemented.")
        det = None # กำหนดค่า Determinant เป็น None

    print(f"Determinant of Matrix A: {det if det is not None else 'Unavailable'}") # แสดงค่า Determinant หรือข้อความแจ้งเตือน
else:
    print("Invalid choice or incompatible matrix size for determinant.")