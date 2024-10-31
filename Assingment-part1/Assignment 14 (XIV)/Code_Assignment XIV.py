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

# การทำงานหลัก
# ตรวจสอบระดับ (degree):
# ถ้า degree เป็น 0 จะคืนค่า [1] ซึ่งเป็นแถวแรกของ Pascal Triangle ที่ประกอบด้วยค่าเดียวคือ 1
# ถ้า degree ไม่ใช่ 0 ฟังก์ชันจะเรียกตัวเองซ้ำไปที่ระดับก่อนหน้า (degree - 1) เพื่อให้ได้ค่าแถวก่อนหน้าที่ต้องการ
# สร้างแถวใหม่จากแถวก่อนหน้า:
# หลังจากได้แถวก่อนหน้าแล้ว โปรแกรมจะใช้ค่าจากแถวนี้ในการคำนวณแต่ละค่าของแถวปัจจุบัน โดยบวกค่าของคู่ตัวเลขที่อยู่ติดกันในแถวก่อนหน้า
# เริ่มต้นและสิ้นสุดแถวด้วยค่า 1 เสมอ
# แสดงผลลัพธ์:
# เมื่อโปรแกรมคำนวณแถวปัจจุบันของ Pascal Triangle เสร็จแล้ว จะคืนค่าเป็นรายการ (list) ของแถวที่ตรงกับระดับที่ผู้ใช้ป้อน
# ตัวอย่างการทำงาน
# หากผู้ใช้ป้อนค่า degree = 3 ฟังก์ชันจะส่งคืนค่า [1, 3, 3, 1] ซึ่งเป็นแถวที่ 3 ของ Pascal Triangle






