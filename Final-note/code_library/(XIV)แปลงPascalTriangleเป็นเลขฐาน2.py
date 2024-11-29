def pascal_triangle_binary(n):
    triangle = []
    for i in range(n + 1):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
        # แปลงค่าทั้งหมดในแถวเป็นเลขฐาน 2
        row = [bin(x)[2:] for x in row]
        triangle.append(row)
    return triangle

# รับค่าระดับ
n = int(input("Enter the number of rows for Pascal Triangle (binary format): "))
result = pascal_triangle_binary(n)

# แสดงผล
for row in result:
    print(" ".join(row))
