def generate_triangle(degree):
    if degree < 0:
        return []

    triangle = [[1]]  # เริ่มจาก Degree 0 ที่มี [1]

    for d in range(1, degree + 1):
        previous_row = triangle[-1]
        current_row = []
        for i in range(len(previous_row) + 1):
            if i == 0:
                # องค์ประกอบแรกของแถวใหม่
                current_row.append(previous_row[i])
            elif i == len(previous_row):
                # องค์ประกอบสุดท้ายของแถวใหม่
                current_row.append(previous_row[i - 1] + current_row[i - 1])
            else:
                # องค์ประกอบอื่น ๆ ของแถวใหม่
                current_row.append(previous_row[i - 1] + previous_row[i])
        triangle.append(current_row)
    
    return triangle[degree]

# รับค่า Degree จากผู้ใช้
degree = int(input("Please Enter Degree: "))
result = generate_triangle(degree)
print(f"Degree {degree} coefficients: {result}")
