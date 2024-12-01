def main():
    # แถวที่ 1 ถึงแถวที่ 5
    row1 = [1]
    row2 = [row1[0], 2]
    row3 = [row2[1], row2[0] + row2[1], row2[1] + (row2[0] + row2[1])]
    row4 = [
        row3[2],                         # 5
        row3[1] + row3[2],               # 7
        row3[2] + (row3[1] + row3[2]),   # 10
        row3[2] + (row3[2] + (row3[1] + row3[2]))  # 15
    ]
    row5 = [
        row4[-1],                          # ตัวแรก: เลขสุดท้ายของแถวที่ 4
        row4[-1] + row4[0],                # ตัวที่สอง
        row4[-1] + row4[0] + row4[1],      # ตัวที่สาม
        row4[-1] + row4[0] + row4[1] + row4[2],  # ตัวที่สี่
        row4[-1] + row4[0] + row4[1] + row4[2] + row4[3]  # ตัวที่ห้า
    ]

    # สร้างแถวที่ 6
    row6 = [
        row5[-1],                          # ตัวแรก: เลขสุดท้ายของแถวที่ 5
        row5[-1] + row5[0],                # ตัวที่สอง
        row5[-1] + row5[0] + row5[1],      # ตัวที่สาม
        row5[-1] + row5[0] + row5[1] + row5[2],  # ตัวที่สี่
        row5[-1] + row5[0] + row5[1] + row5[2] + row5[3],  # ตัวที่ห้า
        row5[-1] + row5[0] + row5[1] + row5[2] + row5[3] + row5[4]  # ตัวที่หก
    ]

    # แสดงผล
    print("แถวที่ 1:", *row1)
    print("แถวที่ 2:", *row2)
    print("แถวที่ 3:", *row3)
    print("แถวที่ 4:", *row4)
    print("แถวที่ 5:", *row5)
    print("แถวที่ 6:", *row6)

if __name__ == "__main__":
    main()