# Drawing a reversed right triangle with increasing letters in each row
while True:
    height = int(input("Enter the height of the triangle (0 to quit): "))
    if height == 0:
        break
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = ''.join(chr(65 + (j % 26)) for j in range(i))
        print(spaces + stars)
    print()