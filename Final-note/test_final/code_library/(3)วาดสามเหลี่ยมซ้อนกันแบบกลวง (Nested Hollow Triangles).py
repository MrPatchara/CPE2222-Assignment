while True:
    height = int(input("Enter the height of nested hollow triangles: "))

    if height == 0:
        break

    for i in range(1, height + 1):
        for j in range(1, i + 1):
            spaces = ' ' * (height - j)
            if j == 1 or j == i:
                stars = '*' * j
            else:
                stars = '*' + ' ' * (j - 2) + '*'
            print(spaces + stars)
    print()