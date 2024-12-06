while True:
    # รับค่าความสูงของสามเหลี่ยมจากผู้ใช้
    height = int(input("Enter the height of nested triangles: "))

    if height == 0:  # หากใส่ 0 จะออกจากโปรแกรม
        break

    # วาดสามเหลี่ยมซ้อนกัน
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            stars = '*' * j
            print(stars.center(height * 2))  # จัดตรงกลาง
    print()  # ขึ้นบรรทัดใหม่