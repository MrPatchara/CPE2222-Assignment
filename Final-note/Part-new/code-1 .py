# 1 โปรแกรมในการรับค่าของจำนวนบรรทัด (Line) ของรูปสามเหลี่ยม (Triangle) แล้วใช้อักษร ‘*’ วาดรูปสามเหลี่ยมดังแสดงในรูปต่อไปนี้ โดยโปรแกรมจะวนซ้ำรับค่าไปเรื่อยๆ จะกว่าจะพิมพ์เลข ‘0’

print("-" * 25, "Drawing the triangle by", "-" * 25)
print("[To quit this program by pressing '0']")
print("-" * 75)
while True:
    try:
        # รับค่าจำนวนบรรทัดจากผู้ใช้
        user_input = input("Please enter the line of triangle: ")
        lines = int(user_input)  # แปลงค่าที่ป้อนเป็นจำนวนเต็ม

        # ตรวจสอบว่าผู้ใช้ต้องการออกจากโปรแกรม
        if lines == 0:
            print("Exit the program!")
            break

        # วาดรูปสามเหลี่ยมเว้นตรงกลาง
        for i in range(1, lines + 1):
            if i == 1:
                # ยอดสามเหลี่ยม
                print(' ' * (lines - i) + '*')
            elif i == lines:
                # ฐานสามเหลี่ยม
                print('*' * (2 * i - 1))
            else:
                # บรรทัดอื่นๆ
                print(' ' * (lines - i) + '*' + ' ' * (2 * (i - 1) - 1) + '*')

    except ValueError:
        print("กรุณาใส่ตัวเลขเท่านั้น!")
