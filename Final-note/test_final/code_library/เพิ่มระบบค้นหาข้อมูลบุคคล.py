# โปรแกรมแสดงข้อมูลของนักเรียน และเพิ่มข้อมูลของนักเรียนคนใหม่
id = {'Peter' : {'Age': 40 , 'Gender': 'Male', 'Test': {'First': 20, 'Second': 18, 'Third': 19}},
      'Paul' : {'Age': 25, 'Gender': 'Male', 'Test': {'First' : 19, 'Second': 20, 'Third': 19}},
      'Mary' : {'Age': 18, 'Gender': 'Female', 'Test': {'First': 10, 'Second': 5, 'Third': 4}},
      'Jenny' : {'Age': 60, 'Gender': 'Female', 'Test': {'First': 5, 'Second': 3, 'Third': 1}}}

print(f'"Peter" is {id['Peter']['Gender']}')
print(f'The 1st test score of "Mary" is {id['Mary']['Test']['First']}')
print(f'The 2st test score of "Jenny" is {id['Jenny']['Test']['Second']}')
print(f'The 3st test score of "Paul" is {id['Paul']['Test']['Third']}')

id['Robert'] = {'Age': 35, 'Gender': 'Male', 'Test' : {'First': 10, 'Second': 18, 'Third': 5}}

print(f'"Robert" is {id['Robert']['Age']} years old')
print('The dictionary to solve this problem was designed as:')

for name, data in id.items():
    print(f'{name} : {data}')