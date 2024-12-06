while True:
    height = int(input("Enter the height of hollow right triangle: "))

    if height == 0:
        break

    for i in range(1, height + 1):
        if i == 1:
            stars = '*'
        elif i == height:
            stars = '*' * i
        else:
            stars = '*' + ' ' * (i - 2) + '*'
        print(stars)
    print()