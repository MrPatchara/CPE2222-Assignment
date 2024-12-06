while True:
    # รับค่าความสูงของสามเหลี่ยมจากผู้ใช้
    height = int(input("Enter the height of reversed right triangle: "))

    if height == 0:  # หากใส่ 0 จะออกจากโปรแกรม
        break

    # วาดสามเหลี่ยมมุมฉากกลับหัว
    for i in range(height, 0, -1):
        stars = '*' * i  # จำนวน * ลดลงทีละ 1 ในแต่ละแถว
        print(stars)  # แสดงผล
    print()  # ขึ้นบรรทัดใหม่