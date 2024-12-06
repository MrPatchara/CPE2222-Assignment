# โปรแกรมวาดสามเหลี่ยมหน้าจั่วตามความสูงที่กำหนด
while True:
    # รับค่าความสูงของสามเหลี่ยมจากผู้ใช้
    height = int(input("Enter the height of isosceles triangle: "))

    if height == 0:  # หากใส่ 0 จะออกจากโปรแกรม
        break

    # วาดสามเหลี่ยมหน้าจั่วตามความสูงที่กำหนด
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)  # ช่องว่างด้านซ้าย
        stars = '*' * i  # จำนวน * ในแต่ละแถว
        print(spaces + stars)  # แสดงผล
    print()  # ขึ้นบรรทัดใหม่