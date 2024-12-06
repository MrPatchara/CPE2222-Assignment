# Drawing a reversed right triangle with increasing numbers in each row
while True:
    height = int(input("Enter the height of the triangle (0 to quit): "))
    if height == 0:
        break
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = ''.join(str(j % 10) for j in range(1, i + 1))
        print(spaces + stars)
    print()