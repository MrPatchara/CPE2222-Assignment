def pascal_triangle_to_file(n, filename):
    def generate_row(row):
        current = [1]
        for i in range(1, len(row)):
            current.append(row[i - 1] + row[i])
        current.append(1)
        return current

    triangle = [[1]]
    for _ in range(1, n + 1):
        triangle.append(generate_row(triangle[-1]))

    # บันทึกผลลงในไฟล์
    with open(filename, 'w') as file:
        for row in triangle:
            file.write(" ".join(map(str, row)) + "\n")

    return f"Pascal Triangle saved to {filename}"

# รับค่าระดับ
n = int(input("Enter number of rows for Pascal Triangle: "))
print(pascal_triangle_to_file(n, "pascal_triangle.txt"))
