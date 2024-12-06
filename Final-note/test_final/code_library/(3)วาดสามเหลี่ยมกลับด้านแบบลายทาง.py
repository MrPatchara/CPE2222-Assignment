# Drawing a reversed right triangle with alternating striped rows
while True:
    height = int(input("Enter the height of the triangle (0 to quit): "))
    if height == 0:
        break
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        if i % 2 == 0:
            stars = '*' * i
        else:
            stars = '#' * i
        print(spaces + stars)
    print()