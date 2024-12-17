while True:
    try:
        # รับค่าจำนวนบรรทัดจากผู้ใช้
        user_input = input("Please enter the line of triangle: ")
        lines = int(user_input)  # แปลงค่าที่ป้อนเป็นจำนวนเต็ม

        # ตรวจสอบป้อน 0
        if lines == 0:
            print("Exit the program!")
            break

        # วาดรูปสามเหลี่ยมเว้นตรงกลาง
        for i in range(1, lines + 1):
            if i == 1:
                print(' ' * (lines - i) + '*')
            elif i == lines:
                print('*' * (2 * i - 1))
            else:
                print(' ' * (lines - i) + '*' + ' ' * (2 * (i - 1) - 1) + '*')

    except ValueError:
        print("Only number only!")
