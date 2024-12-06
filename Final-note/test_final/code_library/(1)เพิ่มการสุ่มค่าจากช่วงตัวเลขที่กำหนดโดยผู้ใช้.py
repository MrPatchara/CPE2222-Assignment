# โปรแกรมสร้างเมทริกซ์ด้วยขนาดที่ผู้ใช้ระบุ และสุ่มค่าตัวเลขในช่วงที่กำหนด
# พร้อมทั้งแสดง Transpose และผลรวมของแนวทแยง (ถ้าเป็นเมทริกซ์สี่เหลี่ยมจัตุรัส)
import random 

print("=" * 80)
rows = int(input("Enter a number of rows: "))
columns = int(input("Enter a number of columns: "))

if rows > 5 or columns > 5:
    print("Matrix size too large! Try smaller dimensions.")
    exit()

# ให้ผู้ใช้กำหนดช่วงตัวเลขสุ่ม
min_val = int(input("Enter minimum random value: "))
max_val = int(input("Enter maximum random value: "))

matrix_a = [[random.randint(min_val, max_val) for _ in range(columns)] for _ in range(rows)]
print(f"Matrix A [{rows}x{columns}]: {matrix_a}")

# คำนวณ Transpose
matrix_a_t = [[matrix_a[j][i] for j in range(rows)] for i in range(columns)]
print(f"Transpose [{columns}x{rows}]: {matrix_a_t}")

# ตรวจสอบว่า Matrix A เป็นสี่เหลี่ยมจัตุรัสและคำนวณผลรวมแนวทแยง
if rows == columns:
    diag_sum = sum(matrix_a[i][i] for i in range(rows))
    print(f"Sum of main diagonal elements: {diag_sum}")