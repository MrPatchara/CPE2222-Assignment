while True:
    # รับค่าความสูงของสามเหลี่ยมจากผู้ใช้
    height = int(input("Enter the height of hollow equilateral triangle: "))

    if height == 0:  # หากใส่ 0 จะออกจากโปรแกรม
        break

    # วาดสามเหลี่ยมด้านเท่าแบบกลวง
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)  # ช่องว่างด้านซ้าย
        if i == 1:  # แถวแรกมีแค่ *
            stars = '*'
        elif i == height:  # แถวสุดท้ายเต็มแถว
            stars = '*' * (2 * i - 1)
        else:  # แถวอื่นๆ จะเป็นแบบกลวง
            stars = '*' + ' ' * (2 * i - 3) + '*'
        print(spaces + stars)  # แสดงผล
    print()  # ขึ้นบรรทัดใหม่