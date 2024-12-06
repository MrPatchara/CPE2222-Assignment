# โปรแกรมสร้าง Pascal Triangle แบบเลขฐาน 2
def pascal_triangle_binary(n): # ฟังก์ชันสร้าง Pascal Triangle แบบเลขฐาน 2
    triangle = [] # เริ่มต้นด้วยลิสต์ว่าง
    for i in range(n + 1): # วนลูปเพื่อสร้างแถว
        row = [1] # สร้างแถวใหม่
        if i > 0: # สร้างตัวเลขใหม่ในแถวที่มากกว่า 0
            for j in range(1, i): # วนลูปเพื่อสร้างตัวเลขใหม่
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j]) # สร้างตัวเลขใหม่จากผลรวม
            row.append(1) # เพิ่มตัวเลขสุดท้าย
        # แปลงค่าทั้งหมดในแถวเป็นเลขฐาน 2
        row = [bin(x)[2:] for x in row] # แปลงค่าทั้งหมดในแถวเป็นเลขฐาน 2
        triangle.append(row) # เพิ่มแถวใหม่เข้าไปในรายการ
    return triangle

# รับค่าระดับ
n = int(input("Enter the number of rows for Pascal Triangle (binary format): "))
result = pascal_triangle_binary(n)

# แสดงผล
for row in result: # วนลูปเพื่อแสดงผล
    print(" ".join(row)) # แสดงผลลัพธ์
