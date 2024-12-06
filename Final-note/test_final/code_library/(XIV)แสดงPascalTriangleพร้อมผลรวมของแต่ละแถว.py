# โปรแกรมสร้าง Pascal Triangle และคำนวณผลรวมของแต่ละแถว
def pascal_triangle_with_sum(n):
    triangle = [] # สร้างรายการเก็บแถว
    row_sums = [] # สร้างรายการเก็บผลรวมของแต่ละแถว
    for i in range(n + 1): # วนลูปเพื่อสร้างแถว
        row = [1] # สร้างแถวใหม่
        if i > 0: # สร้างตัวเลขใหม่ในแถวที่มากกว่า 0
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j]) # สร้างตัวเลขใหม่จากผลรวม
            row.append(1) # เพิ่มตัวเลขสุดท้าย
        triangle.append(row)    # เพิ่มแถวใหม่เข้าไปในรายการ
        row_sums.append(sum(row))  # คำนวณผลรวมของแต่ละแถว 
    return triangle, row_sums # ส่งค่ากลับ

# รับค่าระดับ
n = int(input("Enter the number of rows for Pascal Triangle: "))
triangle, row_sums = pascal_triangle_with_sum(n) # เรียกใช้ฟังก์ชัน

# แสดงผล
for i, row in enumerate(triangle): # วนลูปเพื่อแสดงผล
    print(f"Row {i}: {row} (Sum: {row_sums[i]})") # แสดงผลลัพธ์
