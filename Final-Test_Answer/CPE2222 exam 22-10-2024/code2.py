def triangle(degree):
    triangle = [[1]]  # Degree 0
    
    for d in range(1, degree + 1):
        row = [1]  # ค่าแรกในแถวคือ 1
        prev_row = triangle[d - 1]  # แถวก่อนหน้า
        # คำนวณค่ากลาง
        for i in range(1, d):
            middle_value = (prev_row[i - 1] + prev_row[i]) * 2 - prev_row[i - 1]
            row.append(middle_value)
        # ค่าสุดท้ายในแถว
        row.append(3 ** d)
        triangle.append(row)
    return triangle

degree = int(input("Enter the degree of triangle: "))

triangle = triangle(degree)

print(f"{triangle[degree]}\n")
