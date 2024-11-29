def pascal_triangle_with_sum(n):
    triangle = []
    row_sums = []
    for i in range(n + 1):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
        triangle.append(row)
        row_sums.append(sum(row))  # คำนวณผลรวมของแต่ละแถว
    return triangle, row_sums

# รับค่าระดับ
n = int(input("Enter the number of rows for Pascal Triangle: "))
triangle, row_sums = pascal_triangle_with_sum(n)

# แสดงผล
for i, row in enumerate(triangle):
    print(f"Row {i}: {row} (Sum: {row_sums[i]})")
