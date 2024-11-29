#2.พิจารณาสามเหลี่ยม

def generate_triangle(degree):
    # สร้างสามเหลี่ยมเริ่มต้น
    triangle = [[1]]  # Degree 0
    
    for d in range(1, degree + 1):
        row = [1]  # ค่าแรกในแถวคือ 1
        prev_row = triangle[d - 1]  # แถวก่อนหน้า
        
        # คำนวณค่ากลาง
        for i in range(1, d):
            # คำนวณค่ากลางตามสูตรใหม่
            middle_value = (prev_row[i - 1] + prev_row[i]) * 2 - prev_row[i - 1]
            row.append(middle_value)
        
        # ค่าสุดท้ายในแถวคือ 3^d
        row.append(3 ** d)
        triangle.append(row)
    
    return triangle

# รับค่า Degree จากผู้ใช้
degree = int(input("Enter the degree of triangle: "))

# สร้างรายการสัมประสิทธิ์
triangle = generate_triangle(degree)

# แสดงผลลัพธ์
print(f"{triangle[degree]}\n")
