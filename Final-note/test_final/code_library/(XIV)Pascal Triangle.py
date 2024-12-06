# โปรแกรมสร้าง Pascal Triangle โดยใช้ Recursive Function
def pascal_triangle(input_number):
    if input_number == 0:
        return [1]

    else:
        previous_row = pascal_triangle(input_number - 1) # เรียกใช้ฟังก์ชันเดิม
        current_row = [1] # สร้างแถวใหม่

        for i in range(1, len(previous_row)): # วนลูปเพื่อสร้างตัวเลขใหม่
            current_row.append(previous_row[i - 1] + previous_row[i]) # สร้างตัวเลขใหม่จากผลรวม

        current_row.append(1) # เพิ่มตัวเลขสุดท้าย
        return current_row # ส่งค่ากลับ

input_number = int(input("Please Enter Degree of Pascal Triangle: "))
print(f"{pascal_triangle(input_number)}\n")