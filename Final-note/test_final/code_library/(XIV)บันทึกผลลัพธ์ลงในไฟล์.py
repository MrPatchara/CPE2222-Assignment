# โปรแกรมสร้าง Pascal Triangle และบันทึกลงในไฟล์
def pascal_triangle_to_file(n, filename): # ฟังก์ชันสร้าง Pascal Triangle และบันทึกลงในไฟล์
    def generate_row(row): # ฟังก์ชันสร้างแถวใหม่
        current = [1] # สร้างแถวใหม่
        for i in range(1, len(row)): # วนลูปเพื่อสร้างตัวเลขใหม่
            current.append(row[i - 1] + row[i]) # สร้างตัวเลขใหม่จากผลรวม
        current.append(1) # เพิ่มตัวเลขสุดท้าย
        return current # ส่งค่ากลับ

    triangle = [[1]] # สร้างแถวแรก
    for _ in range(1, n + 1): # วนลูปเพื่อสร้างแถว
        triangle.append(generate_row(triangle[-1])) # เพิ่มแถวใหม่เข้าไปในรายการ

    # บันทึกผลลงในไฟล์
    with open(filename, 'w') as file: # เปิดไฟล์เพื่อเขียน
        for row in triangle: # วนลูปเพื่อบันทึกแถวลงในไฟล์
            file.write(" ".join(map(str, row)) + "\n") # บันทึกแถวลงในไฟล์

    return f"Pascal Triangle saved to {filename}" # ส่งค่ากลับ

# รับค่าระดับ
n = int(input("Enter number of rows for Pascal Triangle: "))
print(pascal_triangle_to_file(n, "pascal_triangle.txt"))
