# ฟังก์ชัน Pascal Triangle แบบ Modular (ผลลัพธ์ mod k)
def pascal_triangle_modular(n, k):
    triangle = []
    for i in range(n + 1):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append((triangle[i - 1][j - 1] + triangle[i - 1][j]) % k)  # ผลลัพธ์ mod k
            row.append(1)
        triangle.append(row)
    return triangle

# รับค่าระดับและตัวเลขที่ใช้ mod
n = int(input("Enter the number of rows for Pascal Triangle: "))
k = int(input("Enter the modular value: "))
result = pascal_triangle_modular(n, k)

# แสดงผล
for row in result:
    print(row)
