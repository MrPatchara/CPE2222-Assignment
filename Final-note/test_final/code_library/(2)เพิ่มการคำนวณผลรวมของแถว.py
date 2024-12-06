# โปรแกรมนี้สร้างแถวตัวเลขแบบสะสม โดยเริ่มจากแถวแรกด้วยเลข 1 
# และคำนวณแต่ละตัวในแถวถัดไปโดยใช้ผลรวมของเลขในแถวก่อนหน้า
# สามารถเลือกแถวที่ต้องการดูได้ และออกจากโปรแกรมเมื่อป้อน -1
def generate_rows(num_rows):
    rows = [[1]]  # เริ่มต้นด้วยแถวที่ 0
    for i in range(1, num_rows + 1):
        previous_row = rows[-1]  # แถวก่อนหน้า
        new_row = [previous_row[-1]]  # ตัวแรก: เลขสุดท้ายของแถวก่อนหน้า
        for j in range(len(previous_row)): # วนลูปเพื่อสร้างตัวเลขใหม่
            new_row.append(new_row[-1] + previous_row[j])  # สร้างตัวเลขใหม่จากผลรวม
        rows.append(new_row)  # เพิ่มแถวใหม่เข้าไปในรายการ
    return rows

def main():
    rows = []  # เก็บผลลัพธ์ของแถว
    while True:
        try:
            user_row = int(input("Please Enter Degree : "))
            if user_row == -1:
                print("ออกจากโปรแกรม")
                break
            if user_row < 0:
                print("กรุณากรอกหมายเลขแถวที่เป็นค่าบวกหรือศูนย์")
                continue
            if len(rows) <= user_row:
                rows = generate_rows(user_row)
            print(f"Row {user_row}: {rows[user_row]}\n")
        except ValueError:
            print("กรุณากรอกตัวเลขที่ถูกต้อง")

if __name__ == "__main__":
    main()