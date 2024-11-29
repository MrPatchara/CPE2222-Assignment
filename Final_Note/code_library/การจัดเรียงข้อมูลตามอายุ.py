id = {'Peter' : {'Age': 40 , 'Gender': 'Male', 'Test': {'First': 20, 'Second': 18, 'Third': 19}},
      'Paul' : {'Age': 25, 'Gender': 'Male', 'Test': {'First' : 19, 'Second': 20, 'Third': 19}},
      'Mary' : {'Age': 18, 'Gender': 'Female', 'Test': {'First': 10, 'Second': 5, 'Third': 4}},
      'Jenny' : {'Age': 60, 'Gender': 'Female', 'Test': {'First': 5, 'Second': 3, 'Third': 1}}}

# จัดเรียงข้อมูลตามอายุจากมากไปน้อย
sorted_by_age = sorted(id.items(), key=lambda item: item[1]['Age'], reverse=True)

# แสดงข้อมูลที่จัดเรียงแล้ว
print("Data sorted by age:")
for name, data in sorted_by_age:
    print(f"{name}: {data['Age']} years old")
