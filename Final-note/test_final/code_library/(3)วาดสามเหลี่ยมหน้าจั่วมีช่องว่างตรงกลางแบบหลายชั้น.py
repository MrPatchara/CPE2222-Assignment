# โปรแกรมสร้างรูปสามเหลี่ยมหน้าจั่วที่มีชั้นว่าง
while True:
    height = int(input("Enter the height of isosceles triangle with hollow layers: "))

    if height == 0:
        break

    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        if i == 1:
            stars = '*'
        elif i == height:
            stars = '*' * (2 * i - 1)
        else:
            stars = '*' + ' ' * (2 * i - 3) + '*'
        print(spaces + stars)
    print()