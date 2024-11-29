# โค้ดสร้างปิรามิดกลับหัว
print('---------- Drawing inverted pyramids ----------')
print('[To quit the program, press "0"]')
print("-----------------------------------------------------------")

while True:
    size = int(input("Please enter the height of the inverted pyramid (at least 2): "))

    if size == 0:
        break
    elif size >= 2:
        for i in range(size):
            print(" " * i + "#" * (2 * (size - i) - 1))
    else:
        print("Invalid input. Please enter a size >= 2.")
