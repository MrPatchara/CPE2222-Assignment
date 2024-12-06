# ฟังก์ชันที่แสดง Pascal Triangle ทั้งหมด
def pascal_triangle_all(n):
    if n == 0:
        return [[1]]  # ระดับแรกของ Pascal Triangle มีเพียง 1
    else:
        previous = pascal_triangle_all(n - 1)  # เรียกฟังก์ชันเดิมสำหรับระดับก่อนหน้า
        last_row = previous[-1]  # แถวสุดท้ายของ Pascal Triangle
        current_row = [1]  # เริ่มแถวใหม่ด้วย 1

        # สร้างค่ากลางของแถวใหม่
        for i in range(1, len(last_row)):
            current_row.append(last_row[i - 1] + last_row[i])

        current_row.append(1)  # จบแถวด้วย 1
        previous.append(current_row)  # เพิ่มแถวใหม่ลงไปใน Pascal Triangle ทั้งหมด
        return previous

# รับค่าระดับของ Pascal Triangle จากผู้ใช้
n = int(input("Enter the number of rows for Pascal Triangle: "))
result = pascal_triangle_all(n)

# แสดงผล Pascal Triangle ในรูปแบบลิสต์ซ้อน
for row in result:
    print(row)
