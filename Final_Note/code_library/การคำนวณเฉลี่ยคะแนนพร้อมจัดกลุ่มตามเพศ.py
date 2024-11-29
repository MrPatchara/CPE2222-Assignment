# ข้อมูลต้นฉบับ
id = {'Peter': {'Age': 40, 'Gender': 'Male', 'Test': {'First': 20, 'Second': 18, 'Third': 19}},
      'Paul': {'Age': 25, 'Gender': 'Male', 'Test': {'First': 19, 'Second': 20, 'Third': 19}},
      'Mary': {'Age': 18, 'Gender': 'Female', 'Test': {'First': 10, 'Second': 5, 'Third': 4}},
      'Jenny': {'Age': 60, 'Gender': 'Female', 'Test': {'First': 5, 'Second': 3, 'Third': 1}}}

# เพิ่มการคำนวณคะแนนเฉลี่ยและจัดกลุ่มตามเพศ
grouped_data = {'Male': [], 'Female': []}

for name, data in id.items():
    # คำนวณคะแนนเฉลี่ยของแต่ละคน
    avg_score = sum(data['Test'].values()) / len(data['Test'])
    data['Average'] = avg_score  # เพิ่มข้อมูลคะแนนเฉลี่ยใน dictionary
    
    # จัดกลุ่มตามเพศ
    grouped_data[data['Gender']].append({'Name': name, 'Average': avg_score})

# แสดงผลข้อมูลที่จัดกลุ่มแล้ว
for gender, individuals in grouped_data.items():
    print(f"--- {gender} ---")
    for person in individuals:
        print(f"{person['Name']} has an average score of {person['Average']:.2f}")
