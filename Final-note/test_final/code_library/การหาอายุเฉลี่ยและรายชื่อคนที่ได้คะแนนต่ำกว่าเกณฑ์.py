# โปรแกรมค้นหาข้อมูลบุคคลในรายชื่อ
id = {'Peter' : {'Age': 40 , 'Gender': 'Male', 'Test': {'First': 20, 'Second': 18, 'Third': 19}},
      'Paul' : {'Age': 25, 'Gender': 'Male', 'Test': {'First' : 19, 'Second': 20, 'Third': 19}},
      'Mary' : {'Age': 18, 'Gender': 'Female', 'Test': {'First': 10, 'Second': 5, 'Third': 4}},
      'Jenny' : {'Age': 60, 'Gender': 'Female', 'Test': {'First': 5, 'Second': 3, 'Third': 1}}}

# ฟังก์ชันค้นหาข้อมูลบุคคลตามชื่อ
def search_person(name):
    if name in id:
        data = id[name]
        avg_score = data.get('Average', "N/A")
        print(f"Name: {name}")
        print(f"Age: {data['Age']}")
        print(f"Gender: {data['Gender']}")
        print(f"Scores: {data['Test']}")
        print(f"Average Score: {avg_score}")
    else:
        print(f"No data found for {name}")

# ทดสอบการค้นหาข้อมูล
search_person("Mary")
search_person("John")
