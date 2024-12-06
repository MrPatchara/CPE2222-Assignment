# โปรแกรมสร้างสี่เหลี่ยมลายขวาง
# โค้ดสร้างสี่เหลี่ยมลายขวาง
print('---------- Drawing striped squares ----------')
print('[To quit the program, press "0"]')
print("-----------------------------------------------------------")

while True:
    size = int(input("Please enter the size (at least 3): "))

    if size == 0:
        break
    elif size >= 3:
        for i in range(size):
            if i % 2 == 0:
                print("#" * size)
            else:
                print(" " * size)
    else:
        print("Invalid input. Please enter a size >= 3.")
