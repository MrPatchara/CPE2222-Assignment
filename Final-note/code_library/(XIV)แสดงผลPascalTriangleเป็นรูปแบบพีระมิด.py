def pascal_triangle_pyramid(n):
    def generate_row(row):
        current = [1]
        for i in range(1, len(row)):
            current.append(row[i - 1] + row[i])
        current.append(1)
        return current

    triangle = [[1]]
    for _ in range(1, n + 1):
        triangle.append(generate_row(triangle[-1]))

    return triangle

# รับค่าระดับ
n = int(input("Enter number of rows for Pascal Triangle Pyramid: "))
triangle = pascal_triangle_pyramid(n)

# แสดงผลในรูปแบบพีระมิด
for i, row in enumerate(triangle):
    print(" " * (n - i), " ".join(map(str, row)))
