# Drawing a reversed right triangle with different symbols per row
while True:
    height = int(input("Enter the height of the triangle (0 to quit): "))
    if height == 0:
        break
    symbols = ['*', '#', '@', '%', '+']
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = symbols[i % len(symbols)] * i
        print(spaces + stars)
    print()