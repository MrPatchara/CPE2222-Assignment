while True:
    height = int(input("Enter the height of hollow diamond (must be odd): "))

    if height == 0:
        break
    if height % 2 == 0:
        print("Height must be an odd number!")
        continue

    for i in range(1, height + 1, 2):
        spaces = ' ' * ((height - i) // 2)
        if i == 1:
            stars = '*'
        else:
            stars = '*' + ' ' * (i - 2) + '*'
        print(spaces + stars)

    for i in range(height - 2, 0, -2):
        spaces = ' ' * ((height - i) // 2)
        if i == 1:
            stars = '*'
        else:
            stars = '*' + ' ' * (i - 2) + '*'
        print(spaces + stars)
    print()