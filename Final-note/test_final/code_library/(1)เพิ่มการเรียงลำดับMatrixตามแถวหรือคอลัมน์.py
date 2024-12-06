# โปรแกรมสร้างเมทริกซ์จากตัวเลขสุ่ม และให้ผู้ใช้เลือกเรียงลำดับตามแถวหรือคอลัมน์
import random

print("=" * 80)
rows = int(input("Enter a number of rows: "))
columns = int(input("Enter a number of columns: "))

if rows < 1 or columns < 1: # ตรวจสอบขนาดของ Matrix
    print("!!! Rows and columns must be at least 1 !!!")
    exit()

# สุ่มค่าจำนวนเต็ม 0-20 สำหรับ Matrix A
matrix_a = [[random.randint(0, 20) for _ in range(columns)] for _ in range(rows)]  # สร้าง Matrix แบบสุ่ม
print(f"Original Matrix A [{rows}x{columns}]: {matrix_a}")

# เลือกการเรียงลำดับ
sort_by = input("Sort matrix by rows or columns? (r/c): ").strip().lower() # รับข้อมูลการเรียงลำดับ
if sort_by == "r": # เรียงลำดับตามแถว
    # เรียงลำดับตามแถว
    sorted_matrix = [sorted(row) for row in matrix_a] # เรียงลำดับแต่ละแถวของ Matrix
    print(f"Matrix sorted by rows: {sorted_matrix}")
elif sort_by == "c": # เรียงลำดับตามคอลัมน์
    # เรียงลำดับตามคอลัมน์
    transposed = [[matrix_a[j][i] for j in range(rows)] for i in range(columns)] 
    sorted_transposed = [sorted(row) for row in transposed] # เรียงลำดับแต่ละคอลัมน์ของ Matrix
    sorted_matrix = [[sorted_transposed[i][j] for i in range(columns)] for j in range(rows)]
    print(f"Matrix sorted by columns: {sorted_matrix}")
else:
    print("Invalid choice!")