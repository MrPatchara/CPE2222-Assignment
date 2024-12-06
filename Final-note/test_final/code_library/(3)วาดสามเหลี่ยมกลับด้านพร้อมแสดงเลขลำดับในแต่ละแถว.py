# Drawing a reversed right triangle with numbers in each row
while True:
    height = int(input("Enter the height of the triangle (0 to quit): "))
    if height == 0:
        break
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        if i == 1:
            stars = f"{i}"
        elif i == height:
            stars = ' '.join(str(j) for j in range(1, i + 1))
        else:
            stars = f"{i}" + ' ' * (2 * (i - 2)) + f"{i}"
        print(spaces + stars)
    print()