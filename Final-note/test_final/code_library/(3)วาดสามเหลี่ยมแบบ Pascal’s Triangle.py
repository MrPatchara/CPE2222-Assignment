while True:
    # รับจำนวนแถวจากผู้ใช้
    rows = int(input("Enter the number of rows for Pascal's Triangle: "))

    if rows == 0:  # หากใส่ 0 จะออกจากโปรแกรม
        break

    # วาด Pascal's Triangle
    triangle = [[1]]
    for i in range(1, rows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    for row in triangle:
        print(' '.join(map(str, row)).center(2 * rows))
    print()  # ขึ้นบรรทัดใหม่