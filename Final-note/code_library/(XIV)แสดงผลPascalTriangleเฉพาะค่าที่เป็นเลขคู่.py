def pascal_triangle_even_only(n):
    triangle = []  # เริ่มต้นด้วยลิสต์ว่าง
    for i in range(n + 1):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
        # แทนค่าที่ไม่ใช่เลขคู่ด้วย "-" เพื่อเน้นเลขคู่
        row = ["-" if x % 2 != 0 else x for x in row]
        triangle.append(row)
    return triangle

# รับค่าระดับ
n = int(input("Enter the number of rows for Pascal Triangle (even numbers only): "))
result = pascal_triangle_even_only(n)

# แสดงผล
for row in result:
    print(" ".join(map(str, row)))
