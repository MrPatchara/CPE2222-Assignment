print('---------- Drawing the square rectangular by "#" ----------')
print('[To quit the program, press "0"]')
print("-----------------------------------------------------------")

while True:
    size = int(input("Please enter the size: "))

    if size == 0:
        break
    elif size >= 2:
        print("#" * size)
        for i in range(size-2):
            print(f"#" + " " * (size - 2) + "#")
        print("#" * size)
    elif size == 1:
        print("#" * size)