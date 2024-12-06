while True:
    # รับค่าความสูงและความชันจากผู้ใช้
    height = int(input("Enter the height of scalene triangle: "))
    slope = int(input("Enter the slope (number of stars added per row): "))

    if height == 0:  # หากใส่ 0 จะออกจากโปรแกรม
        break

    # วาดสามเหลี่ยมด้านไม่เท่าตามความสูงและความชันที่กำหนด
    for i in range(1, height + 1):
        stars = '*' * (i * slope)  # จำนวน * ในแต่ละแถวขึ้นอยู่กับความชัน
        print(stars)  # แสดงผล
    print()  # ขึ้นบรรทัดใหม่