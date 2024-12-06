# Drawing a reversed right triangle with background colors
while True:
    height = int(input("Enter the height of the triangle (0 to quit): "))
    if height == 0:
        break
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '\033[44m' + '*' * i + '\033[0m'
        print(spaces + stars)
    print()