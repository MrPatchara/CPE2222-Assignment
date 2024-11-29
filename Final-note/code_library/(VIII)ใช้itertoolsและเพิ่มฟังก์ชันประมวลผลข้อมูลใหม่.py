import itertools

# ข้อมูลเกม (เหมือนเดิม)
data_game = ['a', 1, 9, 4.8, 'b', 3, 2, 3.2, 'c', 3, 2, 3.2, 'd', 2, 4, 4.3, 
             'e', 1, 12, 6.4, 'f', 4, 2, 4.3, 'g', 2, 3, 3.2, 'h', 4, 2, 4.3, 
             'i', 1, 9, 4.8, 'j', 8, 1, 4.3, 'k', 5, 1, 2.7, 'l', 1, 4, 2.1, 
             'm', 3, 2, 3.2, 'n', 1, 6, 3.2, 'o', 1, 8, 4.3, 'p', 3, 2, 3.2, 
             'q', 10, 1, 5.3, 'r', 1, 6, 3.2, 's', 1, 4, 2.1, 't', 1, 6, 3.2, 
             'u', 1, 4, 2.1, 'v', 4, 2, 4.3, 'w', 4, 2, 4.3, 'x', 8, 1, 4.3, 
             'y', 4, 2, 4.3, 'z', 10, 1, 5.3]

# แบ่งข้อมูลออกเป็น sublists โดยใช้ itertools.islice
sublists = list(itertools.islice(itertools.zip_longest(*[iter(data_game)]*4), 0, len(data_game)//4))
data_game = ['a', 1, 9, 4.8, 'b', 3, 2, 3.2, 'c', 3, 2, 3.2, 'd', 2, 4, 4.3, 
            'e', 1, 12, 6.4, 'f', 4, 2, 4.3, 'g', 2, 3, 3.2, 'h', 4, 2, 4.3, 
            'i', 1, 9, 4.8, 'j', 8, 1, 4.3, 'k', 5, 1, 2.7, 'l', 1, 4, 2.1, 
            'm', 3, 2, 3.2, 'n', 1, 6, 3.2, 'o', 1, 8, 4.3, 'p', 3, 2, 3.2, 
            'q', 10, 1, 5.3, 'r', 1, 6, 3.2, 's', 1, 4, 2.1, 't', 1, 6, 3.2, 
            'u', 1, 4, 2.1, 'v', 4, 2, 4.3, 'w', 4, 2, 4.3, 'x', 8, 1, 4.3, 
            'y', 4, 2, 4.3, 'z', 10, 1, 5.3]

# ฟังก์ชัน: จัดอันดับตัวอักษรที่ปรากฏบ่อยที่สุด
def get_top_frequencies(data, n=5):
    # สร้าง dict เพื่อเก็บจำนวนตัวอักษร
    frequency = {}
    for sublist in data:
        letter = sublist[0]
        frequency[letter] = frequency.get(letter, 0) + 1
    
    # เรียงลำดับข้อมูลตามค่าที่สูงสุด
    return sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:n]

# ฟังก์ชัน: เพิ่มค่าคะแนนให้ทุก sublist โดยการคำนวณแต้มสะสม
def add_accumulated_score(data):
    total_score = 0
    for sublist in data:
        total_score += sublist[1]  # เพิ่มคะแนนในตำแหน่งที่ 1
        sublist.append(total_score)  # เพิ่มคะแนนสะสมลงใน sublist
    return data

# เพิ่มคะแนนสะสมใน sublists
sublists = add_accumulated_score(sublists)

# แสดงข้อมูล
print("Sublists with accumulated scores:")
for sublist in sublists:
    print(sublist)

# ค้นหาตัวอักษรที่ปรากฏบ่อยที่สุด
top_frequencies = get_top_frequencies(sublists)
print("\nTop frequent letters:")
for i, (letter, freq) in enumerate(top_frequencies):
    print(f"    {i+1}) '{letter}' appears {freq} times.")
