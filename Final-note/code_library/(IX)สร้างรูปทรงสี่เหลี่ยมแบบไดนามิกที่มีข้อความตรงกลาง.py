# โค้ดสร้างสี่เหลี่ยมพร้อมข้อความตรงกลาง
print('---------- Drawing squares with a message ----------')
print('[To quit the program, press "0"]')
print("-----------------------------------------------------------")

while True:
    size = int(input("Please enter the size (at least 5): "))
    message = input("Enter a message to center (max 1 less than size): ")

    if size == 0:
        break
    elif size >= 5 and len(message) <= size - 2:
        print("#" * size)
        for i in range(size - 2):
            if i == (size - 2) // 2:  # แสดงข้อความตรงกลาง
                padding = (size - 2 - len(message)) // 2
                print("#" + " " * padding + message + " " * padding + "#")
            else:
                print("#" + " " * (size - 2) + "#")
        print("#" * size)
    else:
        print("Invalid input. Ensure message length < size and size >= 5.")
