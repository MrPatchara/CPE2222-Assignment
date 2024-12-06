# โปรแกรมสร้างเมทริกซ์โดยใช้ฟังก์ชันแบบ Lambda
print('*' * 70)
print('Matrix Function using Lambda'.center(70))
print('*' * 70)

# สร้างฟังก์ชันเมทริกซ์แบบยืดหยุ่น
create_matrix = lambda rows, cols: [[i * j for j in range(1, cols+1)] for i in range(1, rows+1)]

# รับขนาดเมทริกซ์จากผู้ใช้
rows, cols = map(int, input("Enter matrix dimensions (rows cols): ").split())

# สร้างเมทริกซ์
matrix = create_matrix(rows, cols)

print("\nGenerated Matrix:")
for row in matrix:
    print(row)