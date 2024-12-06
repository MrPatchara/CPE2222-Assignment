# โปรแกรมจำลองการเพิ่มแต้มแบบสุ่มในเกม Scrabble

data_game = ['a', 1, 9, 4.8, 'b', 3, 2, 3.2, 'c', 3, 2, 3.2, 'd', 2, 4, 4.3, 
            'e', 1, 12, 6.4, 'f', 4, 2, 4.3, 'g', 2, 3, 3.2, 'h', 4, 2, 4.3, 
            'i', 1, 9, 4.8, 'j', 8, 1, 4.3, 'k', 5, 1, 2.7, 'l', 1, 4, 2.1, 
            'm', 3, 2, 3.2, 'n', 1, 6, 3.2, 'o', 1, 8, 4.3, 'p', 3, 2, 3.2, 
            'q', 10, 1, 5.3, 'r', 1, 6, 3.2, 's', 1, 4, 2.1, 't', 1, 6, 3.2, 
            'u', 1, 4, 2.1, 'v', 4, 2, 4.3, 'w', 4, 2, 4.3, 'x', 8, 1, 4.3, 
            'y', 4, 2, 4.3, 'z', 10, 1, 5.3]

import random

# สร้างฟังก์ชันจำลองการเพิ่มแต้มแบบสุ่ม
def simulate_random_scores(lst, min_add=1, max_add=5):
    for sublist in lst:
        sublist[1] += random.randint(min_add, max_add)
    return lst

# แบ่งข้อมูลออกเป็น sublists (เหมือนเดิม)
sublists = [data_game[i:i+4] for i in range(0, len(data_game), 4)]

# เพิ่มแต้มแบบสุ่ม
updated_sublists = simulate_random_scores(sublists)

# แสดงข้อมูลหลังเพิ่มแต้ม
print("Updated Sublists with Random Scores:")
for sublist in updated_sublists:
    print(sublist)
