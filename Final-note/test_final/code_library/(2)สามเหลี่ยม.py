#โปรแกรมรับค่า Degree ของสามเหลี่ยมนี้ แล้วแสดงรายการ (List) สัมประสิทธิ์ของ Degree นั้น

def generate_rows(num_rows): # สร้างแถวของสามเหลี่ยมพาสกาล
    rows = [[1]]  # เริ่มต้นด้วยแถวที่ 0

    for i in range(1, num_rows + 1): # สร้างแถวตามจำนวนที่ระบุ
        previous_row = rows[-1]  # แถวก่อนหน้า
        new_row = [previous_row[-1]]  # ตัวแรก: เลขสุดท้ายของแถวก่อนหน้า

        for j in range(len(previous_row)): # สร้างตัวเลขใหม่จากผลรวม
            new_row.append(new_row[-1] + previous_row[j])  # สร้างตัวเลขใหม่จากผลรวม

        rows.append(new_row)  # เพิ่มแถวใหม่เข้าไปในรายการ

    return rows

def main():
    rows = []  # เก็บผลลัพธ์ของแถว
    while True:
        try:
            user_row = int(input("Please Enter Degree : "))
            
            # ออกจากโปรแกรมเมื่อป้อน -1
            if user_row == -1: # ออกจากโปรแกรม
                print("ออกจากโปรแกรม")
                break

            # ตรวจสอบว่าเป็นค่าไม่ลบ (ยกเว้น -1 เพื่อออก)
            if user_row < 0: # ตรวจสอบว่าเป็นค่าไม่ลบ (ยกเว้น -1 เพื่อออก)
                print("กรุณากรอกหมายเลขแถวที่เป็นค่าบวกหรือศูนย์")
                continue

            # สร้างแถวที่จำเป็นหากยังไม่เคยคำนวณ
            if len(rows) <= user_row: # สร้างแถวที่จำเป็นหากยังไม่เคยคำนวณ
                rows = generate_rows(user_row)

            # แสดงผลแถวที่เลือก
            print(f"{rows[user_row]}\n") 

        except ValueError:
            print("กรุณากรอกตัวเลขที่ถูกต้อง")

if __name__ == "__main__":
    main()