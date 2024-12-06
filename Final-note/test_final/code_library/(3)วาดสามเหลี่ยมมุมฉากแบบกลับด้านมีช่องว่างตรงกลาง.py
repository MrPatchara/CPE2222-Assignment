while True:
    height = int(input("Enter the height of reversed right triangle with space inside: "))

    if height == 0:
        break

    for i in range(height, 0, -1):
        spaces = ' ' * (height - i)
        if i == 1:
            stars = '*'
        elif i == height:
            stars = '*' * i
        else:
            stars = '*' + ' ' * (i - 2) + '*'
        print(spaces + stars)
    print()