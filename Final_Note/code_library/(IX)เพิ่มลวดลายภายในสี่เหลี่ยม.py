# โค้ดสร้างสี่เหลี่ยมที่มีลวดลายเป็นจุดไขว้ด้านใน
print('---------- Drawing patterned squares ----------')
print('[To quit the program, press "0"]')
print("-----------------------------------------------------------")

while True:
    size = int(input("Please enter the size (at least 5): "))

    if size == 0:
        break
    elif size >= 5:
        for i in range(size):
            if i == 0 or i == size - 1:  # ขอบบน/ล่าง
                print("#" * size)
            else:
                row = [" "] * size
                row[0] = "#"
                row[size - 1] = "#"
                row[i] = "#"
                row[size - i - 1] = "#"
                print("".join(row))
    else:
        print("Invalid input. Please enter a size >= 5.")
