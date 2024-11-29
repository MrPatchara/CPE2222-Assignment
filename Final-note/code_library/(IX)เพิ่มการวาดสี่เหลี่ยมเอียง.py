# โค้ดสร้างสี่เหลี่ยมเอียง
print('---------- Drawing tilted squares ----------')
print('[To quit the program, press "0"]')
print("-----------------------------------------------------------")

while True:
    size = int(input("Please enter the size (at least 3): "))

    if size == 0:
        break
    elif size >= 3:
        for i in range(size):
            if i == 0 or i == size - 1:  # ด้านบนและด้านล่าง
                print(" " * (size - i - 1) + "#" * size)
            else:  # ด้านข้าง
                print(" " * (size - i - 1) + "#" + " " * (size - 2) + "#")
    else:
        print("Invalid input. Please enter a size >= 3.")
