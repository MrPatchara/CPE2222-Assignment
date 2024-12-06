# ฟังก์ชัน Pascal Triangle แบบ Modular (ผลลัพธ์ mod k)
def pascal_triangle_modular(n, k):
    triangle = [] # สร้างรายการเก็บแถว
    for i in range(n + 1): # วนลูปเพื่อสร้างแถว
        row = [1] # สร้างแถวใหม่
        if i > 0: # สร้างตัวเลขใหม่ในแถวที่มากกว่า 0
            for j in range(1, i): # วนลูปเพื่อสร้างตัวเลขใหม่
                row.append((triangle[i - 1][j - 1] + triangle[i - 1][j]) % k)  # คำนวณผลลัพธ์ mod k
            row.append(1) # เพิ่มตัวเลขสุดท้าย
        triangle.append(row) # เพิ่มแถวใหม่เข้าไปในรายการ
    return triangle

# รับค่าระดับและตัวเลขที่ใช้ mod
n = int(input("Enter the number of rows for Pascal Triangle: "))
k = int(input("Enter the modular value: "))
result = pascal_triangle_modular(n, k)

# แสดงผล
for row in result:
    print(row)
