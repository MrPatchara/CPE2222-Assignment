def generate_pyramid(degree):
    # กรณี Degree 0 มีเพียง 1 ค่า
    if degree == 0:
        return [1]
    
    # เริ่มต้นจาก Degree 0 ซึ่งมีค่า [1]
    pyramid = [[1]]  
    
    for d in range(1, degree + 1):
        prev_row = pyramid[-1]  # แถวก่อนหน้า
        row = [1]  # เริ่มแถวใหม่ด้วย 1
        
        # คำนวณความแตกต่าง (difference) จากแถวก่อนหน้า
        if len(prev_row) > 1:
            differences = [prev_row[i+1] - prev_row[i] for i in range(len(prev_row) - 1)]
        
            # เติมค่าตามความแตกต่าง
            for diff in differences:
                row.append(row[-1] + diff)  # คำนวณค่าใหม่

        # สำหรับ Degree 1 ขึ้นไป ให้เพิ่มค่าใหม่ที่เป็นตัวสุดท้าย
        if len(row) > 1:
            last_diff = row[-1] - row[-2]
            row.append(row[-1] + last_diff)
        
        pyramid.append(row)  # เพิ่มแถวใหม่ในพีระมิด
    
    return pyramid[degree]  # คืนค่าแถวที่ต้องการ

# รับค่า Degree จากผู้ใช้
degree = int(input("กรุณาใส่ค่า Degree (0 ขึ้นไป): "))
coefficients = generate_pyramid(degree)

# แสดงผลลัพธ์
print(f"Degree {degree}: {coefficients}")
