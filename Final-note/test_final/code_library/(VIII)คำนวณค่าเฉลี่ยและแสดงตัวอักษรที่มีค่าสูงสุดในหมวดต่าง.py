# โปรแกรม: คำนวณค่าเฉลี่ยและค้นหาค่าสูงสุดจากข้อมูลเกม
# ข้อมูลเกม (เหมือนเดิม)
data_game = ['a', 1, 9, 4.8, 'b', 3, 2, 3.2, 'c', 3, 2, 3.2, 'd', 2, 4, 4.3, 
             'e', 1, 12, 6.4, 'f', 4, 2, 4.3, 'g', 2, 3, 3.2, 'h', 4, 2, 4.3, 
             'i', 1, 9, 4.8, 'j', 8, 1, 4.3, 'k', 5, 1, 2.7, 'l', 1, 4, 2.1, 
             'm', 3, 2, 3.2, 'n', 1, 6, 3.2, 'o', 1, 8, 4.3, 'p', 3, 2, 3.2, 
             'q', 10, 1, 5.3, 'r', 1, 6, 3.2, 's', 1, 4, 2.1, 't', 1, 6, 3.2, 
             'u', 1, 4, 2.1, 'v', 4, 2, 4.3, 'w', 4, 2, 4.3, 'x', 8, 1, 4.3, 
             'y', 4, 2, 4.3, 'z', 10, 1, 5.3]

# แบ่งข้อมูลออกเป็น sublists
sublists = [data_game[i:i+4] for i in range(0, len(data_game), 4)]

# ฟังก์ชัน: คำนวณค่าเฉลี่ยจาก index ที่กำหนด
def calculate_average(lst, index):
    return sum(sublist[index] for sublist in lst) / len(lst)

# ฟังก์ชัน: ดึงตัวอักษรที่มีค่ามากที่สุดใน index ที่กำหนด
def get_highest_by_index(lst, index):
    return max(lst, key=lambda x: x[index])

# คำนวณค่าเฉลี่ย
avg_points = calculate_average(sublists, 1)
avg_amount = calculate_average(sublists, 2)
avg_ratio = calculate_average(sublists, 3)

# ค้นหาค่าที่สูงสุด
highest_point = get_highest_by_index(sublists, 1)
highest_amount = get_highest_by_index(sublists, 2)
highest_ratio = get_highest_by_index(sublists, 3)

# แสดงผลลัพธ์
print(f"Average Points: {avg_points:.2f}")
print(f"Average Amount: {avg_amount:.2f}")
print(f"Average Ratio: {avg_ratio:.2f}")

print("\nHighest values in each category:")
print(f"    Points: '{highest_point[0]}' with {highest_point[1]} points.")
print(f"    Amount: '{highest_amount[0]}' with {highest_amount[2]} pieces.")
print(f"    Ratio: '{highest_ratio[0]}' with {highest_ratio[3]} percent.")
