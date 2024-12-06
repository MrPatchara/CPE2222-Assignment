# โปรแกรมสร้าง Pascal Triangle แต่แสดงเฉพาะเลขคู่เท่านั้น
def pascal_triangle_even_only(n): # ฟังก์ชันสร้าง Pascal Triangle แต่แสดงเฉพาะเลขคู่
    triangle = []  # เริ่มต้นด้วยลิสต์ว่าง
    for i in range(n + 1): # วนลูปเพื่อสร้างแถว
        row = [1] # สร้างแถวใหม่
        if i > 0: # สร้างตัวเลขใหม่ในแถวที่มากกว่า 0
            for j in range(1, i): # วนลูปเพื่อสร้างตัวเลขใหม่
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j]) # สร้างตัวเลขใหม่จากผลรวม
            row.append(1) # เพิ่มตัวเลขสุดท้าย
        # แทนค่าที่ไม่ใช่เลขคู่ด้วย "-" เพื่อเน้นเลขคู่
        row = ["-" if x % 2 != 0 else x for x in row] # แทนค่าที่ไม่ใช่เลขคู่ด้วย "-"
        triangle.append(row) # เพิ่มแถวใหม่เข้าไปในรายการ
    return triangle

# รับค่าระดับ
n = int(input("Enter the number of rows for Pascal Triangle (even numbers only): "))
result = pascal_triangle_even_only(n)

# แสดงผล
for row in result:
    print(" ".join(map(str, row)))
