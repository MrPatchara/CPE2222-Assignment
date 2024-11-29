data_game = ['a', 1, 9, 4.8, 'b', 3, 2, 3.2, 'c', 3, 2, 3.2, 'd', 2, 4, 4.3, 
            'e', 1, 12, 6.4, 'f', 4, 2, 4.3, 'g', 2, 3, 3.2, 'h', 4, 2, 4.3, 
            'i', 1, 9, 4.8, 'j', 8, 1, 4.3, 'k', 5, 1, 2.7, 'l', 1, 4, 2.1, 
            'm', 3, 2, 3.2, 'n', 1, 6, 3.2, 'o', 1, 8, 4.3, 'p', 3, 2, 3.2, 
            'q', 10, 1, 5.3, 'r', 1, 6, 3.2, 's', 1, 4, 2.1, 't', 1, 6, 3.2, 
            'u', 1, 4, 2.1, 'v', 4, 2, 4.3, 'w', 4, 2, 4.3, 'x', 8, 1, 4.3, 
            'y', 4, 2, 4.3, 'z', 10, 1, 5.3]

# ฟังก์ชัน: กรองข้อมูลตามเกณฑ์ที่ผู้ใช้กำหนด
def filter_by_user_input(lst):
    print("Enter minimum points:")
    min_points = int(input())
    print("Enter maximum ratio:")
    max_ratio = float(input())
    filtered = [sublist for sublist in lst if sublist[1] >= min_points and sublist[3] <= max_ratio]
    return filtered

# แบ่งข้อมูลออกเป็น sublists (เหมือนเดิม)
sublists = [data_game[i:i+4] for i in range(0, len(data_game), 4)]

# กรองข้อมูลด้วย Input จากผู้ใช้
filtered_sublists = filter_by_user_input(sublists)

# แสดงผลลัพธ์
print("Filtered Sublists:")
for sublist in filtered_sublists:
    print(sublist)
