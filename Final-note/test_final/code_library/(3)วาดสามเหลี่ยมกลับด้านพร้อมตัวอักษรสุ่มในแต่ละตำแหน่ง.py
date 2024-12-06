# Drawing a reversed right triangle with random letters
import random
import string

while True:
    height = int(input("Enter the height of the triangle (0 to quit): "))
    if height == 0:
        break
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = ''.join(random.choice(string.ascii_letters) for _ in range(i))
        print(spaces + stars)
    print()