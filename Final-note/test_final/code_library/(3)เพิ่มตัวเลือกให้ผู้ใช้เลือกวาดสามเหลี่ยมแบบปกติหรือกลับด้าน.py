# Drawing a right or reversed right triangle based on user choice
while True:
    height = int(input("Enter the height of the triangle (0 to quit): "))
    if height == 0:
        break
    direction = input("Draw normal or reversed triangle? (n/r): ").strip().lower()
    if direction == 'r':
        for i in range(1, height + 1):
            spaces = ' ' * (height - i)
            stars = '*' * i
            print(spaces + stars)
    elif direction == 'n':
        for i in range(height, 0, -1):
            stars = '*' * i
            print(stars)
    print()