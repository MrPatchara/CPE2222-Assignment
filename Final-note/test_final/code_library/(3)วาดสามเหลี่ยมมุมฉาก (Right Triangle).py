while True:
    # รับค่าความสูงของสามเหลี่ยมจากผู้ใช้
    height = int(input("Enter the height of right triangle: "))

    if height == 0:  # หากใส่ 0 จะออกจากโปรแกรม
        break

    # วาดสามเหลี่ยมมุมฉาก
    for i in range(1, height + 1):
        stars = '*' * i  # จำนวน * เพิ่มขึ้นทีละ 1 ในแต่ละแถว
        print(stars)  # แสดงผล
    print()  # ขึ้นบรรทัดใหม่