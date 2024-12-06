# โปรแกรมที่ทำการสร้างลิสต์ของ Factorial series ของ n ที่รับค่า n จากผู้ใช้
print('Making a list of Factorial series of n')
n = int(input("Enter 'n' of Factorial number:"))
result = 1
list_of_n = []

for i in range(1, n+1):
    result *= i
    list_of_n.append(result)
    
print(f"A list of Factorial series of {n} is {list_of_n}\n")
