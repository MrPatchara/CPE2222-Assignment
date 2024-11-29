import matplotlib.pyplot as plt

data_game = ['a', 1, 9, 4.8, 'b', 3, 2, 3.2, 'c', 3, 2, 3.2, 'd', 2, 4, 4.3, 
            'e', 1, 12, 6.4, 'f', 4, 2, 4.3, 'g', 2, 3, 3.2, 'h', 4, 2, 4.3, 
            'i', 1, 9, 4.8, 'j', 8, 1, 4.3, 'k', 5, 1, 2.7, 'l', 1, 4, 2.1, 
            'm', 3, 2, 3.2, 'n', 1, 6, 3.2, 'o', 1, 8, 4.3, 'p', 3, 2, 3.2, 
            'q', 10, 1, 5.3, 'r', 1, 6, 3.2, 's', 1, 4, 2.1, 't', 1, 6, 3.2, 
            'u', 1, 4, 2.1, 'v', 4, 2, 4.3, 'w', 4, 2, 4.3, 'x', 8, 1, 4.3, 
            'y', 4, 2, 4.3, 'z', 10, 1, 5.3]

# แบ่งข้อมูลออกเป็น sublists (เหมือนเดิม)
sublists = [data_game[i:i+4] for i in range(0, len(data_game), 4)]

# ดึงข้อมูลตัวอักษร, คะแนน, จำนวน และอัตราส่วน
letters = [sublist[0] for sublist in sublists]
points = [sublist[1] for sublist in sublists]
amounts = [sublist[2] for sublist in sublists]
ratios = [sublist[3] for sublist in sublists]

# สร้างกราฟแท่งแสดงคะแนน
plt.figure(figsize=(10, 6))
plt.bar(letters, points, color='skyblue', label='Points')
plt.xlabel('Letters')
plt.ylabel('Points')
plt.title('Points per Letter')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# สร้างกราฟเส้นแสดงอัตราส่วน
plt.figure(figsize=(10, 6))
plt.plot(letters, ratios, marker='o', color='orange', label='Ratios')
plt.xlabel('Letters')
plt.ylabel('Ratios')
plt.title('Ratios per Letter')
plt.legend()
plt.grid(alpha=0.7)
plt.show()
