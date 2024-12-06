while True:
    # รับค่าความสูงของเพชรจากผู้ใช้
    height = int(input("Enter the height of the diamond (must be odd): "))

    if height == 0:  # หากใส่ 0 จะออกจากโปรแกรม
        break
    if height % 2 == 0:
        print("Height must be an odd number!")
        continue

    # วาดส่วนบนของเพชร
    for i in range(1, height + 1, 2):
        spaces = ' ' * ((height - i) // 2)
        stars = '*' * i
        print(spaces + stars)

    # วาดส่วนล่างของเพชร
    for i in range(height - 2, 0, -2):
        spaces = ' ' * ((height - i) // 2)
        stars = '*' * i
        print(spaces + stars)
    print()  # ขึ้นบรรทัดใหม่