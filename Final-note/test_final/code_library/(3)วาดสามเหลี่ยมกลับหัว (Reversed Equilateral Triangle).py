while True:
    # รับค่าความสูงของสามเหลี่ยมจากผู้ใช้
    height = int(input("Enter the height of reversed equilateral triangle: "))

    if height == 0:  # หากใส่ 0 จะออกจากโปรแกรม
        break

    # วาดสามเหลี่ยมกลับหัวตามความสูงที่กำหนด
    for i in range(height, 0, -1):
        spaces = ' ' * (height - i)  # ช่องว่างด้านซ้าย
        stars = '*' * (2 * i - 1)  # จำนวน * ในแต่ละแถว
        print(spaces + stars)  # แสดงผล
    print()  # ขึ้นบรรทัดใหม่