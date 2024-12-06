while True:
    height = int(input("Enter the height of hollow reversed equilateral triangle: "))

    if height == 0:
        break

    for i in range(height, 0, -1):
        spaces = ' ' * (height - i)
        if i == 1:
            stars = '*'
        elif i == height:
            stars = '*' + ' ' * (2 * i - 3) + '*'
        else:
            stars = '*' + ' ' * (2 * i - 3) + '*'
        print(spaces + stars)
    print()