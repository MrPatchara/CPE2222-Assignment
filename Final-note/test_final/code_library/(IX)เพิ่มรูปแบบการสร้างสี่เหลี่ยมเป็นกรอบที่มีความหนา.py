# โค้ดสร้างกรอบสี่เหลี่ยมที่มีความหนา
print('---------- Drawing the square frame with thickness ----------')
print('[To quit the program, press "0"]')
print("-----------------------------------------------------------")

while True:
    size = int(input("Please enter the size (at least 3): "))
    thickness = int(input("Please enter the frame thickness: "))

    if size == 0 or thickness == 0:
        break
    elif size >= 3 and thickness < size // 2:
        for i in range(size):
            if i < thickness or i >= size - thickness:  # แถวที่เป็นส่วนกรอบบน/ล่าง
                print("#" * size)
            else:  # แถวที่เป็นกรอบด้านข้าง
                print("#" * thickness + " " * (size - 2 * thickness) + "#" * thickness)
    else:
        print("Invalid input. Please enter valid size and thickness.")
