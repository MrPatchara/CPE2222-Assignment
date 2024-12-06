# โค้ดสร้างปิรามิด
print('---------- Drawing pyramids ----------')
print('[To quit the program, press "0"]')
print("-----------------------------------------------------------")

while True:
    size = int(input("Please enter the height of the pyramid (at least 2): "))

    if size == 0:
        break
    elif size >= 2:
        for i in range(size):
            print(" " * (size - i - 1) + "#" * (2 * i + 1))
    else:
        print("Invalid input. Please enter a size >= 2.")
