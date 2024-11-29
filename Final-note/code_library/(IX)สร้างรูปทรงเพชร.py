# โค้ดสร้างเพชร
print('---------- Drawing diamonds ----------')
print('[To quit the program, press "0"]')
print("-----------------------------------------------------------")

while True:
    size = int(input("Please enter the size (at least 3): "))

    if size == 0:
        break
    elif size >= 3:
        # ส่วนบน
        for i in range(size):
            print(" " * (size - i - 1) + "#" * (2 * i + 1))
        # ส่วนล่าง
        for i in range(size - 2, -1, -1):
            print(" " * (size - i - 1) + "#" * (2 * i + 1))
    else:
        print("Invalid input. Please enter a size >= 3.")
