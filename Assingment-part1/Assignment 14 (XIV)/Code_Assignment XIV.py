# Assignment XIV: Pascal Triangle
def pascal_triangle(degree):
    if degree == 0: # ถ้า degree เป็น 0 ให้ return 1 ซึ่งเป็นแถวแรกของ Pascal Triangle เพราะแถวแรกของ Pascal Triangle มีค่าเป็น [1]
        return [1]
    else: # ถ้าไม่ให้ทำการคำนวณ
        previous_row = pascal_triangle(degree - 1) # คำนวณค่า degree ก่อนหน้า
        current_row = [1]  # สร้าง list ใหม่โดยเริ่มต้นด้วย 1
        for i in range(len(previous_row) - 1): # วนลูปเพื่อคำนวณค่าใน degree ปัจจุบัน
            current_row.append(previous_row[i] + previous_row[i + 1]) # คำนวณค่าใน degree ปัจจุบัน
        current_row.append(1) # เพิ่มค่า 1 ท้ายสุด
        return current_row # คืนค่า current_row

# รับค่า degree จากผู้ใช้
degree = int(input("Please Enter Degree of Pascal Triangle: "))
# แสดงผลลัพธ์
print(pascal_triangle(degree))

