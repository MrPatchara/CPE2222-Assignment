while True:
    height = int(input("Enter the height of hollow isosceles triangle: "))

    if height == 0:
        break

    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        if i == 1:
            stars = '*'
        elif i == height:
            stars = '*' * i
        else:
            stars = '*' + ' ' * (i - 2) + '*'
        print(spaces + stars)
    print()