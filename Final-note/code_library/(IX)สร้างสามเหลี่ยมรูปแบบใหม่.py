# โค้ดสร้างสามเหลี่ยมล่างขวา
print('---------- Drawing right-bottom triangle ----------')
print('[To quit the program, press "0"]')
print("-----------------------------------------------------------")

while True:
    size = int(input("Please enter the size (at least 2): "))

    if size == 0:
        break
    elif size >= 2:
        for i in range(1, size + 1):
            print(" " * (size - i) + "#" * i)
    else:
        print("Invalid input. Please enter a size >= 2.")
