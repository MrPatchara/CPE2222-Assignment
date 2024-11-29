id = {'Peter' : {'Age': 40 , 'Gender': 'Male', 'Test': {'First': 20, 'Second': 18, 'Third': 19}},
      'Paul' : {'Age': 25, 'Gender': 'Male', 'Test': {'First' : 19, 'Second': 20, 'Third': 19}},
      'Mary' : {'Age': 18, 'Gender': 'Female', 'Test': {'First': 10, 'Second': 5, 'Third': 4}},
      'Jenny' : {'Age': 60, 'Gender': 'Female', 'Test': {'First': 5, 'Second': 3, 'Third': 1}}}

import json

# เพิ่มข้อมูลคะแนนเฉลี่ยใน dictionary
for name, data in id.items():
    data['Average'] = sum(data['Test'].values()) / len(data['Test'])

# บันทึกข้อมูลลงไฟล์ JSON
with open('output.json', 'w') as file:
    json.dump(id, file, indent=4)

print("Data has been saved to 'output.json'")
