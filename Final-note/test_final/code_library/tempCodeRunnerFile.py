# โปรแกรมวาดสามเหลี่ยมกลับด้านตามความสูงที่กำหนด
# Drawing a reversed right triangle using '*'
while True:
    # รับค่าความสูงของสามเหลี่ยมจากผู้ใช้
    height = int(input("Enter the height of right triangle: "))

    # หากใส่ 0 จะออกจากโปรแกรม
    if height == 0: # ถ้าความสูงเป็น 0
        break

    # วาดสามเหลี่ยมกลับด้านตามความสูงที่กำหนด
    for i in range(1, height + 1): # วนลูปตามความสูง
        spaces = ' ' * (height - i)  # ช่องว่างด้านซ้าย
        if i == 1:  # แถวแรกมีแค่ *
            stars = '*' # สร้างดาว
        elif i == height:  # แถวสุดท้ายเต็มแถว
            stars = '*' * i # สร้างดาวตามความสูง
        else:  # แถวอื่นๆ มี * เว้นช่องว่างตรงกลาง
            stars = '*' + ' ' * (i - 2) + '*' # สร้างดาวและช่องว่างตรงกลาง
        print(spaces + stars)  # แสดงผล
    print()  # ขึ้นบรรทัดใหม่