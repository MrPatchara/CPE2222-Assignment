# โปรแกรมนี้เป็นโปรแกรมที่ใช้ในการหาความแตกต่างของตัวอักษรในสตริง A และ B
user_a = str(input('Please enter the string A : '))
user_b = str(input('Please enter the string B : '))

set_a = set(user_a)
set_b = set(user_b)

print('--------------------------------------------------')
print(f'A number of character in A is {len(set_a)}')
print(f'A number of character in B is {len(set_b)}')
print(f'A number of character in both A in B is {len(set_a & set_b)}')
print(f'Character in A but not in B is {set_a - set_b}')
print(f'Character in B but not in A is {set_b - set_a}')
print(f'Character in A or B but not in both A and B is {set_a ^ set_b}')
print(f'All character in A or B is {set_a | set_b}\n')