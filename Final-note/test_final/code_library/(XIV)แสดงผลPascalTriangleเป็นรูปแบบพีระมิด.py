# โปรแกรมสร้างพีระมิด Pascal Triangle โดยใช้ Python
def pascal_triangle_pyramid(n):
    def generate_row(row):
        current = [1] # สร้างแถวใหม่
        for i in range(1, len(row)): # วนลูปเพื่อสร้างตัวเลขใหม่
            current.append(row[i - 1] + row[i]) # สร้างตัวเลขใหม่จากผลรวม
        current.append(1) # เพิ่มตัวเลขสุดท้าย
        return current

    triangle = [[1]] # สร้างแถวแรก
    for _ in range(1, n + 1): # วนลูปเพื่อสร้างแถว
        triangle.append(generate_row(triangle[-1])) # เพิ่มแถวใหม่เข้าไปในรายการ

    return triangle

# รับค่าระดับ
n = int(input("Enter number of rows for Pascal Triangle Pyramid: "))
triangle = pascal_triangle_pyramid(n)

# แสดงผลในรูปแบบพีระมิด
for i, row in enumerate(triangle): # วนลูปเพื่อแสดงผล
    print(" " * (n - i), " ".join(map(str, row))) # แสดงผลลัพธ์
